# generate_site.py - writes the updated pages without emojis and with all visual/functional improvements
import os
import shutil
from emoji_cleaner import strip_emojis
from build_components import make_header, make_footer

PAGES = {}

# 1. index.html
PAGES["index.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>INO Techniek en Installatie | Elektrotechniek Utrecht</title>
  <meta name="description" content="INO Techniek en Installatie: erkend elektrotechnisch vakman in Utrecht en omstreken. Meterkasten, groepen, elektra, montage en 24/7 storingsdienst.">
  <meta property="og:title" content="INO Techniek en Installatie | Elektrotechniek Utrecht">
  <meta property="og:description" content="INO Techniek en Installatie: erkend elektrotechnisch vakman in Utrecht en omstreken. Meterkasten, groepen, elektra, montage en 24/7 storingsdienst.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/">
  <meta name="google-site-verification" content="xHeZ_iY8KLYVB6SQZzxa5C9qnocjO7YkzjrELzLSXWw">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <link rel="stylesheet" href="style.css?v=6">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Electrician",
    "name": "INO Techniek en Installatie",
    "image": "https://ino-elektra.nl/logo.png",
    "url": "https://ino-elektra.nl/",
    "telephone": "+31628763775",
    "email": "info@ino-elektra.nl",
    "priceRange": "€€",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Utrecht",
      "addressRegion": "Utrecht",
      "addressCountry": "NL"
    },
    "openingHoursSpecification": [
      {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "opens": "00:00",
        "closes": "23:59"
      }
    ],
    "areaServed": ["Utrecht", "Nieuwegein", "IJsselstein", "Maarssen", "Zeist", "Houten", "Vleuten", "De Meern"]
  }
  </script>
</head>
<body>

""" + make_header("") + """

<main id="home">
  <section class="hero">
    <div class="container hero-grid-2col">
      <div>
        <span class="eyebrow">TECHNIEK · INSTALLATIE · INNOVATIE</span>
        <h1>Elektrotechniek die <span>klopt.</span></h1>
        <p class="lead">Van een nieuwe groepenkast tot het opsporen van een storing. INO Techniek en Installatie helpt particulieren en bedrijven in Utrecht en omstreken met nette, veilige en professionele elektrotechnische werkzaamheden — en staat 24/7 klaar bij een storing.</p>
        <div class="hero-actions">
          <a class="btn btn-secondary" href="tel:+31628763775">Bel 06 28 76 37 75</a>
          <a class="btn btn-whatsapp" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag%20over%20een%20elektrotechnische%20klus." target="_blank" rel="noopener">WhatsApp</a>
          <a class="btn btn-primary" href="offerte.html">Offerte aanvragen</a>
          <a class="btn btn-instagram" href="https://www.instagram.com/ino_techniek_en_installatie?stkn=YWEyc2QwcDh6dWNw&amp;utm_source=qr" target="_blank" rel="noopener">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:7px"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>
            Instagram
          </a>
        </div>
        <div class="trust-row">
          <span>✓ Sinds 2021 actief in Utrecht</span>
          <span>✓ NEN 3140 VP</span>
          <span>✓ 24/7 storingsdienst</span>
          <span>✓ 12 mnd garantie op werk</span>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="hero-elektricien.jpg" alt="INO Techniek en Installatie erkend elektricien Utrecht" class="showcase-img" loading="eager" referrerPolicy="no-referrer">
        <div class="hero-badge-floating">Erkend Vakman · NEN 1010 gecertificeerd</div>
      </div>
    </div>
  </section>

  <section class="split-cta">
    <div class="container split-grid">
      <div class="split-card split-urgent">
        <h3>Ik heb nu een storing</h3>
        <p>Bel of app — je krijgt direct een inschatting en bij spoed staan we zo snel mogelijk voor de deur, 24/7.</p>
        <div class="split-actions">
          <a class="btn btn-primary" href="tel:+31628763775">Bel direct</a>
          <a class="btn btn-whatsapp" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20storing%20en%20wil%20graag%20hulp." target="_blank" rel="noopener">WhatsApp</a>
        </div>
      </div>
      <div class="split-card">
        <h3>Ik wil een klus plannen</h3>
        <p>Meterkast, nieuwe groep, verlichting of een verbouwing? Vraag een offerte aan of geef je voorkeursmoment door.</p>
        <div class="split-actions">
          <a class="btn btn-secondary" href="offerte.html">Offerte aanvragen</a>
          <a class="btn btn-secondary" href="afspraak.html">Afspraak aanvragen</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="ontdek">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">ONTDEK INO</span>
        <h2>Alles op een rij.</h2>
        <p>Kies waar je meer over wilt weten. Elke pagina heeft één doel.</p>
      </div>
      <div class="service-grid">
        <article class="service-card"><h3>Diensten</h3><p>Alles wat INO doet, van meterkast tot laadpaal en storing.</p><a href="diensten.html">Bekijk diensten →</a></article>
        <article class="service-card"><h3>Tarieven</h3><p>Uurtarieven, voorrijkosten en vaste prijzen vooraf.</p><a href="tarieven.html">Bekijk tarieven →</a></article>
        <article class="service-card"><h3>Werkwijze</h3><p>Van aanvraag tot oplevering in vier stappen.</p><a href="werkwijze.html">Bekijk werkwijze →</a></article>
        <article class="service-card"><h3>Werkgebied</h3><p>Utrecht en omstreken, met kaart en overzicht per wijk.</p><a href="werkgebied.html">Bekijk werkgebied →</a></article>
        <article class="service-card"><h3>Vakmanschap</h3><p>NEN 1010, NEN 3140 VP en garantie op ons werk.</p><a href="vakmanschap.html">Bekijk vakmanschap →</a></article>
        <article class="service-card"><h3>Reviews</h3><p>Wat klanten op Google over INO zeggen.</p><a href="reviews.html">Lees reviews →</a></article>
        <article class="service-card"><h3>Offerte aanvragen</h3><p>Beschrijf je klus en stuur foto's mee.</p><a href="offerte.html">Offerte aanvragen →</a></article>
        <article class="service-card"><h3>Afspraak aanvragen</h3><p>Geef je voorkeursdatum en -tijd door.</p><a href="afspraak.html">Afspraak plannen →</a></article>
        <article class="service-card"><h3>Veelgestelde vragen</h3><p>Snel antwoord op de meest gestelde vragen.</p><a href="faq.html">Bekijk vragen →</a></article>
      </div>
    </div>
  </section>

  <section class="contact-cta" id="contact">
    <div class="container">
      <span class="eyebrow">INO TECHNIEK EN INSTALLATIE</span>
      <h2>Een elektrische klus?</h2>
      <p>Neem contact op of vraag direct een offerte aan.</p>
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

