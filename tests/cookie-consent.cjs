const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const ROOT = path.resolve(__dirname, "..");
const SITE_ORIGIN = "https://www.ino-elektra.nl";

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".webp": "image/webp",
  ".jpg": "image/jpeg",
  ".woff2": "font/woff2",
  ".json": "application/json",
};

function resolveLocalFile(urlPath) {
  let clean = decodeURIComponent(urlPath.split("?")[0].split("#")[0]);
  if (clean === "/") return path.join(ROOT, "index.html");
  const rel = clean.replace(/^\/+/, "");
  const direct = path.join(ROOT, rel);
  if (fs.existsSync(direct) && fs.statSync(direct).isFile()) return direct;
  const idx = path.join(ROOT, rel, "index.html");
  if (fs.existsSync(idx) && fs.statSync(idx).isFile()) return idx;
  return null;
}

// Realistic browser-side Google tag simulator: only executes if gtag/js is actually fetched!
const GTAG_STUB = `
(function(){
  var dl = window.dataLayer = window.dataLayer || [];
  var state = { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' };
  function setCookie(n, v){ document.cookie = n + '=' + v + '; path=/; SameSite=Lax'; }
  function process(args){
    var a = Array.from(args);
    var cmd = a[0];
    if (cmd === 'consent' && (a[1] === 'default' || a[1] === 'update') && a[2]) {
      Object.assign(state, a[2]);
    } else if (cmd === 'config') {
      var id = String(a[1] || '');
      if (id.indexOf('G-') === 0 && state.analytics_storage === 'granted') {
        setCookie('_ga', 'GA1.1.123456789');
        setCookie('_ga_' + id.slice(2), 'GS1.1.987654321');
        setCookie('_gid', 'GA1.1.11223344');
        fetch('https://www.google-analytics.com/g/collect?v=2&tid=' + encodeURIComponent(id) + '&en=page_view').catch(function(){});
      }
      if (id.indexOf('AW-') === 0 && state.ad_storage === 'granted') {
        setCookie('_gcl_au', '1.1.555666');
        setCookie('_gcl_aw', 'GCL.1700000000.test');
        setCookie('_gac_gb_12345', '1.1.abc');
        fetch('https://www.googleadservices.com/pagead/conversion/' + id.slice(3) + '/?label=config').catch(function(){});
      }
    } else if (cmd === 'event') {
      var ev = String(a[1] || '');
      if (ev === 'conversion_event_contact') {
        if (state.ad_storage === 'granted' || state.ad_user_data === 'granted') {
          fetch('https://www.googleadservices.com/pagead/conversion/7124503256/?label=conversion_event_contact&au=' + state.ad_user_data + '&ap=' + state.ad_personalization).catch(function(){});
        }
      } else if (state.analytics_storage === 'granted') {
        fetch('https://www.google-analytics.com/g/collect?v=2&tid=G-HR6L1S8V7P&en=' + encodeURIComponent(ev)).catch(function(){});
      }
    }
  }
  for (var i = 0; i < dl.length; i++) process(dl[i]);
  var origPush = dl.push.bind(dl);
  dl.push = function(){
    var r = origPush.apply(dl, arguments);
    for (var i = 0; i < arguments.length; i++) process(arguments[i]);
    return r;
  };
})();
`;

