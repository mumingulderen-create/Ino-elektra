/* INO Elektra – script.js (v2)
   Klein, zonder frameworks. Wordt met `defer` geladen, blokkeert de pagina dus niet. */
(function () {
  "use strict";

  // Oude .html-URL's netjes maken in de adresbalk
  var p = location.pathname;
  if (/(\/index)?\.html$/.test(p)) {
    var clean = p.replace(/\/index\.html$/, "/").replace(/\.html$/, "") || "/";
    history.replaceState(null, "", clean + location.search + location.hash);
  }

  // Mobiel menu
  var btn = document.getElementById("menuBtn"), nav = document.getElementById("nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.setAttribute("aria-label", open ? "Menu sluiten" : "Menu openen");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); btn.focus(); }
    });
  }

  // FAQ-accordeon (toegankelijk). Het +/− teken staat altijd in het LAATSTE <span>.
  document.querySelectorAll(".faq-q").forEach(function (q, i) {
    var a = q.nextElementSibling;
    if (!a) return;
    var id = a.id || "faq-a-" + i;
    a.id = id;
    q.setAttribute("aria-controls", id);
    q.setAttribute("aria-expanded", "false");
    if (!q.getAttribute("type")) q.setAttribute("type", "button");
    q.addEventListener("click", function () {
      var open = a.classList.toggle("open");
      q.setAttribute("aria-expanded", open ? "true" : "false");
      var spans = q.querySelectorAll("span");
      var icon = spans[spans.length - 1];
      if (icon && spans.length) icon.textContent = open ? "−" : "+";
    });
  });

  // Kaart vergroten (werkgebied)
  var mb = document.getElementById("mapEnlargeBtn"), mm = document.getElementById("mapModal"), mc = document.getElementById("mapModalClose");
  if (mb && mm) {
    var close = function () { mm.classList.remove("open"); mb.focus(); };
    mb.addEventListener("click", function () { mm.classList.add("open"); if (mc) mc.focus(); });
    if (mc) mc.addEventListener("click", close);
    mm.addEventListener("click", function (e) { if (e.target === mm) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && mm.classList.contains("open")) close(); });
  }

  // Foto-upload: toon gekozen bestanden
  var photos = document.getElementById("photos"), list = document.getElementById("photoList");
  if (photos && list) photos.addEventListener("change", function () {
    var f = Array.prototype.slice.call(photos.files);
    list.textContent = f.length ? f.length + " bestand(en): " + f.map(function (x) { return x.name; }).join(", ") : "";
  });

  var d = document.getElementById("date");
  if (d) d.min = new Date().toISOString().split("T")[0];

  // Google Reviews Carrousel Navigatie (Native 60fps Scroll)
  var rTrack = document.getElementById("reviewsTrack");
  var rPrev = document.getElementById("reviewsPrevBtn");
  var rNext = document.getElementById("reviewsNextBtn");
  if (rTrack && rPrev && rNext) {
    rPrev.addEventListener("click", function () {
      var step = rTrack.firstElementChild ? rTrack.firstElementChild.offsetWidth + 20 : 340;
      rTrack.scrollBy({ left: -step, behavior: "smooth" });
    });
    rNext.addEventListener("click", function () {
      var step = rTrack.firstElementChild ? rTrack.firstElementChild.offsetWidth + 20 : 340;
      rTrack.scrollBy({ left: step, behavior: "smooth" });
    });
  }

  function esc(v) { return String(v).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" }[c]; }); }

  // Formulieren via FormSubmit (AJAX) met honeypot tegen spam
  function wire(form, okMsg) {
    if (!form) return;
    if (!form.querySelector('[name="_honey"]')) {
      var hp = document.createElement("input");
      hp.type = "text"; hp.name = "_honey"; hp.tabIndex = -1; hp.autocomplete = "off"; hp.className = "hp"; hp.setAttribute("aria-hidden", "true");
      form.appendChild(hp);
    }
    var submit = form.querySelector("button[type='submit']");
    var label = submit ? submit.textContent : "Versturen";
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = new FormData(form);
      if (data.get("_honey")) return;
      var result = form.querySelector(".form-result") || document.getElementById("formResult");
      if (submit) { submit.disabled = true; submit.textContent = "Versturen…"; }
      fetch("https://formsubmit.co/ajax/d0d9de6bb2a30083d92c3fe4775b9ce6", { method: "POST", body: data, headers: { Accept: "application/json" } })
        .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
        .then(function () {
          track("formulier_verstuurd", { formulier: form.id || "form" });
          track("generate_lead", { formulier: form.id || "form", currency: "EUR" });
          if (result) {
            result.hidden = false; result.className = "form-result";
            result.innerHTML = "<strong>Aanvraag verstuurd.</strong><br>Bedankt " + esc(data.get("name") || "") + ", " + okMsg;
            result.scrollIntoView({ behavior: "smooth", block: "center" });
          } else { alert("Verstuurd. " + okMsg); }
          form.reset();
          if (list) list.textContent = "";
        })
        .catch(function () {
          var msg = "<strong>Versturen lukte niet.</strong><br>Bel ons direct op <a href=\"tel:+31628763775\">06 28 76 37 75</a> of probeer het opnieuw.";
          if (result) { result.hidden = false; result.className = "form-result form-result-error"; result.innerHTML = msg; }
          else alert("Versturen lukte niet. Bel ons op 06 28 76 37 75.");
        })
        .finally(function () { if (submit) { submit.disabled = false; submit.textContent = label; } });
    });
  }
  wire(document.getElementById("quoteForm"), "we nemen zo snel mogelijk contact met je op.");
  wire(document.getElementById("spoedForm"), "we bellen je zo snel mogelijk terug.");
  wire(document.getElementById("appointmentForm"), "we bevestigen de afspraak persoonlijk.");

  // ?wijk=... voorinvullen op offerte
  var wijk = new URLSearchParams(location.search).get("wijk");
  if (wijk) {
    var ta = document.querySelector("#quoteForm textarea[name='message']");
    var naam = wijk.replace(/-/g, " ").replace(/\b\w/g, function (c) { return c.toUpperCase(); });
    if (ta && !ta.value) ta.value = "Klus in " + naam + ":\n\n";
    var hid = document.createElement("input");
    hid.type = "hidden"; hid.name = "wijk"; hid.value = naam;
    var qf = document.getElementById("quoteForm"); if (qf) qf.appendChild(hid);
  }

  // Interactieve Groepenkast & Inductie Calculator
  function initCalculator() {
    var deviceInputs = document.querySelectorAll("input[name='calc_device']");
    var huidigInputs = document.querySelectorAll("input[name='calc_huidig']");
    var aansluitingInputs = document.querySelectorAll("input[name='calc_aansluiting']");
    var elGroepen = document.getElementById("calcGroepen");
    var elFase = document.getElementById("calcFase");
    var elTitel = document.getElementById("calcTitel");
    var elUitleg = document.getElementById("calcUitleg");
    var elPrijs = document.getElementById("calcPrijs");
    var elOfferte = document.getElementById("calcOfferteBtn");
    var elWa = document.getElementById("calcWaBtn");
    var elBreakdown = document.getElementById("calcBreakdown");
    var elStedinBox = document.getElementById("calcStedinBox");

    if (!deviceInputs.length || !elGroepen) return;

    function bereken() {
      var groepen = 0;
      var hasLaadpaal = false;
      var hasWarmtepomp = false;
      var hasInductie = false;
      var hasPV = false;
      var hasQuooker = false;

      deviceInputs.forEach(function (inp) {
        if (inp.checked) {
          var val = inp.value;
          var g = parseInt(inp.getAttribute("data-groepen") || "1", 10);
          groepen += g;
          if (val === "laadpaal") hasLaadpaal = true;
          if (val === "warmtepomp") hasWarmtepomp = true;
          if (val === "inductie") hasInductie = true;
          if (val === "zonnepanelen") hasPV = true;
          if (val === "quooker") hasQuooker = true;
        }
      });

      // Minimum 4 basisgroepen
      if (groepen < 4) groepen = 4;

      var currentAansluiting = "1fase";
      aansluitingInputs.forEach(function (r) {
        if (r.checked) currentAansluiting = r.value;
      });

      // Fase advies bepalen
      var advise3Fase = false;
      if (currentAansluiting === "3fase") {
        advise3Fase = true;
      } else if (hasLaadpaal || hasWarmtepomp) {
        advise3Fase = true;
      } else if (hasInductie && groepen >= 7) {
        advise3Fase = true;
      } else if (groepen > 8) {
        advise3Fase = true;
      }

      // Prijsberekening en transparante specificatie
      var breakdownItems = [];
      var basisPrijs = 640; // 1-fase basiskast met 2 aardlekschakelaars en tot 8 groepen (incl. klein materiaal en kamrails)
      breakdownItems.push({ naam: "Basiskast 1-fase (tot 8 gr.)", prijs: "€ 640,-" });

      var extraKosten = 0;

      if (advise3Fase) {
        extraKosten += 120;
        breakdownItems.push({ naam: "3-fase uitvoering & kamrail voorbereiding", prijs: "+ € 120,-" });
      }

      if (hasInductie) {
        extraKosten += 85;
        breakdownItems.push({ naam: "Inductie kookgroep (incl. kamrail & aansluiting)", prijs: "+ € 85,-" });
      }

      if (hasLaadpaal) {
        var laadKosten = advise3Fase ? 185 : 85;
        extraKosten += laadKosten;
        breakdownItems.push({ 
          naam: advise3Fase ? "Laadpaal (4P aardlekautomaat B16 + kracht kamrail)" : "Laadpaal (2P aardlekautomaat)", 
          prijs: "+ € " + laadKosten + ",-" 
        });
      }

      if (hasWarmtepomp) {
        var wpKosten = advise3Fase ? 185 : 85;
        extraKosten += wpKosten;
        breakdownItems.push({ 
          naam: advise3Fase ? "Warmtepomp (4P aardlekautomaat + kracht kamrail)" : "Warmtepomp (2P aardlekautomaat)", 
          prijs: "+ € " + wpKosten + ",-" 
        });
      }

      if (hasPV) {
        extraKosten += 95;
        breakdownItems.push({ naam: "Zonnepanelen (PV-aardlekautomaat & afzekering)", prijs: "+ € 95,-" });
      }

      if (hasQuooker) {
        extraKosten += 45;
        breakdownItems.push({ naam: "Quooker/boiler (aparte groep + kamrail)", prijs: "+ € 45,-" });
      }

      var extraGroepenBovenAcht = Math.max(0, groepen - 8);
      if (extraGroepenBovenAcht > 0) {
        var extraGrKosten = extraGroepenBovenAcht * 45;
        extraKosten += extraGrKosten;
        breakdownItems.push({ 
          naam: extraGroepenBovenAcht + "x Extra groep (" + extraGroepenBovenAcht + "× € 45)", 
          prijs: "+ € " + extraGrKosten + ",-" 
        });
      }

      var totaalPrijs = basisPrijs + extraKosten;

      // Update UI
      elGroepen.textContent = groepen + " groepen";
      elFase.textContent = advise3Fase ? "3-fase (400V)" : "1-fase (230V)";

      if (advise3Fase) {
        elTitel.textContent = "Aanbevolen: 3-fase Hager of ABB Groepenkast";
        if (hasLaadpaal || hasWarmtepomp) {
          elUitleg.textContent = "Door zware verbruikers (zoals je laadpaal of warmtepomp) is een 3-fase aansluiting noodzakelijk om veilig en op vol vermogen te draaien.";
        } else if (hasInductie) {
          elUitleg.textContent = "Met koken op inductie en meerdere keukenapparaten biedt 3-fase een optimale verdeling over de fasen zonder dat de hoofdzekering overbelast raakt.";
        } else {
          elUitleg.textContent = "Bij meer dan 8 groepen adviseren we conform NEN 1010 een 3-fase verdeelkast voor een evenwichtige stroomverdeling over de woning.";
        }
      } else {
        elTitel.textContent = "Aanbevolen: 1-fase Hager of ABB Groepenkast";
        elUitleg.textContent = "Ideaal voor jouw appartement of standaard eengezinswoning met 2 aardlekschakelaars en NEN 1010 opleveringskeuring.";
      }

      // Stedin toelichting tonen of verbergen
      if (elStedinBox) {
        if (advise3Fase && currentAansluiting !== "3fase") {
          elStedinBox.style.display = "block";
        } else {
          elStedinBox.style.display = "none";
        }
      }

      // Prijsopbouw bijwerken
      if (elBreakdown) {
        var bHtml = "";
        breakdownItems.forEach(function (it) {
          bHtml += '<li class="calc-breakdown-item"><span>' + it.naam + '</span><span>' + it.prijs + '</span></li>';
        });
        elBreakdown.innerHTML = bHtml;
      }

      elPrijs.innerHTML = "€ " + totaalPrijs + ",- <span>all-in</span>";

      // Dynamische links
      var params = "?groepen=" + groepen + "&fase=" + (advise3Fase ? "3-fase" : "1-fase") + "&prijs=" + totaalPrijs;
      if (elOfferte) elOfferte.href = "/offerte/" + params;

      if (elWa) {
        var msg = "Hallo INO, via de online calculator kom ik uit op een " +
                  (advise3Fase ? "3-fase" : "1-fase") + " groepenkast met " + groepen +
                  " groepen (berekende all-in indicatie € " + totaalPrijs + "). " +
                  (advise3Fase && currentAansluiting !== "3fase" ? "Ik wil graag advies over Stedin verzwaring en het voorbereiden van de kast. " : "") +
                  "Hierbij stuur ik een foto van mijn huidige meterkast mee voor een bindende offerte.";
        elWa.href = "https://wa.me/31628763775?text=" + encodeURIComponent(msg);
      }
    }

    deviceInputs.forEach(function (inp) { 
      inp.addEventListener("change", bereken); 
      inp.addEventListener("input", bereken); 
      inp.addEventListener("click", bereken); 
    });
    huidigInputs.forEach(function (inp) { 
      inp.addEventListener("change", bereken); 
      inp.addEventListener("click", bereken); 
    });
    aansluitingInputs.forEach(function (inp) { 
      inp.addEventListener("change", bereken); 
      inp.addEventListener("click", bereken); 
    });
    bereken();
  }
  initCalculator();

  // Stedin of INO storingscheck
  function initStedinChecker() {
    var checker = document.getElementById("stedinChecker");
    if (!checker) return;
    var steps = checker.querySelectorAll(".check-step");
    var results = checker.querySelectorAll(".check-result");

    function reset() {
      results.forEach(function (r) { r.hidden = true; });
      steps.forEach(function (s) { s.hidden = s.dataset.step !== "1"; });
    }

    checker.addEventListener("click", function (e) {
      var nextBtn = e.target.closest("[data-next]");
      var backBtn = e.target.closest("[data-back]");
      var resultBtn = e.target.closest("[data-result]");
      var resetBtn = e.target.closest(".reset-link") || e.target.closest(".reset-check");

      if (nextBtn) {
        steps.forEach(function (s) { s.hidden = s.dataset.step !== nextBtn.dataset.next; });
      } else if (backBtn) {
        results.forEach(function (r) { r.hidden = true; });
        steps.forEach(function (s) { s.hidden = s.dataset.step !== backBtn.dataset.back; });
      } else if (resultBtn) {
        steps.forEach(function (s) { s.hidden = true; });
        results.forEach(function (r) { r.hidden = r.dataset.resultId !== resultBtn.dataset.result; });
      } else if (resetBtn) {
        reset();
      }
    });
  }
  initStedinChecker();

  // Klik- en conversiemeting (bellen / WhatsApp / formulieren).
  // Werkt automatisch en naadloos met Google Analytics 4 (GA4) en Google Ads.
  function track(evt, params) {
    try {
      if (window.gtag) window.gtag("event", evt, params || {});
      (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: evt }, params || {}));
    } catch (e) {}
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a");
    if (!a) return;
    var href = a.getAttribute("href") || "";
    var isTel = href.indexOf("tel:") === 0 || a.getAttribute("data-track") === "bellen";
    var isWa = href.indexOf("wa.me") !== -1 || a.getAttribute("data-track") === "whatsapp";

    if (isTel) {
      track("klik_bellen", { pagina: location.pathname });
      track("contact", { method: "phone", pagina: location.pathname });
    } else if (isWa) {
      track("klik_whatsapp", { pagina: location.pathname });
      track("contact", { method: "whatsapp", pagina: location.pathname });
    }
  });

  // Slimme, pagina-specifieke WhatsApp links (voor-ingevulde berichten)
  function initSmartWhatsApp() {
    var p = (location.pathname || "").toLowerCase();
    var msg = "Hallo INO Techniek, ik heb een vraag over een elektra klus in Utrecht. Kan ik een foto sturen voor advies?";
    if (p.indexOf("extra-groep") !== -1) {
      msg = "Hallo INO, ik wil graag een extra groep laten plaatsen in mijn meterkast in Utrecht. Hierbij stuur ik een foto van mijn huidige kast mee.";
    } else if (p.indexOf("groepenkast") !== -1) {
      msg = "Hallo INO, ik wil graag advies of een offerte voor het vervangen/uitbreiden van mijn groepenkast. Hierbij stuur ik een foto van mijn huidige meterkast mee.";
    } else if (p.indexOf("perilex") !== -1) {
      msg = "Hallo INO, ik wil een inductiekookplaat of Perilex aansluiting laten aanleggen. Hierbij een foto van mijn situatie.";
    } else if (p.indexOf("laadpaal") !== -1) {
      msg = "Hallo INO, ik wil graag een laadpaal laten installeren aan huis. Wat zijn de mogelijkheden en kosten?";
    } else if (p.indexOf("krachtstroom") !== -1) {
      msg = "Hallo INO, ik heb krachtstroom (3-fase) nodig in mijn woning of bedrijfspand. Graag ontvang ik advies en een richtprijs.";
    } else if (p.indexOf("spoed") !== -1 || p.indexOf("storing") !== -1 || p.indexOf("kortsluiting") !== -1 || p.indexOf("aardlek") !== -1) {
      msg = "Hallo INO, ik heb met spoed een elektricien nodig in Utrecht in verband met een storing. Hierbij een foto van de meterkast.";
    } else if (p.indexOf("frezen") !== -1 || p.indexOf("stopcontact") !== -1) {
      msg = "Hallo INO, ik wil graag stopcontacten laten verplaatsen/infrezen. Kan ik foto's sturen voor een richtprijs?";
    } else if (p.indexOf("tuinverlichting") !== -1) {
      msg = "Hallo INO, ik wil graag tuinverlichting of buitenelektra laten aanleggen. Wat zijn de mogelijkheden?";
    } else if (p.indexOf("tarieven") !== -1) {
      msg = "Hallo INO, ik heb gekeken naar jullie transparante tarieven en wil graag een indicatie voor mijn klus. Hierbij een foto.";
    } else if (p.indexOf("elektricien-") !== -1) {
      var h1 = document.querySelector("h1");
      var title = h1 ? h1.textContent.trim() : "de regio Utrecht";
      msg = "Hallo INO Techniek, ik zoek een betrouwbare elektricien voor een klus (" + title + "). Hierbij stuur ik foto's van de situatie mee.";
    }

    var waHref = "https://wa.me/31628763775?text=" + encodeURIComponent(msg);

    // Update floating WhatsApp widget en mobiele WhatsApp-knop
    var floatingBtn = document.getElementById("floatingWa");
    if (floatingBtn) floatingBtn.href = waHref;

    document.querySelectorAll(".mobile-btn-whatsapp, .m-btn-whatsapp").forEach(function (btn) {
      btn.href = waHref;
    });
  }
  initSmartWhatsApp();

  // Interactieve Klus-Wizard op offerte-pagina
  function initKlusWizard() {
    var wizard = document.getElementById("quoteWizard");
    if (!wizard) return;

    var currentStep = 1;
    var totalSteps = 3;
    var serviceInput = document.getElementById("wizardService");
    var termijnInput = document.getElementById("wizardTermijn");
    var messageBox = document.getElementById("message");
    var progressBar = document.getElementById("wizardProgressBar");
    var stepIndicators = wizard.querySelectorAll(".wizard-progress-step");
    var stepContents = wizard.querySelectorAll(".wizard-step-content");
    var tiles = wizard.querySelectorAll(".wizard-tile");
    var pills = wizard.querySelectorAll(".wizard-pill");
    var dropzone = document.getElementById("wizardDropzone");
    var photoInput = document.getElementById("photos");
    var photoList = document.getElementById("photoList");

    function goToStep(step) {
      if (step < 1 || step > totalSteps) return;
      currentStep = step;

      // Update progress bar
      if (progressBar) {
        var pct = step === 1 ? 0 : step === 2 ? 50 : 100;
        progressBar.style.width = pct + "%";
      }

      // Update step circles & labels
      stepIndicators.forEach(function (ind) {
        var s = parseInt(ind.dataset.step, 10);
        ind.classList.remove("active", "completed");
        if (s === currentStep) {
          ind.classList.add("active");
        } else if (s < currentStep) {
          ind.classList.add("completed");
        }
      });

      // Show/hide step contents
      stepContents.forEach(function (content) {
        var s = parseInt(content.dataset.step, 10);
        if (s === currentStep) {
          content.hidden = false;
        } else {
          content.hidden = true;
        }
      });

      // Smooth scroll into view
      wizard.scrollIntoView({ behavior: "smooth", block: "start" });
    }

    var countBadge = document.getElementById("wizardStep1Count");
    var step1NextBtn = document.getElementById("wizardStep1Next");

    function getSelectedServices() {
      var arr = [];
      wizard.querySelectorAll(".wizard-tile.selected").forEach(function (t) {
        if (t.dataset.service) arr.push(t.dataset.service);
      });
      return arr;
    }

    function updateSelectionUI() {
      var sel = getSelectedServices();
      var count = sel.length;
      if (serviceInput) serviceInput.value = sel.join(", ");

      if (countBadge) {
        if (count === 0) {
          countBadge.textContent = "Kies minimaal 1 klus";
          countBadge.style.color = "#b91c1c";
          countBadge.style.background = "#fee2e2";
        } else if (count === 1) {
          countBadge.textContent = "1 klus geselecteerd";
          countBadge.style.color = "var(--green-dark)";
          countBadge.style.background = "#eef8ec";
        } else {
          countBadge.textContent = count + " klussen gecombineerd";
          countBadge.style.color = "var(--green-dark)";
          countBadge.style.background = "#eef8ec";
        }
      }

      if (step1NextBtn) {
        if (count > 1) {
          step1NextBtn.innerHTML = "Volgende: Toelichting (" + count + " klussen) →";
        } else {
          step1NextBtn.innerHTML = "Volgende: Toelichting &amp; Foto's →";
        }
      }

      // Dynamic placeholder for message textarea
      if (messageBox) {
        if (count === 0) {
          messageBox.placeholder = "Beschrijf kort je situatie en wat er moet gebeuren...";
        } else if (count === 1) {
          var s = sel[0];
          if (s.indexOf("Meterkast") !== -1) {
            messageBox.placeholder = "Bijv: Mijn groepenkast is verouderd met stoppen. Ik wil graag een nieuwe 1- of 3-fase kast met aardlekschakelaars.";
          } else if (s.indexOf("Extra groep") !== -1) {
            messageBox.placeholder = "Bijv: Ik krijg een Quooker en combi-oven en wil 1 of 2 extra groepen laten bijplaatsen.";
          } else if (s.indexOf("Kookgroep") !== -1 || s.indexOf("Perilex") !== -1) {
            messageBox.placeholder = "Bijv: We gaan koken op inductie. Er ligt nog geen Perilex stopcontact / kookgroep.";
          } else if (s.indexOf("Laadpaal") !== -1) {
            messageBox.placeholder = "Bijv: Ik wil een 11kW Wallbox laten monteren bij de oprit, incl. load balancing.";
          } else {
            messageBox.placeholder = "Beschrijf kort wat er moet gebeuren voor " + s + "...";
          }
        } else {
          messageBox.placeholder = "Licht de situatie kort toe voor: " + sel.join(" + ") + "...";
        }
      }
    }

    // Tile multi-selection (Step 1)
    tiles.forEach(function (tile) {
      tile.addEventListener("click", function () {
        tile.classList.toggle("selected");
        updateSelectionUI();
      });
    });
    updateSelectionUI();

    // Pill selection (termijn in Step 2)
    pills.forEach(function (pill) {
      pill.addEventListener("click", function () {
        pills.forEach(function (p) { p.classList.remove("selected"); });
        pill.classList.add("selected");
        if (termijnInput) termijnInput.value = pill.dataset.val || pill.textContent.trim();
      });
    });

    // Next / Previous buttons
    wizard.addEventListener("click", function (e) {
      var nextBtn = e.target.closest("[data-wizard-next]");
      var prevBtn = e.target.closest("[data-wizard-prev]");

      if (nextBtn) {
        e.preventDefault();
        if (currentStep === 1) {
          var sel = getSelectedServices();
          if (sel.length === 0) {
            if (countBadge) {
              countBadge.textContent = "Kies minimaal 1 optie om door te gaan!";
              countBadge.style.color = "#b91c1c";
              countBadge.style.background = "#fee2e2";
            }
            tiles.forEach(function (t) {
              t.style.borderColor = "#e53e3e";
              setTimeout(function () { t.style.borderColor = ""; }, 1500);
            });
            return;
          }
          goToStep(2);
        } else if (currentStep === 2) {
          // Check if message is filled
          if (messageBox && !messageBox.value.trim()) {
            messageBox.focus();
            messageBox.style.borderColor = "#e53e3e";
            setTimeout(function () { messageBox.style.borderColor = ""; }, 2500);
            return;
          }
          goToStep(3);
        }
      } else if (prevBtn) {
        e.preventDefault();
        goToStep(currentStep - 1);
      }
    });

    // Dropzone drag-and-drop
    if (dropzone && photoInput) {
      ["dragenter", "dragover"].forEach(function (ename) {
        dropzone.addEventListener(ename, function (e) {
          e.preventDefault();
          dropzone.classList.add("dragover");
        });
      });
      ["dragleave", "drop"].forEach(function (ename) {
        dropzone.addEventListener(ename, function (e) {
          e.preventDefault();
          dropzone.classList.remove("dragover");
        });
      });
      dropzone.addEventListener("drop", function (e) {
        if (e.dataTransfer && e.dataTransfer.files) {
          photoInput.files = e.dataTransfer.files;
          updatePhotoDisplay();
        }
      });
      photoInput.addEventListener("change", updatePhotoDisplay);
    }

    function updatePhotoDisplay() {
      if (!photoInput || !photoList) return;
      var f = Array.prototype.slice.call(photoInput.files || []);
      if (!f.length) {
        photoList.innerHTML = "";
        return;
      }
      var html = '<div style="margin-top:10px;display:flex;flex-wrap:wrap;gap:8px;">';
      f.forEach(function (file) {
        html += '<span style="background:#eef8ec;color:#185315;padding:5px 12px;border-radius:8px;font-size:12px;font-weight:700;display:inline-flex;align-items:center;gap:6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/></svg> ' + esc(file.name) + '</span>';
      });
      html += '</div>';
      photoList.innerHTML = html;
    }

    // Direct versturen via WhatsApp knop in Stap 3
    var btnSendWhatsApp = document.getElementById("btnSendWhatsApp");
    if (btnSendWhatsApp) {
      btnSendWhatsApp.addEventListener("click", function (e) {
        e.preventDefault();
        var form = document.getElementById("quoteForm");
        var nameField = form ? form.querySelector("input[name='name']") : null;
        var phoneField = form ? form.querySelector("input[name='phone']") : null;
        var postcodeField = form ? form.querySelector("input[name='postcode']") : null;
        var numberField = form ? form.querySelector("input[name='number']") : null;

        var nameVal = (nameField && nameField.value || "").trim();
        var phoneVal = (phoneField && phoneField.value || "").trim();
        var postcodeVal = (postcodeField && postcodeField.value || "").trim();
        var numberVal = (numberField && numberField.value || "").trim();
        var servicesVal = (serviceInput && serviceInput.value || "").trim() || "Elektra klus";
        var termijnVal = (termijnInput && termijnInput.value || "").trim();
        var msgVal = (messageBox && messageBox.value || "").trim();

        if (!nameVal) {
          if (nameField) {
            nameField.focus();
            nameField.style.borderColor = "#e53e3e";
            setTimeout(function () { nameField.style.borderColor = ""; }, 2000);
          }
          return;
        }

        var lines = [
          "Hallo INO Techniek, ik heb via de offerte-wizard op de website een aanvraag samengesteld:",
          "- Klus(sen): " + servicesVal,
          "- Gewenste termijn: " + (termijnVal || "In overleg"),
          "- Toelichting: " + (msgVal || "(geen extra toelichting)"),
          "- Mijn naam: " + nameVal
        ];
        if (phoneVal) lines.push("- Tel: " + phoneVal);
        if (postcodeVal || numberVal) lines.push("- Adres/postcode: " + (postcodeVal + " " + numberVal).trim());
        lines.push("\nIk stuur hierbij ook direct foto's van mijn situatie mee voor een vaste prijsopgave!");

        var waUrl = "https://wa.me/31628763775?text=" + encodeURIComponent(lines.join("\n"));
        track("formulier_verstuurd", { formulier: "quoteForm", method: "whatsapp_wizard" });
        track("generate_lead", { formulier: "quoteForm", method: "whatsapp_wizard", currency: "EUR" });
        window.open(waUrl, "_blank", "noopener");
      });
    }
  }
  initKlusWizard();
})();