# 2. diensten.html
PAGES["diensten.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Diensten | INO Techniek en Installatie</title>
  <meta name="description" content="Alle diensten van INO Techniek en Installatie: groepenkast, laadpaal, krachtstroom, perilex, frezen, tuinverlichting en 24/7 storingsdienst in Utrecht.">
  <meta property="og:title" content="Diensten | INO Techniek en Installatie">
  <meta property="og:description" content="Alle diensten van INO Techniek en Installatie: groepenkast, laadpaal, krachtstroom, perilex, frezen, tuinverlichting en 24/7 storingsdienst in Utrecht.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/diensten.html">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("diensten") + """

<main>
  <section class="lp-hero">
    <div class="container">
      <div class="badge">Diensten</div>
      <h1>Van meterkast tot storing.</h1>
      <p>Elektrotechnische werkzaamheden voor woning, bedrijf en verbouwing.</p>
      <div class="page-purpose"><strong>Waarvoor deze pagina?</strong><span>Dit is je startpunt om de juiste dienst te vinden. Kies je klus, lees op de dienstpagina wat het inhoudt en wat het kost, en vraag daarna een offerte aan.</span></div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="service-grid">
        <article class="service-card"><h3>Meterkasten</h3><p>Meterkast vernieuwen, 1-fase en 3-fase kasten met A-merk componenten.</p><a href="groepenkast.html">Bekijk pakketten →</a></article>
        <article class="service-card"><h3>Laadpalen</h3><p>Monteren, verplaatsen of vervangen van laadpalen met dynamic load balancing.</p><a href="laadpaal-installeren.html">Bekijk laadpalen →</a></article>
        <article class="service-card"><h3>Krachtstroom 400V</h3><p>3-fase aansluitingen voor warmtepompen, sauna's, jacuzzi's en machines.</p><a href="krachtstroom-aanleggen.html">Bekijk krachtstroom →</a></article>
        <article class="service-card"><h3>Perilex & Kookgroep</h3><p>Perilex stekker aansluiten of leiding vanaf de meterkast trekken.</p><a href="perilex.html">Bekijk perilex →</a></article>
        <article class="service-card"><h3>Frezen & Stopcontacten</h3><p>Stofarm sleuven frezen met diamantfrees en stopcontacten verleggen.</p><a href="frezen-stopcontacten-verleggen.html">Bekijk tarieven frezen →</a></article>
        <article class="service-card"><h3>Tuinverlichting</h3><p>Grondkabels, waterdichte buitenpunten en tuinspots inclusief herbestrating.</p><a href="tuinverlichting-buitenelektra.html">Bekijk buitenelektra →</a></article>
        <article class="service-card"><h3>24/7 Storingsdienst</h3><p>Direct ter plaatse bij stroomuitval of kortsluiting in regio Utrecht.</p><a href="spoed-elektricien-utrecht.html">Bekijk spoedservice →</a></article>
        <article class="service-card"><h3>Montage & Extra Groepen</h3><p>Nieuwe groepen bijplaatsen (vanaf € 60,-) en schakelmateriaal monteren.</p><a href="offerte.html">Aanvragen →</a></article>
      </div>
    </div>
  </section>

  <section class="section soft">
    <div class="container split-grid">
      <a class="split-card" href="groepenkast.html" style="display:block">
        <h3>Groepenkast vervangen</h3>
        <p>1-fase (1–8 groepen) vanaf € 620, 3-fase (1–8 groepen) vanaf € 720. A-merk componenten, all-in en vaste prijs vooraf.</p>
        <span class="mini-link">Bekijk groepenkast-pakketten →</span>
      </a>
      <a class="split-card" href="perilex.html" style="display:block">
        <h3>Perilex &amp; kookgroep</h3>
        <p>Perilex stekker aansluiten voor € 120, of leiding &amp; kookgroep trekken vanaf € 150. Voor inductie en ventilatie.</p>
        <span class="mini-link">Bekijk perilex-opties →</span>
      </a>
    </div>
    <div class="container">
      <div class="reassurance-band">
        <div>
          <h3>Staat jouw klus er niet tussen?</h3>
          <p>Speciale wensen en maatwerk bespreken we graag. Beschrijf de klus in de <a class="mini-link" style="color:var(--green)" href="offerte.html">offerteaanvraag</a> en je hoort vooraf wat het kost.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">KLUS IN GEDACHTEN?</span>
      <h2>Vraag een vaste prijs aan.</h2>
      <p>Stuur een foto van je situatie mee, dan weet je vooraf wat het kost.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag%20over%20een%20van%20jullie%20diensten." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 3. groepenkast.html
PAGES["groepenkast.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Groepenkast vervangen | INO Techniek en Installatie</title>
  <meta name="description" content="Nieuwe groepenkast plaatsen in Utrecht en omstreken. All-in pakketten vanaf € 620, vaste prijs vooraf. NEN 1010, 12 maanden garantie.">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("groepenkast") + """

<main>
  <section class="section" style="padding-bottom:0">
    <div class="container">
      <p class="form-note" style="margin-bottom:0"><a href="diensten.html" class="mini-link">← Alle diensten</a></p>
    </div>
  </section>

  <section class="section" id="groepenkast">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">GROEPENKAST VERVANGEN</span>
        <h2>Nieuwe groepenkast, vaste prijs vooraf.</h2>
        <p>Oude stoppenkast, te weinig groepen of een kast die niet meer overzichtelijk is? INO vervangt 'm door een moderne, veilige groepenkast — met een vaste prijs die je al kent voordat we beginnen.</p>
      </div>

      <div class="showcase-block" style="margin-bottom: 34px;">
        <div class="hero-image-wrapper">
          <img src="groepenkast-montage.jpg" alt="Vakkundige groepenkast montage Utrecht ABB Hager" class="showcase-img" loading="eager" referrerPolicy="no-referrer">
          <div class="hero-badge-floating">Vakkundige montage · A-merk kasten (ABB / Hager) · NEN 1010 keuring</div>
        </div>
      </div>

      <div class="price-grid package-grid">
        <div class="price-card package-card">
          <h3>1-fase groepenkast</h3>
          <div class="price-amount">vanaf € 620</div>
          <p class="package-meta">1 t/m 8 groepen · All-in</p>
          <p>Ideaal voor appartementen en standaard eengezinswoningen. Inclusief A-merk groepenkast, 1-fase hoofdschakelaar, 2 aardlekschakelaars en complete montage.</p>
          <a class="btn btn-secondary full" href="offerte.html">Dit pakket aanvragen</a>
        </div>
        <div class="price-card package-card highlight">
          <h3>3-fase groepenkast</h3>
          <div class="price-amount">vanaf € 720</div>
          <p class="package-meta">1 t/m 8 groepen · All-in</p>
          <p>Voor woningen met een 3-fase aansluiting, koken op inductie of zwaardere verbruikers. Inclusief 3-fase hoofdschakelaar en aardlekautomaten.</p>
          <a class="btn btn-primary full" href="offerte.html">Dit pakket aanvragen</a>
        </div>
        <div class="price-card package-card">
          <h3>Maatwerk & speciale gevallen</h3>
          <div class="price-amount">In overleg</div>
          <p class="package-meta">Uitbreiding / renovatie</p>
          <p>Meer dan 8 groepen, gedeeltelijke vernieuwingen, verwijderen van oude bedrading of krachtgroepen. Vaste prijs vooraf na beoordeling van je foto's.</p>
          <a class="btn btn-secondary full" href="offerte.html">Situatie aanmelden</a>
        </div>
      </div>
      <p class="form-note price-note">All-in richtprijzen inclusief montage, materiaal en 21% btw. Stuur een foto van je meterkast mee met je aanvraag voor een directe vaste prijs vooraf.</p>

      <div class="addon-block">
        <div class="addon-list">
          <h3>Opties die je kunt bijkiezen</h3>
          <ul class="addon-items">
            <li><span>Extra groep bijplaatsen</span><strong>vanaf + € 60</strong></li>
            <li><span>Kookgroep / Perilex stekker aansluiten</span><strong>+ € 120</strong></li>
            <li><span>Perilex kookgroep trekken vanaf kast</span><strong>vanaf + € 150</strong></li>
            <li><span>Zonnepanelen (PV-groep)</span><strong>+ € 129</strong></li>
            <li><span>Extra aardlekautomaat</span><strong>+ € 120</strong></li>
            <li><span>Beltrafo of DIN-stopcontact</span><strong>vanaf + € 39</strong></li>
          </ul>
        </div>
        <div class="addon-includes">
          <h3>Altijd inbegrepen</h3>
          <ul class="include-items">
            <li>✓ Montage en hoogwaardig A-merk materiaal</li>
            <li>✓ 21% btw</li>
            <li>✓ Oude kast netjes gedemonteerd en afgevoerd</li>
            <li>✓ Getest, doorgemeten en gelabeld</li>
            <li>✓ Alleen A-merken (Hager, ABB, Schneider, Eaton)</li>
            <li>✓ Vaste prijs akkoord vóór we starten</li>
            <li>✓ Garantie op de installatie</li>
          </ul>
          <p class="schouw-note">Liever eerst een fysieke schouw ter plaatse? Dit kost € 90 incl. btw — en verrekenen we volledig zodra je akkoord geeft op de klus. Een foto sturen via WhatsApp of offerte is gratis.</p>
        </div>
      </div>

      <div class="section-heading" style="margin-top:60px">
        <span class="eyebrow">ZO PAKT INO HET AAN</span>
        <h2>Van foto tot geteste kast.</h2>
      </div>
      <div class="steps steps-light">
        <div class="step step-light"><b>01</b><h3>Foto of schouw</h3><p>We bekijken je aansluiting, bedrading, aarding en de ruimte in de meterkast, en geven daarna de definitieve vaste prijs.</p></div>
        <div class="step step-light"><b>02</b><h3>Vervanging volgens NEN 1010</h3><p>We spreken een moment af, halen de oude kast er veilig uit en plaatsen de nieuwe groepenkast met passende beveiliging.</p></div>
        <div class="step step-light"><b>03</b><h3>Getest, gelabeld, opgeruimd</h3><p>Elke groep wordt getest en gelabeld, de oude kast gaat mee, en je krijgt 12 maanden garantie op het werk.</p></div>
      </div>

      <div class="section-heading" style="margin-top:60px">
        <span class="eyebrow">VEELGESTELDE VRAGEN</span>
        <h2>Groepenkast vervangen, uitgelegd.</h2>
      </div>
      <div class="faq">
        <button class="faq-q">Wat kost een nieuwe groepenkast bij INO?<span>+</span></button>
        <div class="faq-a">Een 1-fase groepenkast (1 t/m 8 groepen) vervangen start vanaf € 620 all-in. Een 3-fase groepenkast (1 t/m 8 groepen) start vanaf € 720 all-in. Dit is inclusief A-merk componenten (Hager, ABB, Schneider of Eaton), montage, 21% btw en afvoeren van de oude kast. Bij meer dan 8 groepen of speciale uitbreidingen/renovaties bepalen we de vaste prijs vooraf aan de hand van foto's of een schouw.</div>
        <button class="faq-q">Wat is het verschil tussen een meterkast en een groepenkast?<span>+</span></button>
        <div class="faq-a">De meterkast is de ruimte met de meter en hoofdaansluiting, eigendom van de netbeheerder. De groepenkast is de kast met installatieautomaten en aardlekbeveiliging daarin — die vervangt INO.</div>
        <button class="faq-q">Heb ik 1-fase of 3-fase nodig?<span>+</span></button>
        <div class="faq-a">1-fase past bij de meeste appartementen. 3-fase is vaak nodig bij een laadpaal, warmtepomp of meerdere zware apparaten samen — en alleen zinvol als je aansluiting dat al levert.</div>
        <button class="faq-q">Kan een kookgroep of zonnepanelen-groep er meteen bij?<span>+</span></button>
        <div class="faq-a">Ja, als bijkoopoptie tijdens dezelfde klus. Dat is voordeliger dan een los bezoek later, omdat de kast toch al open is.</div>
        <button class="faq-q">Hoeveel groepen heb ik nodig?<span>+</span></button>
        <div class="faq-a">Meestal 6–8 voor een gemiddelde woning, 10–12 bij grotere woningen met zwaardere apparatuur. Twijfel je? Stuur een foto mee met je aanvraag, dan adviseren we het aantal.</div>
        <button class="faq-q">Welke garantie krijg ik?<span>+</span></button>
        <div class="faq-a">12 maanden garantie op het werk en 2 jaar fabrieksgarantie op materialen, alles volgens de NEN 1010-norm.</div>
      </div>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">GROEPENKAST NODIG?</span>
      <h2>Vraag een vaste prijs aan.</h2>
      <p>Stuur een foto van je huidige meterkast en ontvang een vaste prijs voordat we beginnen.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag%20over%20een%20nieuwe%20groepenkast." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

# 4. perilex.html
PAGES["perilex.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Perilex & kookgroep aansluiten | INO Techniek en Installatie</title>
  <meta name="description" content="Perilex stopcontact of kookgroep aansluiten in Utrecht en omstreken. Vaste prijs vanaf € 120 all-in, geschikt voor inductie en fornuis.">
  <link rel="stylesheet" href="style.css?v=6">
</head>
<body>

""" + make_header("perilex") + """

<main>
  <section class="section" style="padding-bottom:0">
    <div class="container">
      <p class="form-note" style="margin-bottom:0"><a href="diensten.html" class="mini-link">← Alle diensten</a></p>
    </div>
  </section>

  <section class="section soft" id="perilex">
    <div class="container">
      <div class="perilex-intro">
        <div class="section-heading no-margin">
          <span class="eyebrow">PERILEX / KOOKGROEP</span>
          <span class="price-pill">€ 120 all-in, vaste prijs vooraf</span>
          <h2>Perilex of kookgroep aansluiten, vaste prijs vooraf.</h2>
          <p>Overstappen op inductie of een nieuw fornuis? INO sluit je perilex stopcontact of kookgroep veilig aan — met een vaste prijs die je al kent voordat we beginnen.</p>
        </div>
        <div class="perilex-visual hero-image-wrapper" style="padding:0">
          <img src="perilex-inductie.jpg" alt="Perilex inductie kookplaat aansluiting Utrecht" class="showcase-img" loading="eager" referrerPolicy="no-referrer">
          <div class="hero-badge-floating">Vaste all-in prijs: € 120 · NEN 1010</div>
        </div>
      </div>

      <div class="price-grid package-grid">
        <div class="price-card package-card highlight">
          <h3>Perilex stekker aansluiten</h3>
          <div class="price-amount">€ 120</div>
          <p class="package-meta">All-in vaste prijs</p>
          <p>Alleen het aansluiten van de perilex stekker en het apparaat (inductiekookplaat of fornuis) op een al bestaande, werkende perilex wandcontactdoos.</p>
          <ul class="include-items compact">
            <li>✓ Aansluiting & fases doormeten</li>
            <li>✓ Perilex stekker monteren</li>
            <li>✓ Aansluiten volgens fabrikantschema (2-fase of 3-fase)</li>
            <li>✓ Testen op vol vermogen & oplevering</li>
            <li>✓ Garantie op de installatie</li>
          </ul>
          <a class="btn btn-primary full" href="offerte.html">Aanvragen</a>
        </div>
        <div class="price-card package-card">
          <h3>Perilex leiding & groep trekken</h3>
          <div class="price-amount">vanaf € 150</div>
          <p class="package-meta">Vanaf meterkast</p>
          <p>Complete perilex leiding en kabel trekken vanaf de groepenkast naar de keuken of zolder (voor inductie kookplaat of mechanische ventilatie).</p>
          <ul class="include-items compact">
            <li>✓ Bekabeling trekken (loze leiding)</li>
            <li>✓ Perilex wandcontactdoos plaatsen</li>
            <li>✓ Geschikt voor inductie of mechanische ventilatie</li>
            <li>✓ Aansluiting in meterkast / kookgroep</li>
            <li>✓ Doormeten en NEN 1010 oplevercheck</li>
          </ul>
          <p class="schouw-note">Prijs is afhankelijk van leidinglengte en of de aardlekschakelaar/groep al aanwezig is in de kast. Stuur gerust een foto mee!</p>
          <a class="btn btn-secondary full" href="offerte.html">Aanvragen</a>
        </div>
        <div class="price-card package-card">
          <h3>Schouw op locatie?</h3>
          <div class="price-amount">€ 90</div>
          <p class="package-meta">Volledig verrekend bij opdracht</p>
          <p>Wil je dat we vooraf ter plaatse komen kijken naar de kabelroute, doorvoeren en groepenkast? Voor € 90 komen we langs, wat we 100% verrekenen bij uitvoering van de klus.</p>
          <a class="btn btn-secondary full" href="offerte.html">Schouw aanvragen</a>
        </div>
      </div>
      <p class="form-note price-note">Prijzen zijn incl. btw en gelden voor de beschreven standaardsituaties. Bij afwijkende werkzaamheden ontvang je altijd vooraf een prijsvoorstel.</p>

      <div class="addon-block">
        <div class="addon-list">
          <h3>Welke aansluiting heb je nodig?</h3>
          <table class="power-table">
            <thead><tr><th>Aansluitvermogen kookplaat</th><th>Benodigde aansluiting</th></tr></thead>
            <tbody>
              <tr><td>tot 3,7 kW</td><td>Eigen kookgroep 230 V, 16 A</td></tr>
              <tr><td>3,7 – 7,4 kW</td><td>Perilex 2-fase, 400 V</td></tr>
              <tr><td>7,4 – 11 kW</td><td>Perilex 3-fase, 400 V</td></tr>
              <tr><td>meer dan 11 kW / fornuis met oven</td><td>Perilex 3-fase + eigen groep</td></tr>
            </tbody>
          </table>
          <p class="schouw-note">Indicatie. Volg altijd het typeplaatje en aansluitschema van de fabrikant — wij controleren dit bij je thuis.</p>
        </div>
        <div class="addon-includes">
          <h3>2-fase of 3-fase?</h3>
          <p>Bij <strong>2-fase</strong> verdelen we het vermogen over twee fasen — genoeg voor de meeste inductiekookplaten. Bij <strong>3-fase</strong> (krachtstroom) spreiden we de belasting over drie fasen, ideaal voor zware toestellen of meerdere zware apparaten samen.</p>
          <p>Twijfel je of je aansluiting geschikt is, of wil je inductie combineren met een laadpaal? Bekijk dan ook onze <a class="mini-link" href="groepenkast.html">groepenkast-opties →</a>.</p>
        </div>
      </div>

      <div class="section-heading" style="margin-top:60px">
        <span class="eyebrow">ZO PAKT INO HET AAN</span>
        <h2>Van controle tot veilig koken.</h2>
      </div>
      <div class="steps steps-light steps-4">
        <div class="step step-light"><b>01</b><h3>Aansluiting controleren</h3><p>We bekijken je groepenkast, de beschikbare ruimte en het aansluitschema van je kookplaat of fornuis.</p></div>
        <div class="step step-light"><b>02</b><h3>Kabel en groep aanleggen</h3><p>Indien nodig leggen we een nieuwe kookgroep aan en trekken we de bekabeling naar de keuken.</p></div>
        <div class="step step-light"><b>03</b><h3>Perilex monteren</h3><p>We monteren het perilex stopcontact of de vaste aansluiting en sluiten je apparaat aan.</p></div>
        <div class="step step-light"><b>04</b><h3>Testen en opleveren</h3><p>We testen de aansluiting, leveren netjes op en geven garantie op het werk.</p></div>
      </div>

      <div class="section-heading" style="margin-top:60px">
        <span class="eyebrow">VEELGESTELDE VRAGEN</span>
        <h2>Perilex en kookgroep, uitgelegd.</h2>
      </div>
      <div class="faq">
        <button class="faq-q">Wat kost een perilex aansluiten?<span>+</span></button>
        <div class="faq-a">€ 120 all-in bij een bestaande, geschikte groep. Moet er een nieuwe kookgroep bij in de groepenkast, dan begint het vanaf € 275. Beide incl. btw, materiaal en garantie op het werk.</div>
        <button class="faq-q">Wat is het verschil tussen 2-fase en 3-fase?<span>+</span></button>
        <div class="faq-a">Bij 2-fase verdelen we het vermogen over twee fasen, genoeg voor de meeste inductiekookplaten. Bij 3-fase wordt de belasting over drie fasen gespreid — nodig voor zware kookplaten of fornuizen.</div>
        <button class="faq-q">Heb ik perilex nodig voor mijn inductiekookplaat?<span>+</span></button>
        <div class="faq-a">Dat hangt af van het aansluitvermogen op het typeplaatje van je kookplaat. Stuur dat mee met je aanvraag, dan adviseren we welke aansluiting nodig is.</div>
        <button class="faq-q">Kan ik een gewoon stopcontact gebruiken voor inductie?<span>+</span></button>
        <div class="faq-a">Lichtere inductieplaten werken soms op een eigen kookgroep, maar krachtigere modellen vragen om een aparte kookgroep of perilex om overbelasting en een doorslaande groep te voorkomen.</div>
        <button class="faq-q">Moet er een extra groep in de groepenkast komen?<span>+</span></button>
        <div class="faq-a">Vaak wel — een kookgroep krijgt idealiter een eigen groep. Is er geen ruimte meer, dan bekijken we of de groepenkast uitgebreid kan worden.</div>
        <button class="faq-q">Hoe lang duurt het aansluiten?<span>+</span></button>
        <div class="faq-a">Meestal 1 tot 2 uur. Moet er eerst bekabeling naar de meterkast getrokken worden, dan kan het iets langer duren.</div>
      </div>
    </div>
  </section>

  <section class="contact-cta">
    <div class="container">
      <span class="eyebrow">PERILEX OF KOOKGROEP NODIG?</span>
      <h2>Vraag een vaste prijs aan.</h2>
      <p>Stuur het typeplaatje van je kookplaat of fornuis mee, dan weet je vooraf wat het kost.</p>
      <div class="hero-actions">
        <a class="btn btn-light" href="offerte.html">Offerte aanvragen</a>
        <a class="btn btn-outline-light" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        <a class="btn btn-outline-light" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20vraag%20over%20perilex%20of%20een%20kookgroep." target="_blank" rel="noopener">WhatsApp</a>
        <a class="btn btn-outline-light" href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a>
      </div>
    </div>
  </section>
</main>

""" + make_footer() + """
</body>
</html>"""

print("Pages batch 1 defined")