async function setupContext(browser, opts = {}) {
  const context = await browser.newContext({ viewport: opts.viewport || { width: 1280, height: 800 } });
  const networkLog = [];

  await context.route("**/*", async (route) => {
    const req = route.request();
    const url = req.url();
    const u = new URL(url);

    if (u.hostname === "www.ino-elektra.nl" || u.hostname === "ino-elektra.nl") {
      const file = resolveLocalFile(u.pathname);
      if (!file) return route.fulfill({ status: 404, body: "Not found" });
      const ext = path.extname(file).toLowerCase();
      return route.fulfill({
        status: 200,
        contentType: MIME[ext] || "application/octet-stream",
        body: fs.readFileSync(file),
      });
    }

    if (u.hostname === "www.googletagmanager.com" && u.pathname.startsWith("/gtag/js")) {
      networkLog.push({ type: "gtag_script", url });
      return route.fulfill({ status: 200, contentType: "application/javascript", body: GTAG_STUB });
    }
    if (u.hostname.includes("google-analytics.com")) {
      networkLog.push({ type: "ga_collect", url });
      return route.fulfill({ status: 204, body: "" });
    }
    if (u.hostname.includes("googleadservices.com") || u.hostname.includes("doubleclick.net") || u.hostname.includes("googlesyndication.com")) {
      networkLog.push({ type: "gads", url });
      return route.fulfill({ status: 204, body: "" });
    }
    if (u.hostname === "challenges.cloudflare.com") {
      const onload = u.searchParams.get("onload") || "inoTurnstileKlaar";
      return route.fulfill({
        status: 200,
        contentType: "application/javascript",
        body: `window.turnstile={render:function(){return "w1";},getResponse:function(){return "mock-turnstile-token";},reset:function(){}};if(typeof window["${onload}"]==="function")window["${onload}"]();`,
      });
    }
    if (u.hostname === "api.ino-elektra.nl" && u.pathname === "/api/form") {
      networkLog.push({ type: "worker_form", url });
      return route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ ok: true }) });
    }
    if (u.hostname === "api.ino-elektra.nl" && u.pathname === "/api/reviews") {
      return route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ ok: true, score: 5.0, aantal: 46, reviews: [] }) });
    }
    return route.abort();
  });

  const page = await context.newPage();
  const pageErrors = [];
  page.on("pageerror", (err) => pageErrors.push(String(err)));

  // Prevent external tel:/wa.me navigations from interrupting the page during conversion tests
  await page.addInitScript(() => {
    window.__openedUrls = [];
    window.open = (u) => { window.__openedUrls.push(String(u)); return null; };
    document.addEventListener("click", (e) => {
      const a = e.target.closest && e.target.closest("a");
      if (!a) return;
      const href = a.getAttribute("href") || "";
      if (href.startsWith("tel:") || href.includes("wa.me")) e.preventDefault();
    });
  });

  const googleRequests = () => networkLog.filter((r) => ["gtag_script", "ga_collect", "gads"].includes(r.type));
  const getDataLayer = () => page.evaluate(() => (window.dataLayer || []).map((entry) => Array.from(entry)));
  const getTrackingCookies = async () => {
    const all = await context.cookies();
    return all.filter((c) => /^(_ga|_gid|_gat|_gcl_|_gac_)/.test(c.name));
  };

  return { context, page, networkLog, googleRequests, getDataLayer, getTrackingCookies, pageErrors };
}

