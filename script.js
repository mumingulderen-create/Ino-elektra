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

  // Klik-meting (bellen / WhatsApp). Werkt automatisch zodra je Google Analytics 4
  // of Google Tag Manager toevoegt; zonder die tools doet dit niets.
  function track(evt, params) {
    try {
      if (window.gtag) window.gtag("event", evt, params || {});
      (window.dataLayer = window.dataLayer || []).push(Object.assign({ event: evt }, params || {}));
    } catch (e) {}
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("[data-track]");
    if (a) track(a.getAttribute("data-track") === "bellen" ? "klik_bellen" : "klik_whatsapp", { pagina: location.pathname });
  });
})();
