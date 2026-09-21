# generate_site_part3.py
from build_components import make_header, make_footer

PAGES_PART3 = {}

# 10. tarieven.html
PAGES_PART3["tarieven.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tarieven | INO Techniek en Installatie</title>
  <meta name="description" content="Transparante tarieven van INO: uurtarieven, gratis voorrijkosten in Utrecht en vaste prijzen voor groepenkast en perilex. Alles incl. 21% btw.">
  <meta property="og:title" content="Tarieven | INO Techniek en Installatie">
  <meta property="og:description" content="Transparante tarieven van INO: uurtarieven, gratis voorrijkosten in Utrecht en vaste prijzen voor groepenkast en perilex. Alles incl. 21% btw.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/tarieven.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("tarieven") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Tarieven</div>
      <h1>Duidelijk vooraf, geen verrassingen achteraf.</h1>
      <p>Alle bedragen zijn inclusief 21% btw. De definitieve prijs stemmen we altijd vooraf met je af na het zien van foto's of een schouw.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Hier zie je vooraf wat een klus kost: uurtarieven, voorrijkosten en de vaste prijzen voor meterkast en perilex. Zo kun je vergelijken voordat je contact opneemt.</span></div>
    </div>
  </section>

  <section class="section soft" id="prijzen">
    <div class="container">
      <div class="price-grid">
        <div class="price-card">
          <span class="price-card-badge">Binnen Utrecht € 0</span>
          <h3>Voorrijkosten</h3>
          <div class="price-amount">Gratis<span> in Utrecht</span></div>
          <p>Binnen Utrecht rekenen we € 0,- voorrijkosten. Buiten Utrecht geldt een vast kilometertarief van € 0,40 per km.</p>
        </div>
        <div class="price-card">
          <span class="price-card-badge">Kantooruren</span>
          <h3>Standaard uurtarief</h3>
          <div class="price-amount">€ 90<span>/u incl. btw</span></div>
          <p>Voor schouwen op locatie, reparaties en reguliere storingen tijdens kantoortijden (08:00 - 17:00).</p>
        </div>
        <div class="price-card highlight">
          <span class="price-card-badge" style="background:rgba(255,255,255,.15);color:#fff">24/7 Bereikbaar</span>
          <h3>Spoed & Storingsdienst</h3>
          <div class="price-amount">vanaf € 90<span>/u</span></div>
          <p>Overdag € 90/u · Buiten kantooruren € 120/u · Vanaf 22:00 en in het weekend € 145/u (incl. btw).</p>
        </div>
        <div class="price-card">
          <h3>Groepenkast 1-fase</h3>
          <div class="price-amount">vanaf € 620</div>
          <p>1 t/m 8 groepen inclusief A-merk kast, hoofdschakelaar, aardlekschakelaars en montage. <a href="groepenkast.html" class="mini-link">Bekijk pakketten →</a></p>
        </div>
        <div class="price-card">
          <h3>Groepenkast 3-fase</h3>
          <div class="price-amount">vanaf € 720</div>
          <p>1 t/m 8 groepen inclusief 3-fase hoofdschakelaar en aardlekbeveiliging. Speciale uitbreidingen in overleg.</p>
        </div>
        <div class="price-card">
          <h3>Extra groep bijplaatsen</h3>
          <div class="price-amount">vanaf € 60</div>
          <p>Afhankelijk van de huidige aardlekschakelaar en kastruimte. Stuur vooraf een foto mee voor direct uitsluitsel.</p>
        </div>
        <div class="price-card">
          <h3>Perilex stekker aansluiten</h3>
          <div class="price-amount">€ 120</div>
          <p>Alleen het aansluiten en doormeten van de perilex stekker/kookplaat bij een al geschikte contactdoos.</p>
        </div>
        <div class="price-card">
          <h3>Perilex kookgroep trekken</h3>
          <div class="price-amount">vanaf € 150</div>
          <p>Leiding en kookgroep trekken vanaf de meterkast naar keuken (voor inductiekookplaat of mechanische ventilatie).</p>
        </div>
        <div class="price-card">
          <h3>Speciale wensen & maatwerk</h3>
          <div class="price-amount">In overleg</div>
          <p>Verwijderingen, gedeeltelijke vernieuwingen of complexe renovaties? Altijd een heldere vaste prijs vooraf.</p>
        </div>
      </div>
      
      <div class="guarantees-grid">
        <div class="guarantee-item">
          <span>Altijd vaste prijs vooraf (geen verrassingen achteraf)</span>
        </div>
        <div class="guarantee-item">
          <span>Offerte binnen 24 uur (of direct telefonisch bij spoed)</span>
        </div>
        <div class="guarantee-item">
          <span>Inclusief garantie op de installatie</span>
        </div>
        <div class="guarantee-item">
          <span>Alleen A-merk componenten (Hager, ABB, Schneider, Eaton)</span>
        </div>
      </div>

      <p class="form-note price-note">Prijzen zijn inclusief 21% btw. Bij afwijkende situaties stemmen we altijd vooraf de exacte vaste prijs af na beoordeling van foto's of een schouw.</p>
      
      <div class="reassurance-band">
        <div>
          <h3>Nooit een verrassing op de factuur</h3>
          <p>Blijkt er tijdens een klus meer werk of extra materiaal nodig? Dan stoppen we en overleggen we eerst de prijs. Pas na jouw akkoord gaan we door.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">MEER PRIJZEN</span>
        <h2>Prijzen per dienst.</h2>
        <p>Op de dienstpagina's vind je de uitgebreide prijzen en wat er precies bij inbegrepen zit.</p>
      </div>
      <div class="addon-block">
        <div class="addon-list">
          <h3>Waar vind ik wat?</h3>
          <ul class="addon-items">
            <li><a href="groepenkast.html">Groepenkast vervangen</a><strong>vanaf € 620</strong></li>
            <li><a href="perilex.html">Perilex aansluiten</a><strong>€ 120</strong></li>
            <li><a href="frezen-stopcontacten-verleggen.html">Sleuven frezen</a><strong>vanaf € 10/meter</strong></li>
            <li><a href="frezen-stopcontacten-verleggen.html">Stopcontact verleggen</a><strong>vanaf € 120/punt</strong></li>
            <li><a href="laadpaal-installeren.html">Laadpaal installeren</a><strong>op maat</strong></li>
            <li><a href="krachtstroom-aanleggen.html">Krachtstroom aanleggen</a><strong>op maat</strong></li>
            <li><a href="tuinverlichting-buitenelektra.html">Tuinverlichting &amp; buitenelektra</a><strong>op maat</strong></li>
          </ul>
        </div>
        <div class="addon-includes">
          <h3>Liever eerst een schouw?</h3>
          <p>We komen bij je langs om de situatie te bekijken. Dit kost € 90 incl. btw en verrekenen we volledig zodra je akkoord geeft op de klus.</p>
          <p class="schouw-note">Een foto sturen via WhatsApp of het offerteformulier is gratis.</p>
          <div class="hero-actions" style="margin-bottom:0">
            <a class="btn btn-primary" href="afspraak.html">Schouw / afspraak aanvragen</a>
            <a class="btn btn-secondary" href="offerte.html">Offerte met foto's</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">PRIJS OP MAAT NODIG?</span>
      <h2>Vraag een offerte aan.</h2>
      <p>Stuur foto's mee en ontvang vooraf een vaste prijs.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag%20over%20jullie%20tarieven." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 11. werkwijze.html
PAGES_PART3["werkwijze.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Werkwijze | INO Techniek en Installatie</title>
  <meta name="description" content="Zo werkt INO Techniek en Installatie: van aanvraag en foto's tot uitvoering en oplevering. Duidelijk, met vaste prijs vooraf.">
  <meta property="og:title" content="Werkwijze | INO Techniek en Installatie">
  <meta property="og:description" content="Zo werkt INO Techniek en Installatie: van aanvraag en foto's tot uitvoering en oplevering. Duidelijk, met vaste prijs vooraf.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/werkwijze.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("werkwijze") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Werkwijze</div>
      <h1>Duidelijk van aanvraag tot oplevering.</h1>
      <p>Vier stappen, van je eerste bericht tot een geteste en opgeleverde installatie.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Hier lees je hoe een klus verloopt, van je eerste bericht tot de oplevering, zodat je weet wat je kunt verwachten.</span></div>
    </div>
  </section>

  <section class="dark-section" id="werkwijze">
    <div class="container">
      <div class="section-heading light">
        <span class="eyebrow">ZO WERKT HET</span>
        <h2>In vier stappen geregeld.</h2>
      </div>
      <div class="steps">
        <div class="step"><b>01</b><h3>Vertel wat je nodig hebt</h3><p>Via het formulier, telefoon of WhatsApp.</p></div>
        <div class="step"><b>02</b><h3>We bekijken de situatie</h3><p>Waar nodig beoordelen we foto's of komen we op locatie kijken.</p></div>
        <div class="step"><b>03</b><h3>We voeren het werk uit</h3><p>Netjes, zorgvuldig en passend bij de situatie.</p></div>
        <div class="step"><b>04</b><h3>Getest en opgeleverd</h3><p>Na afronding controleren we het uitgevoerde werk.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">ZO BEGIN JE</span>
        <h2>Drie manieren om te starten.</h2>
      </div>
      <div class="cert-grid">
        <div class="cert-card">
          <h3>Bel of app</h3>
          <p>Voor een snelle vraag of een storing. Je krijgt direct een inschatting.</p>
          <p><a class="mini-link" href="contact.html">Naar contact →</a></p>
        </div>
        <div class="cert-card">
          <h3>Offerte met foto's</h3>
          <p>Beschrijf de klus en stuur foto's van bijvoorbeeld je meterkast mee. Zo krijg je vooraf een vaste prijs.</p>
          <p><a class="mini-link" href="offerte.html">Offerte aanvragen →</a></p>
        </div>
        <div class="cert-card">
          <h3>Schouw of afspraak</h3>
          <p>Liever dat we langskomen? Een schouw kost € 90 en wordt volledig verrekend zodra je akkoord geeft.</p>
          <p><a class="mini-link" href="afspraak.html">Afspraak aanvragen →</a></p>
        </div>
      </div>
      <div class="reassurance-band">
        <div>
          <h3>Nooit een verrassing op de factuur</h3>
          <p>Blijkt er tijdens een klus meer werk of extra materiaal nodig? Dan stoppen we en overleggen we eerst de prijs. Pas na jouw akkoord gaan we door.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">KLAAR OM TE STARTEN?</span>
      <h2>Begin met een bericht of een foto.</h2>
      <p>Meer heb je niet nodig voor stap één.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20wil%20graag%20een%20klus%20laten%20uitvoeren." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 12. werkgebied.html
PAGES_PART3["werkgebied.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Werkgebied | INO Techniek en Installatie</title>
  <meta name="description" content="INO werkt in Utrecht, Nieuwegein, Houten, Zeist, Maarssen, De Bilt, IJsselstein, Woerden, Amersfoort en Veenendaal. Bekijk de kaart.">
  <meta property="og:title" content="Werkgebied | INO Techniek en Installatie">
  <meta property="og:description" content="INO werkt in Utrecht, Nieuwegein, Houten, Zeist, Maarssen, De Bilt, IJsselstein, Woerden, Amersfoort en Veenendaal. Bekijk de kaart.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/werkgebied.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("werkgebied") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Werkgebied</div>
      <h1>Elektricien in heel Utrecht en omstreken.</h1>
      <p>INO werkt voor particulieren en bedrijven in de stad en provincie Utrecht, van Woerden tot Amersfoort en van Maarssen tot Veenendaal.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Hier controleer je of INO bij jou in de buurt werkt en wat voorrijden kost.</span></div>
    </div>
  </section>

  <section class="section" id="werkgebied">
    <div class="container map-layout">
      <div class="map-card">
        <button class="map-enlarge-btn" id="mapEnlargeBtn" type="button" aria-haspopup="dialog">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M9 3H3v6M15 3h6v6M9 21H3v-6M15 21h6v-6"/></svg>
          Kaart vergroten
        </button>
        <svg class="map-svg" viewBox="0 0 480 440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Werkgebied van INO Techniek en Installatie in en rond Utrecht">
          <rect x="0" y="0" width="480" height="440" fill="#f5f8f4"/>
          <path d="M0 120 Q 90 100 160 140 T 300 150 Q 380 140 480 175 V0H0Z" fill="#eef4ee"/>
          <path d="M0 440 Q 100 380 210 400 T 400 370 Q 450 365 480 380 V440Z" fill="#eef4ee"/>
          <circle cx="70" cy="330" r="46" fill="#e2eee0"/>
          <circle cx="400" cy="90" r="60" fill="#e2eee0"/>
          <circle cx="420" cy="330" r="40" fill="#e2eee0"/>
          <path d="M60 60 Q 140 130 190 200 T 260 320 Q 300 380 380 420" fill="none" stroke="#bcd7ec" stroke-width="10" stroke-linecap="round" opacity=".75"/>
          <path d="M60 60 Q 140 130 190 200 T 260 320 Q 300 380 380 420" fill="none" stroke="#9ec5e0" stroke-width="2" stroke-linecap="round" opacity=".6"/>
          <g stroke="#d7cfa8" stroke-width="3" fill="none" opacity=".8">
            <path d="M240 220 L 90 340"/>
            <path d="M240 220 L 150 90"/>
            <path d="M240 220 L 330 130"/>
            <path d="M240 220 L 360 230"/>
            <path d="M240 220 L 330 330"/>
            <path d="M240 220 L 190 380"/>
            <path d="M240 220 L 100 200"/>
            <path d="M150 90 L 60 55"/>
            <path d="M330 130 L 410 70"/>
            <path d="M330 330 L 400 355"/>
          </g>
          <g font-family="Inter,Arial,sans-serif">
            <g>
              <circle cx="240" cy="220" r="9" fill="#278a1d"/>
              <circle cx="240" cy="220" r="9" fill="none" stroke="#fff" stroke-width="2.5"/>
              <text x="252" y="216" font-size="15" font-weight="800" fill="#101712">Utrecht</text>
            </g>
            <g><circle cx="90" cy="340" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="100" y="345" font-size="12" font-weight="700" fill="#111827">Nieuwegein</text></g>
            <g><circle cx="190" cy="380" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="200" y="385" font-size="12" font-weight="700" fill="#111827">Houten</text></g>
            <g><circle cx="330" cy="130" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="340" y="126" font-size="12" font-weight="700" fill="#111827">Zeist</text></g>
            <g><circle cx="150" cy="90" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="160" y="86" font-size="12" font-weight="700" fill="#111827">Maarssen</text></g>
            <g><circle cx="360" cy="230" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="370" y="235" font-size="12" font-weight="700" fill="#111827">De Bilt</text></g>
            <g><circle cx="100" cy="200" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="45" y="196" font-size="12" font-weight="700" fill="#111827">IJsselstein</text></g>
            <g><circle cx="60" cy="55" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="15" y="42" font-size="12" font-weight="700" fill="#111827">Woerden</text></g>
            <g><circle cx="410" cy="70" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="345" y="58" font-size="12" font-weight="700" fill="#111827">Amersfoort</text></g>
            <g><circle cx="400" cy="355" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="330" y="372" font-size="12" font-weight="700" fill="#111827">Veenendaal</text></g>
            <g><circle cx="330" cy="330" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="340" y="335" font-size="12" font-weight="700" fill="#111827">IJburg-route A12</text></g>
          </g>
          <g transform="translate(38,378)">
            <rect x="-6" y="-6" width="96" height="46" rx="10" fill="#fff" stroke="#e4e9e5" stroke-width="1.5"/>
            <path d="M20 26 L20 4 M12 12 L20 4 L28 12" stroke="#278a1d" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <text x="34" y="15" font-size="10" fill="#65707d" font-weight="700">N</text>
            <line x1="34" y1="24" x2="78" y2="24" stroke="#65707d" stroke-width="1.5"/>
            <line x1="34" y1="21" x2="34" y2="27" stroke="#65707d" stroke-width="1.5"/>
            <line x1="78" y1="21" x2="78" y2="27" stroke="#65707d" stroke-width="1.5"/>
            <text x="40" y="35" font-size="8" fill="#65707d">0&#160;&#160;&#160;&#160;5&#160;&#160;&#160;&#160;10 km</text>
          </g>
          <g transform="translate(18,16)">
            <rect width="150" height="46" rx="10" fill="#fff" stroke="#e4e9e5" stroke-width="1.5"/>
            <text x="14" y="20" font-size="12" font-weight="800" fill="#101712" letter-spacing="1">UTRECHT</text>
            <text x="14" y="35" font-size="9" fill="#65707d" letter-spacing="2">NEDERLAND</text>
          </g>
        </svg>
        <p class="map-caption">Werkgebied van INO Techniek en Installatie: actief in heel Utrecht en omstreken, bij storingen vaak dezelfde dag ter plaatse.</p>
      </div>
      <div>
        <span class="eyebrow">DEZE PLAATSEN</span>
        <h2>Hier zijn we actief.</h2>
        <p>Bij storingen zijn we vaak dezelfde dag ter plaatse. Twijfel je of jouw plaats erbij zit? Neem gerust contact op.</p>
        <div class="location-columns">
          <ul><li>Utrecht</li><li>Nieuwegein</li><li>Houten</li><li>Zeist</li></ul>
          <ul><li>Maarssen</li><li>De Bilt</li><li>IJsselstein</li><li>Woerden</li></ul>
          <ul><li>Amersfoort</li><li>Veenendaal</li></ul>
        </div>
        <p class="mini-link" style="display:inline-block;margin-top:22px"><a href="offerte.html">Check je adres →</a></p>
        <a class="btn btn-secondary" style="margin-top:18px" href="wijken.html">Elektricien per wijk en regio</a>
      </div>
    </div>
  </section>

  <div class="map-modal" id="mapModal">
    <div class="map-modal-inner">
      <button class="map-modal-close" id="mapModalClose" type="button" aria-label="Kaart sluiten">✕</button>
      <svg viewBox="0 0 480 440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Werkgebied van INO Techniek en Installatie, vergroot">
        <rect x="0" y="0" width="480" height="440" fill="#f5f8f4"/>
        <path d="M0 120 Q 90 100 160 140 T 300 150 Q 380 140 480 175 V0H0Z" fill="#eef4ee"/>
        <path d="M0 440 Q 100 380 210 400 T 400 370 Q 450 365 480 380 V440Z" fill="#eef4ee"/>
        <circle cx="70" cy="330" r="46" fill="#e2eee0"/>
        <circle cx="400" cy="90" r="60" fill="#e2eee0"/>
        <circle cx="420" cy="330" r="40" fill="#e2eee0"/>
        <path d="M60 60 Q 140 130 190 200 T 260 320 Q 300 380 380 420" fill="none" stroke="#bcd7ec" stroke-width="10" stroke-linecap="round" opacity=".75"/>
        <path d="M60 60 Q 140 130 190 200 T 260 320 Q 300 380 380 420" fill="none" stroke="#9ec5e0" stroke-width="2" stroke-linecap="round" opacity=".6"/>
        <g stroke="#d7cfa8" stroke-width="3" fill="none" opacity=".8">
          <path d="M240 220 L 90 340"/><path d="M240 220 L 150 90"/><path d="M240 220 L 330 130"/>
          <path d="M240 220 L 360 230"/><path d="M240 220 L 330 330"/><path d="M240 220 L 190 380"/>
          <path d="M240 220 L 100 200"/><path d="M150 90 L 60 55"/><path d="M330 130 L 410 70"/><path d="M330 330 L 400 355"/>
        </g>
        <g font-family="Inter,Arial,sans-serif">
          <g><circle cx="240" cy="220" r="9" fill="#278a1d"/><circle cx="240" cy="220" r="9" fill="none" stroke="#fff" stroke-width="2.5"/><text x="252" y="216" font-size="15" font-weight="800" fill="#101712">Utrecht</text></g>
          <g><circle cx="90" cy="340" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="100" y="345" font-size="12" font-weight="700" fill="#111827">Nieuwegein</text></g>
          <g><circle cx="190" cy="380" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="200" y="385" font-size="12" font-weight="700" fill="#111827">Houten</text></g>
          <g><circle cx="330" cy="130" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="340" y="126" font-size="12" font-weight="700" fill="#111827">Zeist</text></g>
          <g><circle cx="150" cy="90" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="160" y="86" font-size="12" font-weight="700" fill="#111827">Maarssen</text></g>
          <g><circle cx="360" cy="230" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="370" y="235" font-size="12" font-weight="700" fill="#111827">De Bilt</text></g>
          <g><circle cx="100" cy="200" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="45" y="196" font-size="12" font-weight="700" fill="#111827">IJsselstein</text></g>
          <g><circle cx="60" cy="55" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="15" y="42" font-size="12" font-weight="700" fill="#111827">Woerden</text></g>
          <g><circle cx="410" cy="70" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="345" y="58" font-size="12" font-weight="700" fill="#111827">Amersfoort</text></g>
          <g><circle cx="400" cy="355" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="330" y="372" font-size="12" font-weight="700" fill="#111827">Veenendaal</text></g>
          <g><circle cx="330" cy="330" r="5.5" fill="#6bd34d" stroke="#278a1d" stroke-width="1.5"/><text x="340" y="335" font-size="12" font-weight="700" fill="#111827">IJburg-route A12</text></g>
        </g>
        <g transform="translate(18,16)">
          <rect width="150" height="46" rx="10" fill="#fff" stroke="#e4e9e5" stroke-width="1.5"/>
          <text x="14" y="20" font-size="12" font-weight="800" fill="#101712" letter-spacing="1">UTRECHT</text>
          <text x="14" y="35" font-size="9" fill="#65707d" letter-spacing="2">NEDERLAND</text>
        </g>
      </svg>
    </div>
  </div>

  <section class="section soft">
    <div class="container">
      <div class="cert-grid">
        <div class="cert-card">
          <h3>Voorrijkosten</h3>
          <p>Binnen Utrecht rekenen we € 0,- voorrijkosten. Buiten Utrecht geldt een vast kilometertarief van € 0,40 per km.</p>
        </div>
        <div class="cert-card">
          <h3>Per wijk en regio</h3>
          <p>Kies je wijk of regio voor een elektricien die de buurt kent.</p>
          <p><a class="mini-link" href="wijken.html">Bekijk alle wijken →</a></p>
        </div>
        <div class="cert-card">
          <h3>Storing?</h3>
          <p>Geen stroom, kortsluiting of rook uit de meterkast? Bel direct, we zijn 24/7 bereikbaar.</p>
          <p><a class="mini-link" href="tel:+31628763775">Bel 06 28 76 37 75 →</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">STAAT JE PLAATS ER NIET BIJ?</span>
      <h2>Vraag je adres na.</h2>
      <p>We komen vaak ook net buiten het werkgebied langs.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20werken%20jullie%20ook%20in%20mijn%20plaats%3F" target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 13. wijken.html
PAGES_PART3["wijken.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Elektricien Utrecht per Wijk &amp; Regio | INO Techniek</title>
  <meta name="description" content="Erkend elektricien in alle wijken van Utrecht en omstreken (Binnenstad, Oost, Leidsche Rijn, Nieuwegein, Maarssen, Zeist). Vaste prijs en 24/7 storingsdienst.">
  <link rel="canonical" href="https://ino-elektra.nl/wijken">
  <meta name="robots" content="index, follow">
  <meta property="og:locale" content="nl_NL">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Elektricien Utrecht per Wijk &amp; Regio | INO Techniek">
  <meta property="og:description" content="Erkend elektricien in alle wijken van Utrecht en omstreken (Binnenstad, Oost, Leidsche Rijn, Nieuwegein, Maarssen, Zeist). Vaste prijs en 24/7 storingsdienst.">
  <meta property="og:url" content="https://ino-elektra.nl/wijken">
  <meta property="og:site_name" content="INO Techniek en Installatie">
  <meta property="og:image" content="https://ino-elektra.nl/hero-elektricien.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Elektricien in alle wijken van Utrecht en omstreken">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Elektricien Utrecht per Wijk &amp; Regio | INO Techniek">
  <meta name="twitter:description" content="Erkend elektricien in alle wijken van Utrecht en omliggende gemeenten. NEN 1010 gecertificeerd.">
  <meta name="twitter:image" content="https://ino-elektra.nl/hero-elektricien.jpg">
  <link rel="stylesheet" href="style.css?v=6">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Electrician",
    "name": "INO Techniek en Installatie - Utrecht en Regio",
    "url": "https://ino-elektra.nl/wijken",
    "telephone": "+31628763775",
    "description": "Erkend elektricien werkzaam in alle wijken van Utrecht en de omliggende regio voor groepenkasten, Perilex en spoedklussen.",
    "areaServed": [
      "Binnenstad Utrecht", "Utrecht Oost", "Utrecht Noordoost", "Overvecht", "Zuilen", "Lombok", "Kanaleneiland", "Hoograven", "Leidsche Rijn", "Vleuten", "De Meern",
      "Nieuwegein", "Houten", "Zeist", "Maarssen", "De Bilt", "IJsselstein", "Woerden", "Amersfoort", "Veenendaal"
    ]
  }
  </script>
</head>
<body>

""" + make_header("werkgebied") + """

<main>
  <section class="section" style="padding-bottom:0">
    <div class="container">
      <p class="form-note" style="margin-bottom:0"><a href="werkgebied.html" class="mini-link">← Terug naar werkgebied</a></p>
    </div>
  </section>

  <section class="section" style="padding-top:22px">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">WERKGEBIED UTRECHT &amp; REGIO</span>
        <h1>Elektricien in Elke Wijk van Utrecht &amp; Regio</h1>
        <p>Kies je wijk of regio voor een elektricien die de buurt kent. Overal dezelfde vaste prijzen vooraf en 24/7 storingsdienst.</p>
      </div>

      <a class="alert-banner" href="tel:+31628763775">
        <div>
          <strong>Storing? Bel direct — 24/7 bereikbaar</strong>
          <span>Geen stroom, kortsluiting of rook uit de meterkast? Bel 06 28 76 37 75, ook 's avonds en in het weekend.</span>
        </div>
        <span class="arrow">→</span>
      </a>

      <h3 class="wijk-label">Utrecht</h3>
      <div class="wijk-grid">
        <a class="wijk-card" href="offerte.html?wijk=Binnenstad">
          <div><h3>Elektricien Binnenstad</h3><p>Domplein · Neude · Oudegracht</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Oost">
          <div><h3>Elektricien Oost</h3><p>Wilhelminapark · Rubenslaan · Abstede</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Noordoost">
          <div><h3>Elektricien Noordoost</h3><p>Tuindorp · Voordorp · Watervogelbuurt</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Overvecht">
          <div><h3>Elektricien Overvecht</h3><p>Overvecht-Noord · Overvecht-Zuid</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Noordwest">
          <div><h3>Elektricien Noordwest</h3><p>Zuilen · Ondiep · Pijlsweerd</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=West">
          <div><h3>Elektricien West</h3><p>Lombok · Oog in Al</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Zuidwest">
          <div><h3>Elektricien Zuidwest</h3><p>Kanaleneiland · Transwijk · Rivierenwijk</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Zuid">
          <div><h3>Elektricien Zuid</h3><p>Hoograven · Tolsteeg · Bokkenbuurt</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Leidsche-Rijn">
          <div><h3>Elektricien Leidsche Rijn</h3><p>Terwijde · Vleuterweide · Parkwijk</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Vleuten-De-Meern">
          <div><h3>Elektricien Vleuten-De Meern</h3><p>Vleuten · De Meern · Haarzicht</p></div>
        </a>
      </div>

      <h3 class="wijk-label">Regio Utrecht</h3>
      <div class="wijk-grid">
        <a class="wijk-card" href="offerte.html?wijk=Nieuwegein">
          <div><h3>Elektricien Nieuwegein</h3><p>Batau · Doorslag · City</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Houten">
          <div><h3>Elektricien Houten</h3><p>Houten-Zuid · Castellum · Het Rond</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Zeist">
          <div><h3>Elektricien Zeist</h3><p>Zeist-West · Kerckebosch · Vollenhove</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Maarssen">
          <div><h3>Elektricien Maarssen</h3><p>Maarssenbroek · Zogweteringen</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=De-Bilt">
          <div><h3>Elektricien De Bilt</h3><p>De Bilt · Bilthoven</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=IJsselstein">
          <div><h3>Elektricien IJsselstein</h3><p>IJsselveld · Zenderpark</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Woerden">
          <div><h3>Elektricien Woerden</h3><p>Woerden-Centrum · Molenvliet</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Amersfoort">
          <div><h3>Elektricien Amersfoort</h3><p>Kruiskamp · Vathorst · Schothorst</p></div>
        </a>
        <a class="wijk-card" href="offerte.html?wijk=Veenendaal">
          <div><h3>Elektricien Veenendaal</h3><p>Veenendaal-Oost · De Compagnie</p></div>
        </a>
      </div>

      <p class="form-note" style="margin-top:28px">Staat jouw wijk of plaats er niet bij? We komen vaak ook net daarbuiten langs — <a href="offerte.html" class="mini-link">vraag je adres na →</a></p>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 14. vakmanschap.html
PAGES_PART3["vakmanschap.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Vakmanschap en garantie | INO Techniek en Installatie</title>
  <meta name="description" content="NEN 1010, NEN 3140 VP en 12 maanden garantie: dit is waar INO Techniek en Installatie voor staat. Veilig werk aan je elektrische installatie.">
  <meta property="og:title" content="Vakmanschap en garantie | INO Techniek en Installatie">
  <meta property="og:description" content="NEN 1010, NEN 3140 VP en 12 maanden garantie: dit is waar INO Techniek en Installatie voor staat. Veilig werk aan je elektrische installatie.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/vakmanschap.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("vakmanschap") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Vakmanschap</div>
      <h1>Vakbekwaam en gecertificeerd.</h1>
      <p>Werk aan elektrische installaties vraagt om kennis van zaken. INO werkt volgens de geldende normen.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Hier lees je op welke normen en garanties je kunt rekenen, zodat je weet dat het werk veilig en verantwoord wordt uitgevoerd.</span></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cert-grid">
        <div class="cert-card">
          <h3>NEN 1010 Garantie</h3>
          <p>Alle installaties worden strikt aangelegd volgens de NEN 1010: dé Nederlandse veiligheidsnorm voor veilige, betrouwbare en brandveilige elektrotechnische installaties.</p>
        </div>
        <div class="cert-card">
          <h3>NEN 3140 VP</h3>
          <p>Gecertificeerd voor het veilig werken aan en met elektrische installaties volgens de NEN 3140-norm.</p>
        </div>
        <div class="cert-card">
          <h3>Garantie op ons werk</h3>
          <p>12 maanden garantie op uitgevoerd werk en 2 jaar op geplaatste materialen.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section soft">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">IN DE PRAKTIJK</span>
        <h2>Wat dat voor jou betekent.</h2>
      </div>
      <div class="showcase-block" style="margin-bottom: 34px;">
        <div class="hero-image-wrapper">
          <img src="Gemini_Generated_Image_fuc7skfuc7skfuc7.jpg" onerror="this.onerror=null; this.src='groepenkast-montage.jpg';" alt="INO monteur aan het werk volgens NEN 1010 en NEN 3140 normen" class="showcase-img" loading="lazy" referrerPolicy="no-referrer">
          <div class="hero-badge-floating">Vakmanschap · NEN 1010 gecertificeerd · Veiligheid voorop</div>
        </div>
      </div>
      <div class="guarantees-grid">
        <div class="guarantee-item"><span>Alleen A-merk componenten (Hager, ABB, Schneider, Eaton)</span></div>
        <div class="guarantee-item"><span>Elke installatie getest, doorgemeten en gelabeld</span></div>
        <div class="guarantee-item"><span>Altijd vaste prijs vooraf</span></div>
        <div class="guarantee-item"><span>Sinds 2021 actief in Utrecht</span></div>
      </div>
      <p class="form-note price-note">Benieuwd wat klanten ervan vinden? Lees de <a class="mini-link" href="reviews.html">reviews</a>.</p>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">VAKWERK NODIG?</span>
      <h2>Laat het door een vakman doen.</h2>
      <p>Vraag een offerte aan, of bel direct als het niet kan wachten.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag%20over%20een%20elektrotechnische%20klus." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 15. reviews.html
PAGES_PART3["reviews.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Reviews | INO Techniek en Installatie</title>
  <meta name="description" content="Lees wat klanten op Google over INO Techniek en Installatie zeggen. Bekijk het volledige overzicht van reviews.">
  <meta property="og:title" content="Reviews | INO Techniek en Installatie">
  <meta property="og:description" content="Lees wat klanten op Google over INO Techniek en Installatie zeggen. Bekijk het volledige overzicht van reviews.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/reviews.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("reviews") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Reviews</div>
      <h1>Wat klanten op Google zeggen.</h1>
      <p>Bekijk het volledige, geverifieerde overzicht van onze Google-reviews.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Hier lees je wat andere klanten van het werk vinden, voordat je zelf een keuze maakt.</span></div>
    </div>
  </section>

  <section class="section" id="reviews">
    <div class="container">
      <a class="google-featured" href="https://www.google.com/maps?cid=15258938996024411928" target="_blank" rel="noopener">
        <div>
          <h3>INO Techniek en Installatie op Google</h3>
          <p>Klik door naar ons Google-bedrijfsprofiel voor de actuele score en alle reviews.</p>
        </div>
        <span class="btn btn-primary">Bekijk alle Google-reviews →</span>
      </a>
      <div class="review-grid google-quotes">
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p>"Zeer tevreden over de service. Professioneel, netjes gewerkt en duidelijke communicatie. Zeker een aanrader!"</p>
          <div class="review-source">Ali · Google-review</div>
        </div>
        <div class="review-card">
          <div class="review-stars">★★★★★</div>
          <p>"Geweldige klusbedrijf, zeker aan te raden! Heel netjes en snel afgehandeld."</p>
          <div class="review-source">Hasan Demir · Google-review</div>
        </div>
        <a class="review-card placeholder-review" href="https://www.google.com/maps?cid=15258938996024411928" target="_blank" rel="noopener">
          <div class="review-stars">★★★★★</div>
          <p>Bekijk alle Google-reviews →</p>
          <div class="review-source">Meer klantervaringen op Google</div>
        </a>
      </div>
      <div class="werkspot-corner">
        <span class="review-stars small">★★★★★</span>
        <span>5.0 op <strong>Werkspot</strong></span>
        <a href="https://www.werkspot.nl" target="_blank" rel="noopener" class="mini-link">bekijken →</a>
      </div>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">OOK TEVREDEN KLANT WORDEN?</span>
      <h2>Vraag een offerte aan.</h2>
      <p>Beschrijf je klus en ontvang vooraf een vaste prijs.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag%20over%20een%20elektrotechnische%20klus." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 16. offerte.html
PAGES_PART3["offerte.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Offerte aanvragen | INO Techniek en Installatie</title>
  <meta name="description" content="Vraag een offerte aan bij INO Techniek en Installatie. Beschrijf je klus, voeg foto's toe en ontvang een vaste prijs vooraf.">
  <meta property="og:title" content="Offerte aanvragen | INO Techniek en Installatie">
  <meta property="og:description" content="Vraag een offerte aan bij INO Techniek en Installatie. Beschrijf je klus, voeg foto's toe en ontvang een vaste prijs vooraf.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/offerte.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Offerte aanvragen</div>
      <h1>Vertel wat er moet gebeuren.</h1>
      <p>Je kunt foto's van de situatie meesturen. Dat helpt om vooraf een beter beeld van de klus te krijgen.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Beschrijf je klus, voeg foto's toe en ontvang een vaste prijs vooraf. Geschikt voor alles wat niet met spoed hoeft.</span></div>
    </div>
  </section>

  <section class="section soft" id="offerte">
    <div class="container form-layout">
      <div>
        <span class="eyebrow">OFFERTE / AANVRAAG</span>
        <h2>Stuur je aanvraag in.</h2>
        <p>Vul het formulier in. We bekijken je aanvraag en komen met een vaste prijs.</p>
        <div class="form-benefits"><div>✓ Foto's meesturen</div><div>✓ Gewenste datum aangeven</div><div>✓ Dienst selecteren</div><div>✓ Offerte binnen 24 uur</div></div>
        <p class="form-note" style="margin-top:22px">Is het een storing? Bel dan direct: <a class="mini-link" href="tel:+31628763775">06 28 76 37 75</a></p>
      </div>
      <form id="quoteForm" class="quote-form" action="https://formsubmit.co/d0d9de6bb2a30083d92c3fe4775b9ce6" method="POST" enctype="multipart/form-data">
        <input type="hidden" name="_subject" value="Nieuwe offerteaanvraag via de website">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <label>Soort werkzaamheden
          <select name="service" required>
            <option value="">Kies een dienst</option>
            <option>Meterkast vernieuwen</option><option>Nieuwe groep</option><option>Elektra / bekabeling</option>
            <option>Stopcontact / schakelaar</option><option>Montage / installatie</option><option>Storing</option><option>Anders</option>
          </select>
        </label>
        <label>Naam<input name="name" required placeholder="Voor- en achternaam"></label>
        <div class="two-col">
          <label>Telefoon<input name="phone" required placeholder="06 ..."></label>
          <label>E-mail<input name="email" type="email" required placeholder="naam@email.nl"></label>
        </div>
        <div class="two-col">
          <label>Postcode<input name="postcode" placeholder="1234 AB"></label>
          <label>Huisnummer<input name="number" placeholder="12"></label>
        </div>
        <label>Omschrijving<textarea name="message" id="message" rows="5" required placeholder="Wat moet er gebeuren?"></textarea></label>
        <label>Foto's toevoegen (zeer aanbevolen)
          <span style="font-weight:400;font-size:12px;color:var(--muted)">Voeg 1 of meerdere foto's toe van je huidige meterkast / aardlekschakelaar. Zo kunnen we direct zien of uitbreiding mogelijk is en ontvang je direct een vaste prijs!</span>
          <input id="photos" name="photos" type="file" accept="image/*" multiple>
        </label>
        <div id="photoList" class="photo-list"></div>
        <label class="check"><input type="checkbox" required> Ik ga akkoord dat INO mijn gegevens gebruikt om contact op te nemen over deze aanvraag.</label>
        <button class="btn btn-primary full" type="submit">Aanvraag voorbereiden</button>
        <p class="form-note">Je aanvraag, inclusief eventuele foto's, komt rechtstreeks binnen op info@ino-elektra.nl.</p>
        <div id="formResult" class="form-result" hidden></div>
      </form>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">LIEVER EERST OVERLEGGEN?</span>
      <h2>Bel of app gerust.</h2>
      <p>Je krijgt direct een inschatting. Wil je dat we langskomen? Dan plan je een afspraak.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="afspraak.html">Afspraak aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag%20over%20een%20offerte." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 17. afspraak.html
PAGES_PART3["afspraak.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Afspraak aanvragen | INO Techniek en Installatie</title>
  <meta name="description" content="Plan een afspraak of schouw met INO Techniek en Installatie. Geef je voorkeursdatum en -tijd door, wij bevestigen persoonlijk.">
  <meta property="og:title" content="Afspraak aanvragen | INO Techniek en Installatie">
  <meta property="og:description" content="Plan een afspraak of schouw met INO Techniek en Installatie. Geef je voorkeursdatum en -tijd door, wij bevestigen persoonlijk.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/afspraak.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Afspraak aanvragen</div>
      <h1>Plan je afspraak met INO.</h1>
      <p>De gekozen datum en tijd zijn een voorkeur; de definitieve afspraak bevestigen we persoonlijk.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Geef je voorkeursdatum en -tijd door voor een schouw of klus. Wij nemen contact op om de afspraak te bevestigen.</span></div>
    </div>
  </section>

  <section class="section" id="afspraak">
    <div class="container appointment">
      <div>
        <span class="eyebrow">AFSPRAAK AANVRAGEN</span>
        <h2>Wanneer komt het je uit?</h2>
        <p>Kies een datum en tijdvak en laat je gegevens achter, zodat we je kunnen bereiken.</p>
        <ul class="include-items">
          <li>✓ Schouw op locatie: € 90 incl. btw, volledig verrekend bij opdracht</li>
          <li>✓ Geen voorrijkosten binnen Utrecht</li>
          <li>✓ Definitieve afspraak bevestigen we persoonlijk</li>
        </ul>
      </div>
      <form id="appointmentForm" class="appointment-form" action="https://formsubmit.co/d0d9de6bb2a30083d92c3fe4775b9ce6" method="POST">
        <input type="hidden" name="_subject" value="Nieuwe afspraakvoorkeur via de website">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <label>Naam<input name="name" required placeholder="Voor- en achternaam"></label>
        <label>Telefoon<input name="phone" required placeholder="06 ..."></label>
        <label>Gewenste datum<input type="date" id="date" name="datum" required></label>
        <label>Voorkeurstijd<select name="tijd" required><option value="">Kies een tijd</option><option>08:00 – 10:00</option><option>10:00 – 12:00</option><option>12:00 – 14:00</option><option>14:00 – 16:00</option><option>16:00 – 18:00</option></select></label>
        <label class="span-2">Waar gaat het om? (optioneel)<textarea name="message" rows="3" placeholder="Bijv. schouw voor een nieuwe groepenkast"></textarea></label>
        <button class="btn btn-primary" type="submit">Voorkeur aanvragen</button>
        <div id="formResult" class="form-result" hidden></div>
      </form>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">LIEVER EERST EEN OFFERTE?</span>
      <h2>Vraag een vaste prijs aan.</h2>
      <p>Stuur foto's mee, dan weet je vooraf wat het kost.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20wil%20graag%20een%20afspraak%20plannen." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 18. faq.html
PAGES_PART3["faq.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Veelgestelde vragen | INO Techniek en Installatie</title>
  <meta name="description" content="Antwoorden op veelgestelde vragen over tarieven, garantie, schouw, voorrijkosten en werkzaamheden van INO Techniek en Installatie.">
  <meta property="og:title" content="Veelgestelde vragen | INO Techniek en Installatie">
  <meta property="og:description" content="Antwoorden op veelgestelde vragen over tarieven, garantie, schouw, voorrijkosten en werkzaamheden van INO Techniek en Installatie.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/faq.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Veelgestelde vragen</div>
      <h1>Veelgestelde vragen.</h1>
      <p>Snel antwoord op wat klanten het vaakst vragen.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Hier vind je snel antwoord op de vragen die klanten het vaakst stellen, zonder dat je hoeft te bellen.</span></div>
    </div>
  </section>

  <section class="section soft" id="faq">
    <div class="container narrow">
      <div class="faq">
        <button class="faq-q">Welke werkzaamheden voert INO uit?<span>+</span></button><div class="faq-a">INO richt zich onder andere op meterkasten, nieuwe groepen, elektra en bekabeling, stopcontacten, montage, installatie en het opsporen en oplossen van storingen. Alle diensten staan op de <a class="mini-link" href="diensten.html">dienstenpagina</a>.</div>
        <button class="faq-q">Kan ik foto's van mijn situatie meesturen?<span>+</span></button><div class="faq-a">Ja. In het offerteformulier kun je foto's van bijvoorbeeld de meterkast of de betreffende ruimte toevoegen. Een foto sturen via WhatsApp of het formulier is gratis.</div>
        <button class="faq-q">Kan ik eerst een offerte aanvragen?<span>+</span></button><div class="faq-a">Ja. Via het aanvraagformulier kun je de werkzaamheden en situatie beschrijven. De definitieve werkwijze en prijs stemmen we af op de situatie.</div>
        <button class="faq-q">Werkt INO voor particulieren en bedrijven?<span>+</span></button><div class="faq-a">De website is ingericht voor zowel particuliere als zakelijke aanvragen.</div>
        <button class="faq-q">Wat kost een schouw op locatie?<span>+</span></button><div class="faq-a">Een schouw kost € 90 incl. btw. Dat bedrag verrekenen we volledig zodra je akkoord geeft op de klus.</div>
        <button class="faq-q">Wat zijn de voorrijkosten?<span>+</span></button><div class="faq-a">Binnen Utrecht rekenen we € 0,- voorrijkosten. Buiten Utrecht geldt een vast kilometertarief van € 0,40 per km.</div>
        <button class="faq-q">Welke garantie krijg ik?<span>+</span></button><div class="faq-a">12 maanden garantie op het uitgevoerde werk en 2 jaar fabrieksgarantie op materialen, alles volgens de NEN 1010-norm.</div>
        <button class="faq-q">Ben ik ook 's avonds en in het weekend welkom te bellen?<span>+</span></button><div class="faq-a">Ja, bij storingen ben je 24/7 welkom te bellen. Voor spoed gelden deze uurtarieven (incl. btw): overdag € 90, buiten kantooruren € 120, vanaf 22:00 en in het weekend € 145.</div>
        <button class="faq-q">Werkt INO ook in mijn plaats?<span>+</span></button><div class="faq-a">We werken in de stad en provincie Utrecht. Staat jouw plaats er niet bij? We komen vaak ook net daarbuiten langs, vraag je adres na via het <a class="mini-link" href="werkgebied.html">werkgebied</a>.</div>
        <button class="faq-q">Wat als er tijdens de klus meer werk nodig blijkt?<span>+</span></button><div class="faq-a">Dan stoppen we en overleggen we eerst de prijs. Pas na jouw akkoord gaan we door.</div>
      </div>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">VRAAG NIET BEANTWOORD?</span>
      <h2>Stel je vraag rechtstreeks.</h2>
      <p>We denken graag met je mee.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="contact.html">Contact opnemen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 19. contact.html
PAGES_PART3["contact.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Contact Elektricien Utrecht | INO Techniek en Installatie</title>
  <meta name="description" content="Contact opnemen met elektricien INO in Utrecht. Bel direct 06 28 76 37 75, stuur een WhatsApp of e-mail naar info@ino-elektra.nl. 24/7 bereikbaar bij stroomstoringen.">
  <link rel="canonical" href="https://ino-elektra.nl/contact">
  <meta name="robots" content="index, follow">
  <meta property="og:locale" content="nl_NL">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Contact Elektricien Utrecht | INO Techniek en Installatie">
  <meta property="og:description" content="Neem direct contact op met INO Techniek en Installatie in Utrecht. Bel 06 28 76 37 75 voor spoed, advies of een vrijblijvende offerte.">
  <meta property="og:url" content="https://ino-elektra.nl/contact">
  <meta property="og:site_name" content="INO Techniek en Installatie">
  <meta property="og:image" content="https://ino-elektra.nl/hero-elektricien.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Contact INO Techniek en Installatie elektricien Utrecht">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Contact Elektricien Utrecht | INO Techniek">
  <meta name="twitter:description" content="Bel 06 28 76 37 75 of mail info@ino-elektra.nl. 24/7 bereikbaar bij storingen in Utrecht.">
  <meta name="twitter:image" content="https://ino-elektra.nl/hero-elektricien.jpg">
  <link rel="stylesheet" href="style.css?v=6">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Electrician",
    "name": "INO Techniek en Installatie",
    "url": "https://ino-elektra.nl/contact",
    "telephone": "+31628763775",
    "email": "info@ino-elektra.nl",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Utrecht",
      "addressRegion": "Utrecht",
      "addressCountry": "NL"
    },
    "areaServed": ["Utrecht", "Nieuwegein", "Maarssen", "Houten", "IJsselstein", "De Meern", "Vleuten", "Zeist"],
    "openingHoursSpecification": [
      {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "opens": "00:00",
        "closes": "23:59"
      }
    ]
  }
  </script>
</head>
<body>

""" + make_header("contact") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Contact</div>
      <h1>Neem contact op met INO.</h1>
      <p>Bel, app of mail. Kies wat je het prettigst vindt.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Hier vind je alle manieren om INO te bereiken. Bij een storing kun je het beste direct bellen.</span></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <a class="alert-banner" href="tel:+31628763775" style="margin-top:0">
        <div>
          <strong>Storing? Bel direct, 24/7 bereikbaar</strong>
          <span>Geen stroom, kortsluiting of rook uit de meterkast? Bel 06 28 76 37 75, ook 's avonds en in het weekend.</span>
        </div>
        <span class="arrow">→</span>
      </a>
      <div class="service-grid" style="margin-top:26px">
        <a class="service-card" href="tel:+31628763775" style="display:block"><h3>Bellen</h3><p>Direct een vakman aan de lijn.</p><span class="mini-link">06 28 76 37 75 →</span></a>
        <a class="service-card" href="https://wa.me/31628763775" target="_blank" rel="noopener" style="display:block"><h3>WhatsApp</h3><p>Stuur een bericht, eventueel met foto's van je situatie.</p><span class="mini-link">Open WhatsApp →</span></a>
        <a class="service-card" href="mailto:info@ino-elektra.nl" style="display:block"><h3>E-mail</h3><p>Voor vragen die niet met spoed hoeven.</p><span class="mini-link">info@ino-elektra.nl →</span></a>
        <a class="service-card" href="https://www.instagram.com/ino_techniek_en_installatie?stkn=YWEyc2QwcDh6dWNw&amp;utm_source=qr" target="_blank" rel="noopener" style="display:block"><h3>Instagram</h3><p>Bekijk ons werk en volg INO.</p><span class="mini-link">Naar Instagram →</span></a>
        <a class="service-card" href="offerte.html" style="display:block"><h3>Offerte aanvragen</h3><p>Beschrijf je klus en stuur foto's mee.</p><span class="mini-link">Naar het formulier →</span></a>
        <a class="service-card" href="afspraak.html" style="display:block"><h3>Afspraak aanvragen</h3><p>Geef je voorkeursdatum en -tijd door.</p><span class="mini-link">Afspraak plannen →</span></a>
      </div>
    </div>
  </section>

  <section class="section soft">
    <div class="container split-grid">
      <a class="split-card" href="werkgebied.html" style="display:block">
        <h3>Werkgebied</h3>
        <p>Actief in de stad en provincie Utrecht. Bekijk de kaart en of jouw plaats erbij zit.</p>
        <span class="mini-link">Bekijk werkgebied →</span>
      </a>
      <a class="split-card" href="faq.html" style="display:block">
        <h3>Veelgestelde vragen</h3>
        <p>Over tarieven, schouw, garantie en voorrijkosten. Misschien staat je vraag er al bij.</p>
        <span class="mini-link">Bekijk de antwoorden →</span>
      </a>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

print("Pages batch 3 defined")