async function run() {
  const browser = await chromium.launch({ headless: true });
  try {
    // 1. Pre-consent (NL & EN)
    {
      const { context, page, googleRequests, getDataLayer, getTrackingCookies, pageErrors } = await setupContext(browser);
      await page.goto(`${SITE_ORIGIN}/`, { waitUntil: "networkidle" });
      assert.equal(googleRequests().length, 0, "Before consent: 0 Google requests");
      assert.equal((await getTrackingCookies()).length, 0, "Before consent: 0 tracking cookies");

      const dl = await getDataLayer();
      assert.deepEqual(dl[0], [
        "consent",
        "default",
        { analytics_storage: "denied", ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", wait_for_update: 500 },
      ]);

      const bannerVisible = await page.locator(".consent").isVisible();
      assert.equal(bannerVisible, true, "Cookie banner must be visible before consent");
      assert.equal(await page.locator("[data-consent-stat]").isChecked(), false, "Analytics checkbox must NOT be pre-checked");
      assert.equal(await page.locator("[data-consent-ads]").isChecked(), false, "Ads checkbox must NOT be pre-checked");

      // Check equal ease of Reject vs Accept buttons
      const neeBox = await page.locator('[data-consent="nee"]').boundingBox();
      const jaBox = await page.locator('[data-consent="ja"]').boundingBox();
      assert(neeBox && jaBox && Math.abs(neeBox.height - jaBox.height) <= 2, "Reject and Accept buttons must have equal height");

      // Click tel & WhatsApp before consent -> 0 events, 0 Google requests
      await page.locator('a[data-track="bellen"]').first().click();
      await page.locator('a[data-track="whatsapp"]').first().click();
      assert.equal(googleRequests().length, 0, "Clicks before consent must emit 0 Google requests");
      const dlAfterClicks = await getDataLayer();
      assert.equal(dlAfterClicks.some((e) => e[0] === "event"), false, "Clicks before consent must emit 0 gtag events");

      // English site pre-consent check
      await page.goto(`${SITE_ORIGIN}/en/`, { waitUntil: "networkidle" });
      assert.equal(googleRequests().length, 0, "EN before consent: 0 Google requests");
      const enText = await page.locator(".consent").innerText();
      assert(enText.includes("Your privacy") && enText.includes("Necessary only") && enText.includes("Accept all"));
      assert.equal(pageErrors.length, 0);
      await context.close();
      console.log("PASS [Chromium] 1. Pre-consent (NL + EN)");
    }

    // 2. Reject All ("Alleen noodzakelijk")
    {
      const { context, page, googleRequests, getDataLayer, getTrackingCookies, pageErrors } = await setupContext(browser);
      await page.goto(`${SITE_ORIGIN}/`, { waitUntil: "networkidle" });
      await page.locator('[data-consent="nee"]').click();
      await page.waitForTimeout(150);

      assert.equal(await page.locator(".consent").isVisible(), false, "Banner closes after reject");
      assert.equal(googleRequests().length, 0, "After reject: 0 Google requests");
      assert.equal((await getTrackingCookies()).length, 0, "After reject: 0 tracking cookies");
      const ls = await page.evaluate(() => JSON.parse(localStorage.getItem("ino_cookies")));
      assert.deepEqual(ls, { stat: false, ads: false });

      await page.locator('a[data-track="bellen"]').first().click();
      await page.locator('a[data-track="whatsapp"]').first().click();
      assert.equal(googleRequests().length, 0, "After reject: clicks send 0 Google requests");

      await page.reload({ waitUntil: "networkidle" });
      assert.equal(await page.locator(".consent").count(), 0, "After reload with rejection: banner stays closed");
      assert.equal(googleRequests().length, 0, "After reload with rejection: 0 Google requests");
      const dl = await getDataLayer();
      assert.equal(dl.some((e) => e[0] === "consent" && e[1] === "update" && Object.values(e[2]).includes("granted")), false);
      assert.equal(pageErrors.length, 0);
      await context.close();
      console.log("PASS [Chromium] 2. Reject All");
    }

    // 3. Analytics-only
    {
      const { context, page, networkLog, googleRequests, getDataLayer, getTrackingCookies, pageErrors } = await setupContext(browser);
      await page.goto(`${SITE_ORIGIN}/`, { waitUntil: "networkidle" });
      await page.locator('[data-consent="voorkeuren"]').click();
      await page.locator("[data-consent-stat]").check({ force: true });
      assert.equal(await page.locator("[data-consent-ads]").isChecked(), false);
      await page.locator('[data-consent="opslaan"]').click();
      await page.waitForTimeout(300);

      const dl = await getDataLayer();
      const upd = dl.find((e) => e[0] === "consent" && e[1] === "update");
      assert.deepEqual(upd[2], { analytics_storage: "granted", ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied" });
      assert(networkLog.some((r) => r.type === "gtag_script" && r.url.includes("G-HR6L1S8V7P")));
      assert(networkLog.some((r) => r.type === "ga_collect"));
      assert.equal(networkLog.some((r) => r.type === "gads"), false, "Analytics-only must send 0 Google Ads requests");

      const cks = (await getTrackingCookies()).map((c) => c.name);
      assert(cks.includes("_ga") && cks.includes("_ga_HR6L1S8V7P") && cks.includes("_gid"));
      assert(!cks.some((n) => n.startsWith("_gcl_") || n.startsWith("_gac_")), "Analytics-only must set 0 Ads cookies");

      // Conversion clicks: GA4 events fire, NO conversion_event_contact
      await page.locator('a[data-track="bellen"]').first().click();
      await page.locator('a[data-track="whatsapp"]').first().click();
      await page.waitForTimeout(150);
      const dl2 = await getDataLayer();
      assert(dl2.some((e) => e[0] === "event" && e[1] === "klik_bellen"));
      assert(dl2.some((e) => e[0] === "event" && e[1] === "klik_whatsapp"));
      assert.equal(dl2.some((e) => e[0] === "event" && e[1] === "conversion_event_contact"), false, "No Ads conversion event on Analytics-only");
      assert.equal(networkLog.some((r) => r.type === "gads"), false);

      // Reload check
      networkLog.length = 0;
      await page.reload({ waitUntil: "networkidle" });
      assert(networkLog.some((r) => r.type === "gtag_script" && r.url.includes("G-HR6L1S8V7P")));
      assert.equal(networkLog.some((r) => r.type === "gads"), false);
      assert.equal(googleRequests().length > 0, true);
      assert.equal(pageErrors.length, 0);
      await context.close();
      console.log("PASS [Chromium] 3. Analytics-only");
    }

    // 4. Ads-only + Conversion tests (Call, WhatsApp, Quote Form, Wizard) without duplicates
    {
      const { context, page, networkLog, getDataLayer, getTrackingCookies, pageErrors } = await setupContext(browser);
      await page.goto(`${SITE_ORIGIN}/`, { waitUntil: "networkidle" });
      await page.locator('[data-consent="voorkeuren"]').click();
      await page.locator("[data-consent-ads]").check({ force: true });
      assert.equal(await page.locator("[data-consent-stat]").isChecked(), false);
      await page.locator('[data-consent="opslaan"]').click();
      await page.waitForTimeout(300);

      const dl = await getDataLayer();
      const upd = dl.find((e) => e[0] === "consent" && e[1] === "update");
      assert.deepEqual(upd[2], { analytics_storage: "denied", ad_storage: "granted", ad_user_data: "granted", ad_personalization: "denied" });
      assert(networkLog.some((r) => r.type === "gtag_script" && r.url.includes("AW-7124503256")), "Ads-only loads AW container");
      assert(networkLog.some((r) => r.type === "gads"));
      assert.equal(networkLog.some((r) => r.type === "ga_collect"), false, "Ads-only must send 0 GA4 collect requests");

      const cks = (await getTrackingCookies()).map((c) => c.name);
      assert(cks.includes("_gcl_au") && cks.includes("_gcl_aw") && cks.includes("_gac_gb_12345"));
      assert(!cks.some((n) => n === "_ga" || n === "_gid"), "Ads-only must set 0 GA4 cookies");

      // Test call + WhatsApp clicks -> exactly 1 conversion_event_contact per click, 0 GA4 events
      await page.locator('a[data-track="bellen"]').first().click();
      await page.locator('a[data-track="whatsapp"]').first().click();
      await page.waitForTimeout(150);
      let dlEvents = (await getDataLayer()).filter((e) => e[0] === "event");
      assert.equal(dlEvents.filter((e) => e[1] === "conversion_event_contact").length, 2);
      assert.equal(dlEvents.some((e) => e[1] === "klik_bellen" || e[1] === "klik_whatsapp"), false);
      assert.equal(networkLog.some((r) => r.type === "ga_collect"), false);

      // Navigate to /offerte/ and test both quote form submit & wizard WhatsApp without duplicates
      await page.goto(`${SITE_ORIGIN}/offerte/`, { waitUntil: "networkidle" });
      // Step 1 -> Step 2 (fill required message) -> Step 3
      await page.locator("#wizardStep1Next").click();
      await page.locator('#quoteForm textarea[name="message"]').fill("Groepenkast vervangen");
      await page.locator('[data-step="2"] [data-wizard-next]').click();
      await page.locator('#quoteForm input[name="name"]').fill("Jan Jansen");
      await page.locator('#quoteForm input[name="phone"]').fill("0612345678");
      await page.locator('#quoteForm input[name="email"]').fill("jan@example.nl");
      await page.locator('#quoteForm input[name="akkoord"]').check();

      // Wizard WhatsApp button (step 3)
      await page.locator("#btnSendWhatsApp").click();
      await page.waitForTimeout(150);
      dlEvents = (await getDataLayer()).filter((e) => e[0] === "event");
      assert.equal(dlEvents.filter((e) => e[1] === "conversion_event_contact").length, 1, "Wizard WhatsApp emits exactly 1 conversion");
      assert.equal(dlEvents.some((e) => e[1] === "generate_lead"), false, "Ads-only emits 0 GA4 generate_lead");

      // Submit quote form via #btnSendEmail
      await page.locator("#btnSendEmail").click();
      await page.waitForSelector(".form-result", { state: "visible" });
      dlEvents = (await getDataLayer()).filter((e) => e[0] === "event");
      assert.equal(dlEvents.filter((e) => e[1] === "conversion_event_contact").length, 2, "Quote submit emits exactly 1 more conversion (total 2 on /offerte/)");
      assert.equal(networkLog.some((r) => r.type === "ga_collect"), false, "Still 0 GA4 requests on Ads-only");
      assert.equal(pageErrors.length, 0);
      await context.close();
      console.log("PASS [Chromium] 4. Ads-only + Conversion tracking (no duplicates)");
    }

    // 5. Accept All + Conversion tests (no duplicates) + Withdraw Consent + Cookie deletion
    {
      const { context, page, networkLog, googleRequests, getDataLayer, getTrackingCookies, pageErrors } = await setupContext(browser);
      await page.goto(`${SITE_ORIGIN}/`, { waitUntil: "networkidle" });
      await page.locator('[data-consent="ja"]').click();
      await page.waitForTimeout(300);

      const dl = await getDataLayer();
      const upd = dl.find((e) => e[0] === "consent" && e[1] === "update");
      // CRITICAL Point 1 check: ad_personalization MUST remain 'denied'!
      assert.deepEqual(upd[2], { analytics_storage: "granted", ad_storage: "granted", ad_user_data: "granted", ad_personalization: "denied" });
      assert((await getTrackingCookies()).length >= 6, "Both GA4 and Ads cookies set on Accept All");

      // Check 1 call click + 1 WhatsApp click = 2 conversions (no duplicates)
      await page.locator('a[data-track="bellen"]').first().click();
      await page.locator('a[data-track="whatsapp"]').first().click();
      await page.waitForTimeout(150);
      const eventsHome = (await getDataLayer()).filter((e) => e[0] === "event");
      assert.equal(eventsHome.filter((e) => e[1] === "klik_bellen").length, 1);
      assert.equal(eventsHome.filter((e) => e[1] === "klik_whatsapp").length, 1);
      assert.equal(eventsHome.filter((e) => e[1] === "conversion_event_contact").length, 2);

      // Withdraw consent via footer link -> Alleen noodzakelijk -> reload
      networkLog.length = 0;
      await Promise.all([
        page.waitForNavigation({ waitUntil: "networkidle" }),
        (async () => {
          await page.locator("[data-cookie-instellingen]").first().click();
          await page.locator('[data-consent="nee"]').click();
        })(),
      ]);

      // Verify tracking cookies deleted in Chromium & 0 Google requests on reloaded page
      const remainingCookies = await getTrackingCookies();
      assert.equal(remainingCookies.length, 0, "All tracking cookies deleted after withdrawal: " + JSON.stringify(remainingCookies));
      assert.equal(googleRequests().length, 0, "After withdrawal + reload: 0 Google requests");
      const dlReload = await getDataLayer();
      assert.deepEqual(dlReload[0], [
        "consent",
        "default",
        { analytics_storage: "denied", ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", wait_for_update: 500 },
      ]);
      await page.locator('a[data-track="bellen"]').first().click();
      assert.equal(googleRequests().length, 0, "After withdrawal: clicks send 0 Google requests");
      assert.equal(pageErrors.length, 0);
      await context.close();
      console.log("PASS [Chromium] 5. Accept All (ad_personalization=denied) + Withdraw Consent");
    }

    // 6. Expired Consent + Privacy Policy Tables + Core UI Smoke Check
    {
      const { context, page, googleRequests, getDataLayer, pageErrors } = await setupContext(browser, { viewport: { width: 390, height: 844 } });
      await page.goto(`${SITE_ORIGIN}/`, { waitUntil: "networkidle" });
      await page.evaluate(() => {
        localStorage.setItem("ino_cookies", JSON.stringify({ stat: true, ads: true }));
        localStorage.setItem("ino_cookies_datum", String(Date.now() - 366 * 864e5));
      });
      await page.reload({ waitUntil: "networkidle" });
      assert.equal(googleRequests().length, 0, "Expired consent: 0 Google requests");
      assert.equal(await page.locator(".consent").isVisible(), true, "Expired consent re-opens banner");
      assert.equal(await page.locator("[data-consent-stat]").isChecked(), false);
      assert.equal(await page.locator("[data-consent-ads]").isChecked(), false);
      assert.equal(await page.evaluate(() => localStorage.getItem("ino_cookies")), null);

      // Mobile menu + FAQ + Privacy table checks
      await page.locator('[data-consent="nee"]').click();
      await page.locator("#menuBtn").click();
      assert.equal(await page.locator("#nav").evaluate((el) => el.classList.contains("open")), true, "Mobile menu opens");

      await page.goto(`${SITE_ORIGIN}/privacy/`, { waitUntil: "networkidle" });
      const nlTable = await page.locator(".responstijd-table").innerText();
      for (const k of ["ino_cookies", "ino_cookies_datum", "ino_thema", "inoReviews", "_ga", "_gcl_au", "_gcl_aw", "Cloudflare Turnstile"]) {
        assert(nlTable.includes(k), "NL privacy table missing: " + k);
      }

      await page.goto(`${SITE_ORIGIN}/en/privacy/`, { waitUntil: "networkidle" });
      const enTable = await page.locator(".responstijd-table").innerText();
      for (const k of ["ino_cookies", "ino_cookies_datum", "ino_thema", "inoReviews", "_ga", "_gcl_au", "_gcl_aw", "Cloudflare Turnstile"]) {
        assert(enTable.includes(k), "EN privacy table missing: " + k);
      }

      assert.equal(pageErrors.length, 0, "Zero JS errors on mobile smoke check");
      await context.close();
      console.log("PASS [Chromium] 6. Expired Consent + Privacy Tables + UI Smoke");
    }
  } finally {
    await browser.close();
  }
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
