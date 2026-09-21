# generate_site_part2.py
from build_components import make_header, make_footer

PAGES_PART2 = {}

# 5. laadpaal-installeren.html
PAGES_PART2["laadpaal-installeren.html"] = """<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Laadpaal Installeren Utrecht & Omstreken | INO Elektra</title>
  <meta name="description" content="Professionele laadpaal installatie in Utrecht. Montage, verplaatsen of vervangen van wandladers en laadpalen. 3-fase, dynamic load balancing & schouw op locatie.">
  <meta property="og:title" content="Laadpaal Installeren Utrecht | INO Techniek en Installatie">
  <meta property="og:description" content="Laadpaal monteren, verplaatsen of vervangen in Utrecht en Midden-Nederland. Veilig aangesloten op je groepenkast volgens NEN 1010.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/laadpaal-installeren.html">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="style.css?v=6">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Laadpaal Installatie Utrecht",
    "provider": {
      "@type": "Electrician",
      "name": "INO Techniek en Installatie",
      "telephone": "+31628763775",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Utrecht",
        "addressCountry": "NL"
      }
    },
    "areaServed": "Utrecht en Midden-Nederland",
    "description": "Installatie, vervanging en verplaatsing van elektrische laadpalen en wallboxen met load balancing en veilige groepenkastaansluiting."
  }
  </script>
</head>
<body>

""" + make_header("laadpaal") + """

  <section class="lp-hero">
    <div class="container hero-grid-2col">
      <div>
        <div class="badge">Elektrisch Rijden & Laadoplossingen</div>
        <h1>Laadpaal installeren, verplaatsen of vervangen in Utrecht</h1>
        <p>Heb je zelf een laadpaal aangeschaft of wil je een wallbox laten monteren? Wij zorgen voor de veilige kabelroute vanaf de meterkast, aardlekautomaat, 3-fase aansluiting en Dynamic Load Balancing volgens de NEN 1010 norm.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="offerte.html">Offerte / Schouw aanvragen</a>
          <a class="btn btn-secondary" href="tel:+31628763775">Direct bellen: 06 28 76 37 75</a>
        </div>
        <div class="meta-row">
          <span>✓ Eigen laadpaal laten monteren</span>
          <span>✓ Verplaatsen naar andere plek</span>
          <span>✓ Defecte laadpaal vervangen / ander merk</span>
          <span>✓ Schouw op locatie (€ 90,- verrekend)</span>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="Gemini_Generated_Image_mxhzxsmxhzxsmxhz.jpg" onerror="this.onerror=null; this.src='laadpaal-installatie.jpg';" alt="EV wallbox laadpaal installatie aan gevel Utrecht" class="showcase-img" loading="eager" referrerPolicy="no-referrer">
        <div class="hero-badge-floating">Veilig laden · NEN 1010 · Dynamic Load Balancing</div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">DIENSTEN VOOR LAADPALEN</span>
        <h2>Wat kan INO Techniek voor jouw laadpaal doen?</h2>
        <p>Iedere woning en oprit is anders. Daarom leveren we maatwerk met helder advies vooraf.</p>
      </div>

      <div class="service-grid">
        <div class="service-card">
          <h3>Nieuwe laadpaal monteren & aansluiten</h3>
          <p>Heb je zelf een laadpaal gekocht (zoals Easee, Alfen, Zaptec, Webasto of Wallbox)? Wij trekken de juiste voedingskabel vanaf de groepenkast, plaatsen een geschikte aardlekautomaat en sluiten alles vakkundig aan.</p>
        </div>
        <div class="service-card">
          <h3>Laadpaal verplaatsen</h3>
          <p>Ben je niet tevreden met waar de laadpaal nu zit, of heb je een nieuwe oprit of carport? Wij verlengen of verleggen de bekabeling en monteren de laadpaal op de gewenste nieuwe positie.</p>
        </div>
        <div class="service-card">
          <h3>Laadpaal vervangen of upgraden</h3>
          <p>Is je huidige laadpaal defect of wil je overstappen naar een nieuwer model met slimme functies of Dynamic Load Balancing? Wij demonteren de oude en installeren het nieuwe merk vlekkeloos.</p>
        </div>
        <div class="service-card">
          <h3>Dynamic Load Balancing</h3>
          <p>Voorkom overbelasting van je hoofdzekering als de wasmachine, inductiekookplaat en warmtepomp tegelijk aanstaan. Wij installeren een energiemeter / P1-koppeling die de laadsnelheid automatisch doseert.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section soft">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">TARIEVEN & WERKWIJZE</span>
        <h2>Waarom een schouw op locatie bij een laadpaal?</h2>
        <p>Bij een laadpaal zijn er geen standaard 'one-size-fits-all' prijzen. De situatie bepaalt de werkzaamheden en de kosten.</p>
      </div>

      <div class="price-grid package-grid">
        <div class="price-card package-card highlight">
          <span class="price-card-badge">Aanbevolen</span>
          <h3>Schouw op locatie</h3>
          <div class="price-amount">€ 90<span> incl. btw</span></div>
          <p class="package-meta">Volledig verrekend bij uitvoering</p>
          <p>We komen ter plaatse kijken hoe we de kabel vanaf de meterkast kunnen trekken (via kruipruimte, gevel of straatwerk), meten de meterkastcapaciteit en brengen alle kosten in kaart.</p>
          <ul class="include-items compact">
            <li>✓ Inspectie groepenkast & hoofdaansluiting</li>
            <li>✓ Kabelroute bepalen (minste hak- of breekwerk)</li>
            <li>✓ Controle load balancing mogelijkheid</li>
            <li>✓ Vaste, bindende offerte vooraf</li>
            <li>✓ 100% in mindering gebracht op de montagefactuur</li>
          </ul>
          <a class="btn btn-primary full" href="offerte.html">Schouw aanvragen</a>
        </div>
        <div class="price-card package-card">
          <h3>Vaste prijs vooraf</h3>
          <div class="price-amount">Op maat</div>
          <p class="package-meta">Geen verrassingen achteraf</p>
          <p>Heb je al duidelijke foto's van je meterkast, het traject naar de oprit en de gewenste plek van de laadpaal? Stuur ze mee via ons offerteformulier voor een gerichte prijsindicatie.</p>
          <ul class="include-items compact">
            <li>✓ Geen voorrijkosten in Utrecht</li>
            <li>✓ Alleen A-merk aardlekautomaten</li>
            <li>✓ Inclusief montage en NEN-testmeting</li>
            <li>✓ Garantie op de installatie</li>
          </ul>
          <a class="btn btn-secondary full" href="offerte.html">Offerte opvragen met foto's</a>
        </div>
      </div>

      <div class="faq" style="margin-top:40px">
        <button class="faq-q">Kan elke woning een 3-fase (11 kW) laadpaal aan?<span>+</span></button>
        <div class="faq-a">De meeste nieuwere woningen hebben al een 3-fase aansluiting (3x25A). Heb je nog een 1-fase aansluiting? Dan kun je laden op 1-fase (max 3,7 kW) of een netverzwaring aanvragen bij Stedin. INO kan je groepenkast direct 3-fase gereed maken!</div>
        <button class="faq-q">Wat als ik de laadpaal zelf al heb gekocht?<span>+</span></button>
        <div class="faq-a">Geen enkel probleem! Wij zijn gespecialiseerd in het vakkundig installeren en aansluiten van zelf aangeschafte laadpalen van alle merken.</div>
      </div>
    </div>
  </section>

""" + make_footer() + """
</body>
</html>"""

# 6. krachtstroom-aanleggen.html
PAGES_PART2["krachtstroom-aanleggen.html"] = """<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Krachtstroom Aanleggen Utrecht (3-Fase 400V) | INO Elektra</title>
  <meta name="description" content="Krachtstroom aanleggen in Utrecht en omstreken. 3-fase 400V aansluiting voor warmtepomp, jacuzzi, sauna, tuinhuis of zonnepanelen. Vakkundige berekening kabeldikte & karakteristiek.">
  <meta property="og:title" content="Krachtstroom Aanleggen Utrecht | INO Techniek en Installatie">
  <meta property="og:description" content="Veilig krachtstroom (400V) aanleggen voor zware verbruikers. A-merk componenten, juiste kabeldikte tegen spanningsverlies en NEN 1010 gecertificeerd.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/krachtstroom-aanleggen.html">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="style.css?v=6">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Krachtstroom Aanleggen Utrecht",
    "provider": {
      "@type": "Electrician",
      "name": "INO Techniek en Installatie",
      "telephone": "+31628763775",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Utrecht",
        "addressCountry": "NL"
      }
    },
    "areaServed": "Utrecht en Midden-Nederland",
    "description": "Aanleg van 3-fase krachtgroepen, 400V CEE-contactdozen en zware voedingskabels voor warmtepompen, sauna's, jacuzzi's en machines."
  }
  </script>
</head>
<body>

""" + make_header("krachtstroom") + """

  <section class="lp-hero">
    <div class="container">
      <div class="badge">3-Fase 400V Krachtgroepen</div>
      <h1>Krachtstroom aanleggen in Utrecht & omstreken</h1>
      <p>Heb je zware apparatuur zoals een warmtepomp, jacuzzi, sauna, werkplaatsmachines of een laadpaal? Wij leggen veilige 400V krachtstroom aan met de juiste aardlekautomaat, kabeldikte en NEN 1010 keuring.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="offerte.html">Offerte opvragen met foto's</a>
        <a class="btn btn-secondary" href="tel:+31628763775">Bel direct: 06 28 76 37 75</a>
      </div>
      <div class="meta-row">
        <span>✓ Inspectie kastruimte & faseverdeling</span>
        <span>✓ Juiste kabeldikte tegen spanningsval</span>
        <span>✓ Correcte uitschakelkarakteristiek (B of C)</span>
        <span>✓ Geen voorrijkosten binnen Utrecht</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">TOEPASSINGEN KRACHTSTROOM</span>
        <h2>Waarvoor wordt een 400V krachtgroep aangelegd?</h2>
        <p>Standaard 230V stopcontacten leveren maximaal 3.680 Watt. Voor zwaardere apparatuur is een 3-fase krachtgroep (tot wel 11.000W of meer) noodzakelijk voor veilig gebruik zonder overbelasting.</p>
      </div>

      <div class="service-grid">
        <div class="service-card">
          <h3>Warmtepomp & Hybride systemen</h3>
          <p>Veel all-electric en hybride warmtepompen vragen een eigen 3-fase voeding met werkschakelaar aan de buitenzijde om veilig onderhoud te kunnen plegen.</p>
        </div>
        <div class="service-card">
          <h3>Jacuzzi, Hottub & Sauna</h3>
          <p>Elektrische heaters van jacuzzi's en sauna's vragen continu hoog vermogen. Wij leggen een speciale waterdichte krachtvoeding met separate aardlekbeveiliging aan.</p>
        </div>
        <div class="service-card">
          <h3>Schuur, Tuinhuis & Werkplaats</h3>
          <p>Wil je in je schuur zware machines, een brug, lasapparaat of een onderverdeelkast gebruiken? Wij trekken een zware grondkabel vanaf het hoofdgebouw.</p>
        </div>
        <div class="service-card">
          <h3>Grote PV-installatie (Zonnepanelen)</h3>
          <p>Vanaf ca. 16 panelen of een zwaardere 3-fase omvormer is een 3-fase aansluiting in de groepenkast vereist om netcongestie en uitval te voorkomen.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section soft">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">VAKWERK & BEREKENING</span>
        <h2>Hoe bepalen we de juiste krachtstroom-installatie?</h2>
        <p>Krachtstroom vraagt om nauwkeurige technische berekeningen. Iedere situatie is uniek:</p>
      </div>

      <div class="service-grid">
        <div class="service-card">
          <h3>1. Ruimte en ondersteuning in de meterkast</h3>
          <p>We controleren eerst of je huidige groepenkast al 3-fase is aangesloten en of er fysieke DIN-rail ruimte is voor een 4-polige aardlekautomaat. Indien nodig kunnen we de kast direct uitbreiden.</p>
        </div>
        <div class="service-card">
          <h3>2. De kabelroute & afstand</h3>
          <p>Moet de kabel door de kruipruimte, langs de gevel, via de zolder of door de tuin? De afstand en route bepalen welke type kabel (bijv. YMvK of XMvK-as grondkabel) nodig is.</p>
        </div>
        <div class="service-card">
          <h3>3. Kabeldikte tegen spanningsverlies</h3>
          <p>Bij langere afstanden (bijvoorbeeld naar een tuinhuis of achtertuin) berekenen we exact de benodigde aderdoorsnede (bijv. 2,5mm², 4mm² of 6mm²) zodat de spanning niet inzakt onder belasting.</p>
        </div>
        <div class="service-card">
          <h3>4. Karakteristiek & type stopcontact</h3>
          <p>Apparaten met een hoge inschakelstroom (zoals compressoren of zware pompen) vereisen een C-karakteristiek in plaats van de standaard B-karakteristiek, en een passende rode CEE-contactdoos (16A of 32A).</p>
        </div>
      </div>

      <div class="reassurance-band" style="margin-top:40px">
        <div>
          <h3>Stuur een foto of video mee bij je aanvraag</h3>
          <p>Maak een duidelijke foto van je geopende groepenkast en een foto of kort filmpje van de plek waar de krachtgroep/het stopcontact moet komen. Zo kunnen we direct de situatie analyseren en ontvang je snel een vaste prijs vooraf!</p>
        </div>
      </div>
    </div>
  </section>

""" + make_footer() + """
</body>
</html>"""

# 7. frezen-stopcontacten-verleggen.html
PAGES_PART2["frezen-stopcontacten-verleggen.html"] = """<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sleuven Frezen & Stopcontacten Verleggen Utrecht | INO Elektra</title>
  <meta name="description" content="Stofarm sleuven frezen en stopcontacten verleggen in Utrecht. Prijzen per meter (gips €10, baksteen €15, beton €30) en heldere tarieven per inbouwdoos. Vaste prijs vooraf.">
  <meta property="og:title" content="Sleuven Frezen & Stopcontacten Verleggen Utrecht | INO Techniek">
  <meta property="og:description" content="Professioneel en stofarm sleuven frezen met diamantfrees. Stopcontacten verplaatsen, bijmaken of inbouwen voor keukens en verbouwingen.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/frezen-stopcontacten-verleggen.html">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="style.css?v=6">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Sleuven Frezen en Stopcontacten Verleggen Utrecht",
    "provider": {
      "@type": "Electrician",
      "name": "INO Techniek en Installatie",
      "telephone": "+31628763775",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Utrecht",
        "addressCountry": "NL"
      }
    },
    "areaServed": "Utrecht en Midden-Nederland",
    "description": "Stofarm sleuven frezen in gips, kalkzandsteen, baksteen en beton. Verleggen en bijplaatsen van inbouwdozen en stopcontacten."
  }
  </script>
</head>
<body>

""" + make_header("frezen") + """

  <section class="lp-hero">
    <div class="container hero-grid-2col">
      <div>
        <div class="badge">Stofarm Frezen & Verleggen</div>
        <h1>Sleuven frezen en stopcontacten verleggen in Utrecht</h1>
        <p>Ga je verbouwen, komt er een nieuwe keuken of wil je die loshangende snoeren strak in de muur weggewerkt hebben? Wij frezen professioneel en stofarm met professionele diamantfrezen en industriële stofafzuiging.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="offerte.html">Offerte aanvragen</a>
          <a class="btn btn-secondary" href="tel:+31628763775">Direct bellen: 06 28 76 37 75</a>
        </div>
        <div class="meta-row">
          <span>✓ Stofarm frezen met diamantfrees & afzuiging</span>
          <span>✓ Duidelijke meterprijzen per materiaalsoort</span>
          <span>✓ All-in verleggen per inbouwdoos</span>
          <span>✓ Staffelkorting bij 3+ stopcontacten</span>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="frezen-stopcontacten.jpg" alt="Stofarm sleuven frezen en inbouwdozen boren Utrecht" class="showcase-img" loading="eager" referrerPolicy="no-referrer">
        <div class="hero-badge-floating">Stofarm frezen · Diamantfrees & industriële H-klasse afzuiging</div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">TARIEVEN SLEUVEN FREZEN</span>
        <h2>1. Sleuven frezen per strekkende meter</h2>
        <p>De kosten voor het frezen van sleuven hangen af van de hardheid van de muur. Al onze prijzen zijn inclusief btw en stofarm frezen met diamantgereedschap:</p>
      </div>

      <div class="price-grid">
        <div class="price-card">
          <span class="price-card-badge">Zacht materiaal</span>
          <h3>Gipsblokken / Gasbeton</h3>
          <div class="price-amount">€ 10,00<span>/meter</span></div>
          <p>Licht en relatief zacht materiaal. Snelle verwerking met minimale trillingen voor binnenmuren.</p>
        </div>
        <div class="price-card highlight">
          <span class="price-card-badge">Meest voorkomend</span>
          <h3>Baksteen / Kalkzandsteen</h3>
          <div class="price-amount">€ 15,00<span>/meter</span></div>
          <p>Zachte tot middelharde steensoorten. Wordt strak en stofarm ingeslepen voor flexbuis of installatiebuis.</p>
        </div>
        <div class="price-card">
          <span class="price-card-badge">Zeer hard materiaal</span>
          <h3>Beton / Gewapend beton</h3>
          <div class="price-amount">€ 30,00<span>/meter</span></div>
          <p>Massief beton vraagt zwaardere diamantbladen, hoog vermogen en intensievere bewerking.</p>
        </div>
      </div>
      <p class="form-note price-note">Opmerking: Binnen Utrecht rekenen we € 0,- voorrijkosten. Het dichtmaken (afsmeren of stucen) van de gemaakte sleuven is niet inbegrepen in deze meterprijs (kan in overleg worden meegenomen).</p>
    </div>
  </section>

  <section class="section soft">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">STOPCONTACTEN & SCHAKELAARS</span>
        <h2>2. Stopcontact verleggen of bijplaatsen (totaalprijzen)</h2>
        <p>Compleet verzorgd: inclusief frezen van de sleuf, trekken van nieuwe VD-bedrading, inbouwdoos plaatsen en monteren van het schakelmateriaal.</p>
      </div>

      <div class="price-grid package-grid">
        <div class="price-card package-card">
          <h3>Eenvoudig verleggen / aftakken</h3>
          <div class="price-amount">€ 120,00<span> per punt</span></div>
          <p class="package-meta">Korte afstand vanaf bestaand punt</p>
          <p>Ideaal voor het omhoog of opzij verplaatsen van een stopcontact (bijvoorbeeld achter een hangende tv of naar een nieuw nachtkastje).</p>
          <ul class="include-items compact">
            <li>✓ Sleuf frezen en doos boren</li>
            <li>✓ Inbouwdoos stevig vastzetten</li>
            <li>✓ Bedrading doortrekken & lassen</li>
            <li>✓ Schakelmateriaal afmonteren</li>
          </ul>
          <a class="btn btn-secondary full" href="offerte.html">Aanvragen</a>
        </div>
        <div class="price-card package-card highlight">
          <h3>Nieuwe locatie / Grotere afstand</h3>
          <div class="price-amount">€ 130 – € 250<span> per punt</span></div>
          <p class="package-meta">Langere kabelroute</p>
          <p>Wanneer een stopcontact vanaf een centraaldoos of verdere muur moet worden aangelegd (bijvoorbeeld bij complete keuken- of kamerverbouwingen).</p>
          <ul class="include-items compact">
            <li>✓ Langere sleuf frezen (volgens materiaaltarief)</li>
            <li>✓ Buizen leggen en bedrading trekken</li>
            <li>✓ Nieuwe inbouwdoos infrezen</li>
            <li>✓ Doormeten en gebruiksklaar opleveren</li>
          </ul>
          <a class="btn btn-primary full" href="offerte.html">Aanvragen</a>
        </div>
        <div class="price-card package-card">
          <h3>Speciale varianten & Staffelkorting</h3>
          <div class="price-amount">Korting bij 3+</div>
          <p class="package-meta">Meerdere punten tegelijk</p>
          <p>Wil je spatwaterdichte stopcontacten voor de badkamer/buiten, of stopcontacten met ingebouwde USB-A/C snellader? Dezelfde scherpe basistarieven.</p>
          <ul class="include-items compact">
            <li>✓ <strong>Staffelkorting:</strong> Laat je 3 of meer punten tegelijk doen? Dan daalt de prijs per stuk!</li>
            <li>✓ Keukens volgens nieuw leidinggevend schema</li>
            <li>✓ A-merk schakelmateriaal (Gira, Busch-Jaeger, Jung)</li>
          </ul>
          <a class="btn btn-secondary full" href="offerte.html">Vrijblijvende opgave</a>
        </div>
      </div>
    </div>
  </section>

""" + make_footer() + """
</body>
</html>"""

# 8. tuinverlichting-buitenelektra.html
PAGES_PART2["tuinverlichting-buitenelektra.html"] = """<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tuinverlichting & Buitenelektra Utrecht | INO Elektra</title>
  <meta name="description" content="Professionele tuinverlichting en buitenelektra aanleggen in Utrecht. Grondkabels XMvK-as, waterdichte IP68 verbindingen, tuinpalen en strak herstel van straatwerk.">
  <meta property="og:title" content="Tuinverlichting & Buitenelektra Utrecht | INO Techniek en Installatie">
  <meta property="og:description" content="Veilige buitenelektra en sfeervolle tuinverlichting. Grondkabel aanleg, berekening tegen spanningsverlies en professionele samenwerking met ervaren stratenmakers.">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://ino-elektra.nl/tuinverlichting-buitenelektra.html">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="style.css?v=6">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Tuinverlichting en Buitenelektra Utrecht",
    "provider": {
      "@type": "Electrician",
      "name": "INO Techniek en Installatie",
      "telephone": "+31628763775",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Utrecht",
        "addressCountry": "NL"
      }
    },
    "areaServed": "Utrecht en Midden-Nederland",
    "description": "Aanleg van veilige grondkabels, spatwaterdichte buitenstopcontacten, tuinspots en grondmoffen inclusief vakkundig herstel van bestrating."
  }
  </script>
</head>
<body>

""" + make_header("tuinverlichting") + """

  <section class="lp-hero">
    <div class="container hero-grid-2col">
      <div>
        <div class="badge">Buitenelektra & Tuinverlichting</div>
        <h1>Tuinverlichting en buitenelektra aanleggen in Utrecht</h1>
        <p>Veilige stroom in je tuin voor sfeerverlichting, buitenstopcontacten, vijverpompen of een overkapping. Wij leggen gecertificeerde grondkabels (XMvK-as) aan met 100% waterdichte gietharsmoffen en werken nauw samen met ervaren stratenmakers voor een strak afgewerkte tuin.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="offerte.html">Vrijblijvende offerte aanvragen</a>
          <a class="btn btn-secondary" href="tel:+31628763775">Bel direct: 06 28 76 37 75</a>
        </div>
        <div class="meta-row">
          <span>✓ Gewapende grondkabel (XMvK-as)</span>
          <span>✓ 100% waterdichte IP68 verbindingen</span>
          <span>✓ Berekening kabeldikte tegen spanningsval</span>
          <span>✓ Samenwerking met professionele stratenmakers</span>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="tuinverlichting-buiten.jpg" alt="Sfeervolle tuinverlichting en buitenelektra aanleg Utrecht" class="showcase-img" loading="eager" referrerPolicy="no-referrer">
        <div class="hero-badge-floating">Veilig & sfeervol · IP68 gietharsmoffen · Grondkabel XMvK-as</div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">BUITENELEKTRA DIENSTEN</span>
        <h2>Van subtiele grondspot tot complete tuininstallatie</h2>
        <p>Buitenelektra moet bestand zijn tegen regen, vorst en grondvocht. Wij zorgen voor een installatie waar je tientallen jaren zorgeloos van geniet.</p>
      </div>

      <div class="service-grid">
        <div class="service-card">
          <h3>Sfeerverlichting & Grondspots</h3>
          <p>Staande tuinpalen, wandlampen op schuttingen of verzonken grondspots langs het tuinpad en terras. Schakelbaar vanuit huis, met een app of via een automatische schemerschakelaar.</p>
        </div>
        <div class="service-card">
          <h3>Spatwaterdichte Buitenstopcontacten (IP55/IP66)</h3>
          <p>Handige stroompunten op het terras, bij de barbecue of in het gazon voor de grasmaaier. Netjes en veilig gemonteerd tegen vocht en weersinvloeden.</p>
        </div>
        <div class="service-card">
          <h3>Overkapping, Veranda & Tuinhuis</h3>
          <p>Complete elektra voor je veranda of tuinhuis: inbouwspots in het plafond, heaters, heaterschakelaars, stopcontacten en eventueel een eigen onderverdeelkast.</p>
        </div>
        <div class="service-card">
          <h3>Vijverpompen, Fonteinen & Beregening</h3>
          <p>Betrouwbare en veilige stroomvoorziening voor vijverfilters, UV-lampen en geautomatiseerde beregeningssystemen met separate aardlekbeveiliging.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section soft">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">VAKMANSCHAP & OFFERTE OP MAAT</span>
        <h2>Waarom offerte op maat bij buitenelektra?</h2>
        <p>Bij tuinprojecten zijn vaste standaardprijzen niet eerlijk, omdat elke tuin anders is ingericht:</p>
      </div>

      <div class="service-grid">
        <div class="service-card">
          <h3>Grondsoort & Graafwerk</h3>
          <p>Zandgrond graaft makkelijker dan zware kleigrond of verharde puinlagen onder de oprit. Wij beoordelen vooraf wat nodig is voor de vereiste diepte van 50–60 cm.</p>
        </div>
        <div class="service-card">
          <h3>Professioneel Stratenmakerswerk</h3>
          <p>Moet de kabel onder een strak gelegd terras of klinkers door? Wij werken nauw samen met vakkundige collega-stratenmakers zodat je bestrating weer kaarsrecht en naadloos terugligt.</p>
        </div>
        <div class="service-card">
          <h3>Kabeldikte & Spanningsverlies</h3>
          <p>Bij diepe tuinen (20 tot 50+ meter) treedt spanningsval op als de kabel te dun is. Wij berekenen exact de juiste kabeldikte zodat lampen niet knipperen en pompen op vol vermogen draaien.</p>
        </div>
        <div class="service-card">
          <h3>Eigen Tuin-Aardlekschakelaar</h3>
          <p>Wij sluiten buitenelektra bij voorkeur aan op een aparte aardlekschakelaar in de groepenkast. Zo voorkom je dat bij vocht in een tuinlamp meteen de koelkast in huis uitvalt!</p>
        </div>
      </div>

      <div class="reassurance-band" style="margin-top:40px">
        <div>
          <h3>Vrijblijvend advies en offerte voor jouw tuin</h3>
          <p>Vertel ons je wensen of stuur een schets/foto's van je tuin mee via ons offerteformulier. We denken met je mee en geven vooraf een heldere prijsopgave!</p>
        </div>
      </div>
    </div>
  </section>

""" + make_footer() + """
</body>
</html>"""

# 9. spoed-elektricien-utrecht.html
PAGES_PART2["spoed-elektricien-utrecht.html"] = """<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Spoed Elektricien Utrecht 24/7 | Binnen 60 Min Ter Plaatse | INO Techniek</title>
  <meta name="description" content="Spoed elektricien in Utrecht nodig? INO is 24/7 bereikbaar bij acute stroomstoring, aardlekuitval of kortsluiting. Vaak binnen 60 min ter plaatse. Geen woekertarieven: 06 28 76 37 75.">
  <link rel="canonical" href="https://ino-elektra.nl/spoed-elektricien-utrecht">
  <meta name="robots" content="index, follow">
  <meta property="og:locale" content="nl_NL">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Spoed Elektricien Utrecht 24/7 | Binnen 60 Min Ter Plaatse | INO Techniek">
  <meta property="og:description" content="Acute stroomstoring of kortsluiting in Utrecht? 24/7 bereikbaar, NEN 3140 erkend en vaak binnen 60 minuten ter plaatse. Vaste all-in tarieven zonder verrassingen.">
  <meta property="og:url" content="https://ino-elektra.nl/spoed-elektricien-utrecht">
  <meta property="og:site_name" content="INO Techniek en Installatie">
  <meta property="og:image" content="https://ino-elektra.nl/hero-elektricien.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Spoed elektricien storingsdienst Utrecht INO Techniek">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Spoed Elektricien Utrecht 24/7 | INO Techniek">
  <meta name="twitter:description" content="24/7 storingsdienst bij stroomuitval en kortsluiting in Utrecht en omstreken. Bel direct 06 28 76 37 75.">
  <meta name="twitter:image" content="https://ino-elektra.nl/hero-elektricien.jpg">
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="style.css?v=6">
  
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": ["Electrician", "EmergencyService"],
        "@id": "https://ino-elektra.nl/spoed-elektricien-utrecht#service",
        "name": "Spoed Elektricien Utrecht 24/7 - INO Techniek en Installatie",
        "url": "https://ino-elektra.nl/spoed-elektricien-utrecht",
        "telephone": "+31628763775",
        "priceRange": "€ 90 - € 145",
        "image": "https://ino-elektra.nl/storingsdienst-meting.jpg",
        "description": "24/7 spoed elektricien en storingsdienst in Utrecht en omliggende gemeenten. Direct hulp bij stroomstoringen, aardlekautomaten en kortsluiting. Binnen 60 minuten ter plaatse.",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Utrecht",
          "addressRegion": "Utrecht",
          "addressCountry": "NL"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 52.0907,
          "longitude": 5.1214
        },
        "areaServed": [
          {"@type": "City", "name": "Utrecht"},
          {"@type": "City", "name": "Nieuwegein"},
          {"@type": "City", "name": "Maarssen"},
          {"@type": "City", "name": "Houten"},
          {"@type": "City", "name": "IJsselstein"},
          {"@type": "City", "name": "De Meern"},
          {"@type": "City", "name": "Vleuten"},
          {"@type": "City", "name": "Zeist"}
        ],
        "openingHoursSpecification": [
          {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "opens": "00:00",
            "closes": "23:59"
          }
        ]
      },
      {
        "@type": "FAQPage",
        "@id": "https://ino-elektra.nl/spoed-elektricien-utrecht#faq",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Kan ik jullie echt 24/7 en midden in de nacht bellen bij een stroomstoring?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Ja. Onze storingsdienst is 24 uur per dag, 7 dagen per week bemand voor acute storingen in Utrecht en omstreken. Je krijgt direct een ervaren elektricien aan de lijn, geen extern callcenter."
            }
          },
          {
            "@type": "Question",
            "name": "Wat als het probleem niet binnen het eerste uur is opgelost?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "In ruim 85% van de gevallen lossen we de storing binnen het eerste uur op. Is er meer tijd of een specifiek vervangend onderdeel nodig? We stoppen altijd eerst en bespreken de situatie en exacte meerkosten met jou vóórdat we verder gaan. Je betaalt daarna transparant per kwartier."
            }
          },
          {
            "@type": "Question",
            "name": "Krijg ik garantie op de uitgevoerde spoedreparatie (NEN 1010 / NEN 3140)?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Jazeker. Al onze noodreparaties en gemonteerde materialen worden uitgevoerd volgens de geldende NEN 1010 en NEN 3140 normen. Je ontvangt 12 maanden garantie op het geleverde werk en de gebruikte A-merk onderdelen."
            }
          },
          {
            "@type": "Question",
            "name": "Hoe weet ik zeker of de storing in mijn eigen woning zit of bij Stedin?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Controleer of de buren en de straatverlichting wel stroom hebben. Hebben zij wel stroom? Dan zit het probleem in je eigen installatie en helpen wij je direct. Zit de hele straat zonder stroom? Dan is het een netstoring en bel je het gratis Nationaal Storingsnummer (0800-9009) voor Stedin om onnodige voorrijkosten te voorkomen."
            }
          },
          {
            "@type": "Question",
            "name": "Rekenen jullie voorrijkosten binnen de gemeente Utrecht?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Nee, binnen Utrecht rekenen wij geen voorrijkosten. Je betaalt uitsluitend het vooraf afgesproken all-in uurtarief inclusief btw en diagnose."
            }
          },
          {
            "@type": "Question",
            "name": "Hoe kan ik betalen bij een spoedklus?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Je kunt na afronding en controle eenvoudig betalen via een digitaal betaalverzoek (bijv. Tikkie of iDEAL), per bankoverschrijving of contant. Je ontvangt direct een officiële factuur per e-mail met specificatie voor je administratie of verzekering."
            }
          }
        ]
      }
    ]
  }
  </script>

  <style>
    /* Scoped Emergency CRO Landing Page Styles */
    .lp-header{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.98);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
    .lp-header .nav-wrap{height:76px;display:flex;align-items:center;justify-content:space-between}
    .lp-header-right{display:flex;align-items:center;gap:12px}
    .lp-status-pill{display:inline-flex;align-items:center;gap:7px;background:#eef8eb;color:var(--green-dark);border:1px solid #cce8c5;padding:6px 12px;border-radius:999px;font-size:12px;font-weight:700}
    .lp-status-dot{width:8px;height:8px;border-radius:50%;background:#22c55e;box-shadow:0 0 0 3px rgba(34,197,94,.25);animation:lp-pulse 1.8s infinite}
    @keyframes lp-pulse{0%{transform:scale(0.95);box-shadow:0 0 0 0 rgba(34,197,94,.7)}70%{transform:scale(1);box-shadow:0 0 0 6px rgba(34,197,94,0)}100%{transform:scale(0.95);box-shadow:0 0 0 0 rgba(34,197,94,0)}}
    .lp-call-btn{display:inline-flex;align-items:center;gap:8px;background:var(--green);color:#10220d;padding:11px 18px;border-radius:10px;font-weight:800;font-size:14px;transition:background .15s}
    .lp-call-btn:hover{background:#58c63b}

    .spoed-hero{padding:48px 0 36px;background:linear-gradient(135deg,#fbfdfb 0%,#f1f8ef 50%,#eaf4fc 100%);border-bottom:1px solid var(--line)}
    .spoed-badge{display:inline-flex;align-items:center;gap:8px;background:#101712;color:#fff;padding:7px 14px;border-radius:999px;font-size:12px;font-weight:800;letter-spacing:.5px;margin-bottom:16px}
    .spoed-badge .green-dot{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 8px var(--green)}
    .spoed-hero h1{font-size:clamp(32px,4.8vw,52px);line-height:1.08;letter-spacing:-1.8px;margin:8px 0 16px;color:#111827}
    .spoed-hero .lead{font-size:17px;line-height:1.6;color:#4b5563;margin-bottom:24px}

    .spoed-cta-box{display:flex;flex-direction:column;gap:12px;max-width:520px;margin:24px 0}
    .btn-spoed-primary{display:flex;align-items:center;justify-content:center;gap:12px;background:var(--green);color:#10220d;padding:18px 24px;border-radius:14px;font-weight:800;font-size:20px;text-align:center;box-shadow:0 12px 28px rgba(39,138,29,.25);transition:transform .15s, background .15s;min-height:60px}
    .btn-spoed-primary:hover{background:#58c63b;transform:translateY(-2px)}
    .btn-spoed-whatsapp{display:flex;align-items:center;justify-content:center;gap:12px;background:#25d366;color:#ffffff;padding:16px 22px;border-radius:14px;font-weight:800;font-size:16px;text-align:center;box-shadow:0 8px 20px rgba(37,211,102,.25);transition:transform .15s, background .15s;min-height:54px}
    .btn-spoed-whatsapp:hover{background:#20ba5a;transform:translateY(-2px)}
    .btn-spoed-whatsapp svg, .btn-spoed-primary svg{flex-shrink:0}

    .spoed-trust-row{display:grid;grid-template-columns:repeat(2,1fr);gap:10px 16px;font-size:13px;font-weight:700;color:#374151;margin-top:20px}
    .spoed-trust-row span{display:flex;align-items:center;gap:8px}
    .spoed-trust-row svg{color:var(--green-dark);flex-shrink:0}

    /* Anti-Malafide Reassurance Banner */
    .anti-malafide-strip{background:#111a14;color:#fff;padding:26px 0;border-bottom:1px solid rgba(255,255,255,.08)}
    .anti-malafide-grid{display:grid;grid-template-columns:auto 1fr;gap:24px;align-items:center}
    .anti-shield-icon{width:52px;height:52px;border-radius:14px;background:rgba(107,211,77,.14);border:1px solid rgba(107,211,77,.3);display:flex;align-items:center;justify-content:center;color:var(--green)}
    .anti-malafide-text h3{margin:0 0 4px;font-size:18px;color:#fff}
    .anti-malafide-text p{margin:0;font-size:14px;color:#c7d0ca;line-height:1.5}
    .anti-malafide-pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
    .anti-malafide-pills span{background:rgba(255,255,255,.08);padding:4px 10px;border-radius:6px;font-size:12px;font-weight:700;color:#e1e7e2}

    /* Triage Section: Spoed-Check in 30 Seconden */
    .triage-section{padding:70px 0;background:#fff}
    .triage-heading{text-align:center;max-width:760px;margin:0 auto 44px}
    .triage-heading h2{margin:8px 0 12px}
    .triage-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
    .triage-card{border:1px solid var(--line);border-radius:18px;background:#fff;padding:24px 20px;display:flex;flex-direction:column;position:relative;transition:transform .15s, box-shadow .15s}
    .triage-card:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(0,0,0,.06)}
    
    .triage-card.danger{border-top:4px solid #dc2626;background:linear-gradient(180deg,#fff9f9 0%,#ffffff 45%)}
    .triage-card.warning{border-top:4px solid #f59e0b;background:linear-gradient(180deg,#fffdf5 0%,#ffffff 45%)}
    .triage-card.internal{border-top:4px solid #0284c7;background:linear-gradient(180deg,#f5fbff 0%,#ffffff 45%)}
    .triage-card.grid{border-top:4px solid #64748b;background:linear-gradient(180deg,#f8fafc 0%,#ffffff 45%)}

    .triage-badge{display:inline-block;align-self:flex-start;font-size:11px;font-weight:800;letter-spacing:.5px;padding:4px 9px;border-radius:6px;text-transform:uppercase;margin-bottom:12px}
    .danger .triage-badge{background:#fee2e2;color:#991b1b}
    .warning .triage-badge{background:#fef3c7;color:#92400e}
    .internal .triage-badge{background:#e0f2fe;color:#075985}
    .grid .triage-badge{background:#f1f5f9;color:#334155}

    .triage-title{font-size:17px;font-weight:800;margin:0 0 10px;line-height:1.25}
    .triage-steps{list-style:none;margin:0 0 20px;padding:0;display:grid;gap:10px;font-size:13px;line-height:1.45;color:#4b5563;flex:1}
    .triage-steps li{position:relative;padding-left:22px}
    .triage-steps li::before{content:counter(item);counter-increment:item;position:absolute;left:0;top:0;width:16px;height:16px;border-radius:50%;background:#e5e7eb;font-size:10px;font-weight:800;color:#374151;display:flex;align-items:center;justify-content:center}
    .triage-steps{counter-reset:item}
    .danger .triage-steps li strong{color:#991b1b}
    
    .triage-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:12px 14px;border-radius:10px;font-weight:800;font-size:13px;text-align:center;text-decoration:none;transition:background .15s}
    .danger .triage-btn{background:#dc2626;color:#fff}
    .danger .triage-btn:hover{background:#b91c1c}
    .warning .triage-btn{background:var(--green);color:#10220d}
    .warning .triage-btn:hover{background:#58c63b}
    .internal .triage-btn{background:#0284c7;color:#fff}
    .internal .triage-btn:hover{background:#0369a1}
    .grid .triage-btn{background:#475569;color:#fff}
    .grid .triage-btn:hover{background:#334155}

    /* Response Time Table */
    .responstijd-section{padding:70px 0;background:var(--soft);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
    .responstijd-wrap{background:#fff;border:1px solid var(--line);border-radius:20px;padding:32px;box-shadow:0 14px 40px rgba(22,46,29,.05)}
    .table-container{overflow-x:auto;margin:20px 0}
    .responstijd-table{width:100%;border-collapse:collapse;font-size:14px;text-align:left}
    .responstijd-table th{background:#f8faf8;padding:14px 16px;font-weight:800;font-size:12px;text-transform:uppercase;letter-spacing:.6px;color:#374151;border-bottom:2px solid var(--line)}
    .responstijd-table td{padding:16px;border-bottom:1px solid var(--line);vertical-align:middle}
    .responstijd-table tr:hover td{background:#fafdf9}
    .time-badge{display:inline-flex;align-items:center;gap:6px;background:#eafbe6;color:var(--green-dark);font-weight:800;font-size:13px;padding:6px 12px;border-radius:8px;border:1px solid #c7edba;white-space:nowrap}
    .status-ok{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:700;color:var(--green-dark)}

    /* Pricing Section & No-Surprise Guarantee */
    .spoed-pricing-section{padding:75px 0;background:#fff}
    .spoed-pricing-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:30px}
    .spoed-price-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:28px 24px;display:flex;flex-direction:column;position:relative}
    .spoed-price-card.featured{border:2px solid var(--green);background:linear-gradient(180deg,#f7fdf5 0%,#ffffff 40%);box-shadow:0 12px 36px rgba(107,211,77,.15)}
    .spoed-price-badge{display:inline-block;align-self:flex-start;background:#eef8eb;color:var(--green-dark);font-weight:800;font-size:11px;padding:4px 8px;border-radius:6px;text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px}
    .spoed-price-tag{font-size:38px;font-weight:800;letter-spacing:-1.5px;color:var(--ink);margin:8px 0 4px}
    .spoed-price-tag span{font-size:15px;font-weight:600;color:var(--muted);letter-spacing:normal}
    .spoed-price-card p{font-size:13px;color:var(--muted);margin:0 0 16px}
    .spoed-price-list{list-style:none;margin:0 0 20px;padding:0;display:grid;gap:8px;font-size:13px;font-weight:600;color:#374151}
    .spoed-price-list li{display:flex;align-items:center;gap:8px}
    .spoed-price-list svg{color:var(--green-dark);flex-shrink:0}

    .no-surprise-box{background:#111a14;color:#fff;border-radius:18px;padding:32px;display:grid;grid-template-columns:auto 1fr auto;gap:26px;align-items:center}
    .no-surprise-icon{width:56px;height:56px;border-radius:14px;background:rgba(107,211,77,.18);display:flex;align-items:center;justify-content:center;color:var(--green)}
    .no-surprise-box h3{margin:0 0 6px;font-size:20px;color:#fff}
    .no-surprise-box p{margin:0;font-size:14px;color:#c7d0ca;line-height:1.55}

    /* FAQ Section */
    .spoed-faq-section{padding:75px 0;background:var(--soft);border-top:1px solid var(--line)}
    .faq-container{max-width:840px;margin:0 auto}

    /* Floating Mobile Emergency Bar */
    .mobile-bar-emergency{display:none}
    @media(max-width:768px){
      body{padding-bottom:76px}
      .mobile-bar-emergency{position:fixed;bottom:0;left:0;right:0;z-index:9999;display:grid;grid-template-columns:1.2fr .8fr;height:64px;box-shadow:0 -4px 20px rgba(0,0,0,.22);background:#0f172a}
      .m-btn-call{background:#15803d;color:#fff;display:flex;align-items:center;justify-content:center;gap:8px;font-size:15px;font-weight:800;text-decoration:none;border-right:1px solid rgba(255,255,255,.15);padding:0 12px;min-height:48px}
      .m-btn-whatsapp{background:#25d366;color:#fff;display:flex;align-items:center;justify-content:center;gap:8px;font-size:14px;font-weight:800;text-decoration:none;padding:0 12px;min-height:48px}
      .triage-grid{grid-template-columns:1fr}
      .spoed-pricing-grid{grid-template-columns:1fr}
      .anti-malafide-grid{grid-template-columns:1fr}
      .no-surprise-box{grid-template-columns:1fr;text-align:left}
      .spoed-trust-row{grid-template-columns:1fr}
      .lp-header-right .lp-status-pill{display:none}
    }
    @media(min-width:769px) and (max-width:1024px){
      .triage-grid{grid-template-columns:repeat(2,1fr)}
    }
  </style>
</head>
<body>

<header class="lp-header">
  <div class="container nav-wrap">
    <a class="brand" href="index.html" aria-label="INO Techniek en Installatie Home">
      <img src="logo.png" alt="INO Techniek en Installatie logo" width="160" height="42">
    </a>
    <div class="lp-header-right">
      <div class="lp-status-pill">
        <span class="lp-status-dot"></span> 24/7 Storingsdienst Actief
      </div>
      <a class="lp-call-btn" href="tel:+31628763775" aria-label="Bel direct 06 28 76 37 75">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        06 28 76 37 75
      </a>
    </div>
  </div>
</header>

<main>
  <!-- 1. Hero & Dual Prominent CTA -->
  <section class="spoed-hero">
    <div class="container hero-grid-2col">
      <div>
        <div class="spoed-badge">
          <span class="green-dot"></span> 24/7 BEREIKBAAR IN UTRECHT &amp; OMSTREKEN · VAAK BINNEN 60 MINUTEN TER PLAATSE
        </div>
        <h1>Spoed Elektricien in Utrecht Nodig? Direct een Erkend Vakman Ter Plaatse.</h1>
        <p class="lead">Acuut stroomuitval, een doorgeslagen aardlekschakelaar of brandlucht uit de meterkast? INO Techniek staat dag en nacht direct paraat. <strong>Geen anoniem callcenter of tussenpartij</strong>, maar direct telefonisch contact met een NEN 3140 gecertificeerd elektricien.</p>

        <div class="spoed-cta-box">
          <a class="btn-spoed-primary" href="tel:+31628763775" id="heroCallBtn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            Bel Direct: 06 28 76 37 75
          </a>
          <a class="btn-spoed-whatsapp" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20nu%20een%20stroomstoring%20in%20Utrecht%20en%20stuur%20hierbij%20een%20foto%20van%20de%20meterkast%20voor%20beoordeling." target="_blank" rel="noopener" id="heroWhatsAppBtn">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
            WhatsApp met Foto (Snelle Beoordeling Meterkast)
          </a>
        </div>

        <div class="spoed-trust-row">
          <span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
            Gemiddeld binnen 30 - 60 min ter plaatse
          </span>
          <span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
            Geen voorrijkosten binnen Utrecht
          </span>
          <span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
            NEN 3140 VP &amp; NEN 1010 gecertificeerd
          </span>
          <span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>
            Vaste prijsafspraak vóór we beginnen
          </span>
        </div>
      </div>

      <div class="hero-image-wrapper">
        <img src="storingsdienst-meting.jpg" alt="Storingsdienst elektricien Utrecht meting aardlekschakelaar multimeter" class="showcase-img" loading="eager" width="540" height="380" referrerPolicy="no-referrer">
        <div class="hero-badge-floating">Erkend Installateur · Directe Foutmeting &amp; Veilig Herstel</div>
      </div>
    </div>
  </section>

  <!-- Reassurance / Anti-Scam Banner -->
  <section class="anti-malafide-strip">
    <div class="container anti-malafide-grid">
      <div class="anti-shield-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
      </div>
      <div class="anti-malafide-text">
        <h3>Pas op voor malafide callcenters en woekertarieven</h3>
        <p>In de spoedmarkt zijn veel louche tussenpersonen actief die via landelijke callcenters torenhoge rekeningen van honderden euro's uitschrijven. <strong>INO Techniek is een lokaal Utrechts familiebedrijf met KvK-inschrijving en een vaste werkplaats.</strong> Je spreekt direct de monteur die zelf in de bus stapt.</p>
        <div class="anti-malafide-pills">
          <span>KvK Geregistreerd</span>
          <span>Geen Tussenbureau</span>
          <span>Eerlijke All-in Tarieven</span>
          <span>12 Mnd Garantie</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. Interactive 30-Second Emergency Triage (Paniek-reductie) -->
  <section class="triage-section" id="spoed-check">
    <div class="container">
      <div class="triage-heading">
        <span class="eyebrow">PANIEK-REDUCTIE &amp; STAPPENPLAN</span>
        <h2>Spoed-Check in 30 Seconden: Wat is jouw situatie?</h2>
        <p class="lead">Blijf rustig en volg onderstaand advies voor jouw specifieke storing om direct gevaar af te wenden en onnodige kosten te voorkomen.</p>
      </div>

      <div class="triage-grid">
        <!-- Situatie 1 -->
        <article class="triage-card danger" id="situatie-acuut">
          <span class="triage-badge">Situatie 1 · Acuut Gevaar</span>
          <h3 class="triage-title">Rook, brandlucht of vonken uit de meterkast</h3>
          <ul class="triage-steps">
            <li>Schakel direct de <strong>hoofdschakelaar</strong> in de meterkast uit (naar beneden).</li>
            <li>Blijf op veilige afstand en houd de meterkastdeur gesloten.</li>
            <li>Bel bij actieve vlammen of aanhoudende rook direct <strong>112</strong>.</li>
            <li>Bel daarna direct onze spoeddienst voor noodherstel en veilige inspectie.</li>
          </ul>
          <a class="triage-btn" href="tel:+31628763775">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            Bel Direct Spoedmonteur
          </a>
        </article>

        <!-- Situatie 2 -->
        <article class="triage-card warning" id="situatie-kortsluiting">
          <span class="triage-badge">Situatie 2 · Kortsluiting</span>
          <h3 class="triage-title">Aardlek of automaat klapt er telkens uit</h3>
          <ul class="triage-steps">
            <li>Koppel alle aangesloten apparaten op die specifieke groep los (stekkers eruit).</li>
            <li>Zet de aardlekschakelaar éénmalig rustig weer omhoog.</li>
            <li>Blijft hij uitvallen? <strong>Niet forceren of vasthouden</strong> (gevaar voor oververhitting).</li>
            <li>Bel ons: wij meten de leidingen en componenten door met een isolatieweerstandsmeter.</li>
          </ul>
          <a class="triage-btn" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20mijn%20aardlekschakelaar%20valt%20steeds%20uit.%20Hierbij%20een%20foto%20van%20de%20groepenkast." target="_blank" rel="noopener">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
            Stuur Foto van Meterkast
          </a>
        </article>

        <!-- Situatie 3 -->
        <article class="triage-card internal" id="situatie-binnenshuis">
          <span class="triage-badge">Situatie 3 · Binnenshuis</span>
          <h3 class="triage-title">Alleen jouw woning donker (buren hebben stroom)</h3>
          <ul class="triage-steps">
            <li>Kijk naar buiten: branden lantaarnpalen en hebben buren wel gewoon licht?</li>
            <li>Controleer of de hoofdschakelaar of aardlekautomaat naar beneden staat.</li>
            <li>Staan alle schakelaars omhoog maar heb je toch geen stroom? Mogelijk een hoofdzekering defect.</li>
            <li>Het probleem zit in je eigen installatie; bel direct onze storingsdienst.</li>
          </ul>
          <a class="triage-btn" href="tel:+31628763775">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            Bel Storingsmonteur
          </a>
        </article>

        <!-- Situatie 4 -->
        <article class="triage-card grid" id="situatie-netbeheerder">
          <span class="triage-badge">Situatie 4 · Netbeheerder</span>
          <h3 class="triage-title">Hele straat of buurt zit zonder stroom</h3>
          <ul class="triage-steps">
            <li>Zitten ook de buren en straatverlichting zonder stroom?</li>
            <li>Dan is er sprake van een netstoring in het openbare netwerk van Stedin.</li>
            <li>Een elektricien kan dit netwerk niet openen; Stedin herstelt de straatkabel.</li>
            <li>Bel het gratis Nationaal Storingsnummer (0800-9009) om voorrijkosten te voorkomen.</li>
          </ul>
          <a class="triage-btn" href="tel:08009009">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
            Bel Stedin: 0800-9009
          </a>
        </article>
      </div>
    </div>
  </section>

  <!-- 3. Local Social Proof & Utrecht Response Times Table -->
  <section class="responstijd-section" id="wijken">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">UTRECHT &amp; REGIO AANRIJTIJDEN</span>
        <h2>Gemiddelde Aanrijtijden in Utrecht &amp; Randgemeenten</h2>
        <p class="lead">Doordat onze storingsdienst lokaal gevestigd is in Utrecht en onze bussen strategisch onderweg zijn, zijn we snel bij je ter plaatse. Direct contact met de monteur, géén anoniem tussenbureau.</p>
      </div>

      <div class="responstijd-wrap">
        <div class="table-container">
          <table class="responstijd-table" aria-label="Aanrijtijden per wijk in Utrecht">
            <thead>
              <tr>
                <th>Wijk / Gebied</th>
                <th>Verwachte Aanrijtijd</th>
                <th>Bekende Buurten &amp; Postcodes</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Utrecht Binnenstad, Oost &amp; De Uithof</strong></td>
                <td><span class="time-badge">20 – 35 min</span></td>
                <td>Binnenstad, Oudwijk, Wittevrouwen, Schildersbuurt, Science Park (3584, 3512, 3581)</td>
                <td><span class="status-ok">● Direct Beschikbaar</span></td>
              </tr>
              <tr>
                <td><strong>Leidsche Rijn &amp; Vleuten-De Meern</strong></td>
                <td><span class="time-badge">25 – 45 min</span></td>
                <td>Leidsche Rijn Centrum, Terwijde, Parkwijk, Het Zand, Vleuterweide (3544, 3543, 3451)</td>
                <td><span class="status-ok">● Direct Beschikbaar</span></td>
              </tr>
              <tr>
                <td><strong>Overvecht, Zuilen &amp; Noord</strong></td>
                <td><span class="time-badge">20 – 40 min</span></td>
                <td>Overvecht-Noord/Zuid, Zuilen, Ondiep, Pijlsweerd, Tuindorp (3561, 3562, 3553)</td>
                <td><span class="status-ok">● Direct Beschikbaar</span></td>
              </tr>
              <tr>
                <td><strong>Kanaleneiland, Lombok &amp; Zuid</strong></td>
                <td><span class="time-badge">20 – 35 min</span></td>
                <td>Lombok, Oog in Al, Kanaleneiland, Rivierenwijk, Hoograven, Lunetten (3531, 3526, 3523)</td>
                <td><span class="status-ok">● Direct Beschikbaar</span></td>
              </tr>
              <tr>
                <td><strong>Randgemeenten: Nieuwegein, Maarssen, IJsselstein &amp; Zeist</strong></td>
                <td><span class="time-badge">30 – 50 min</span></td>
                <td>Nieuwegein, Maarssen-Dorp/Broek, IJsselstein, Zeist, Houten, De Bilt</td>
                <td><span class="status-ok">● Direct Beschikbaar</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;margin-top:14px">
          <small style="color:var(--muted)">* Aanrijtijden zijn indicatief en afhankelijk van het actuele verkeer op de ring Utrecht (A2, A12, A27).</small>
          <a class="btn btn-primary" href="tel:+31628763775" style="padding:10px 18px;font-size:13px">Check Direct Beschikbaarheid</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. Transparent Pricing & No-Surprise Price Guarantee -->
  <section class="spoed-pricing-section" id="tarieven">
    <div class="container">
      <div class="section-heading">
        <span class="eyebrow">100% TRANSPARANTE TARIEVEN</span>
        <h2>Geen Woekertarieven: Altijd Eerlijke Prijzen Vooraf</h2>
        <p class="lead">Wij hanteren duidelijke all-in tarieven inclusief btw en diagnose binnen Utrecht. Geen onverwachte 'nachttoeslagen' van honderden euro's achteraf.</p>
      </div>

      <div class="spoed-pricing-grid">
        <!-- Tarief 1: Overdag -->
        <div class="spoed-price-card">
          <span class="spoed-price-badge">Overdag · Kantooruren</span>
          <h3>Maandag t/m Vrijdag</h3>
          <div class="spoed-price-tag">€ 90,- <span>all-in (1e uur)</span></div>
          <p>Tussen 08:00 en 18:00 uur. Inclusief btw, diagnose en reparatietijd.</p>
          <ul class="spoed-price-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Geen voorrijkosten binnen Utrecht</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Inclusief professionele foutmeting</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Vervolgwerk: € 22,50 per kwartier</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Betalen via betaalverzoek of factuur</li>
          </ul>
          <a class="btn btn-secondary full" href="tel:+31628763775">Bel 06 28 76 37 75</a>
        </div>

        <!-- Tarief 2: Avond & Zaterdag -->
        <div class="spoed-price-card featured">
          <span class="spoed-price-badge" style="background:#dcfce7;color:#166534">Avond &amp; Zaterdag</span>
          <h3>18:00 – 22:00 &amp; Zaterdag</h3>
          <div class="spoed-price-tag">€ 120,- <span>all-in (1e uur)</span></div>
          <p>Buiten reguliere kantooruren. Snelle interventie bij avondstoringen.</p>
          <ul class="spoed-price-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Geen voorrijkosten binnen Utrecht</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Spoedopkomst binnen 60 minuten</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Vervolgwerk: € 30,00 per kwartier</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> NEN 3140 veilige noodoplossing</li>
          </ul>
          <a class="btn btn-primary full" href="tel:+31628763775">Bel Direct Storingsdienst</a>
        </div>

        <!-- Tarief 3: Nacht & Zondag -->
        <div class="spoed-price-card">
          <span class="spoed-price-badge">Nacht &amp; Zondag</span>
          <h3>22:00 – 08:00 &amp; Zondagen</h3>
          <div class="spoed-price-tag">€ 145,- <span>all-in (1e uur)</span></div>
          <p>Nachtdienst en officiële feestdagen voor acute noodsituaties.</p>
          <ul class="spoed-price-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> 24/7 bereikbaar en direct onderweg</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Inclusief btw en storingsdiagnose</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Vervolgwerk: € 36,25 per kwartier</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg> Geen verborgen posten</li>
          </ul>
          <a class="btn btn-secondary full" href="tel:+31628763775">Bel Nachtdienst</a>
        </div>
      </div>

      <!-- Hard Price Guarantee Banner -->
      <div class="no-surprise-box">
        <div class="no-surprise-icon">
          <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
        </div>
        <div>
          <h3>Harde No-Surprise Prijsgarantie van INO</h3>
          <p>In 85% van de gevallen verhelpen we de storing binnen het eerste uur. Blijkt er meer tijd of een specifiek vervangend A-merk onderdeel (zoals een aardlekschakelaar of zekering) nodig te zijn? <strong>We stoppen ALTIJD eerst om de exacte meerkosten met jou te overleggen vóórdat we verder gaan.</strong> Je komt bij ons nooit voor een voldongen feit of torenhoge rekening te staan.</p>
        </div>
        <div>
          <a class="btn btn-light" href="tel:+31628763775" style="white-space:nowrap;font-weight:800">Direct Contact</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. FAQ with Schema.org Microdata -->
  <section class="spoed-faq-section" id="faq" itemscope itemtype="https://schema.org/FAQPage">
    <div class="container faq-container">
      <div class="section-heading text-center" style="margin-bottom:34px">
        <span class="eyebrow">VEELGESTELDE VRAGEN BIJ SPOED</span>
        <h2>Veelgestelde Vragen over de Storingsdienst</h2>
        <p>Alles wat je moet weten over onze werkwijze, tarieven en responstijden bij acute nood.</p>
      </div>

      <div class="faq" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <button class="faq-q" type="button" aria-expanded="false">
          <span itemprop="name">Kan ik jullie echt 24/7 en midden in de nacht bellen bij een stroomstoring?</span>
          <span>+</span>
        </button>
        <div class="faq-a" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">Ja. Onze storingsdienst is 24 uur per dag, 7 dagen per week bereikbaar voor acute storingen in Utrecht en omstreken. Je krijgt direct een vakbekwame elektricien aan de lijn en geen anoniem callcenter.</p>
        </div>
      </div>

      <div class="faq" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <button class="faq-q" type="button" aria-expanded="false">
          <span itemprop="name">Wat gebeurt er als het probleem niet binnen het eerste uur is opgelost?</span>
          <span>+</span>
        </button>
        <div class="faq-a" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">In ruim 85% van de gevallen is de storing binnen het eerste uur gelokaliseerd en opgelost. Blijkt er meer tijd of een vervangend onderdeel nodig te zijn? Dan overleggen we altijd eerst de exacte situatie en meerkosten vóór we verder gaan. Zo houd je altijd 100% controle over de kosten.</p>
        </div>
      </div>

      <div class="faq" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <button class="faq-q" type="button" aria-expanded="false">
          <span itemprop="name">Krijg ik garantie op de uitgevoerde spoedreparatie volgens NEN 1010?</span>
          <span>+</span>
        </button>
        <div class="faq-a" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">Absoluut. Al onze reparaties en geplaatste A-merk componenten voldoen aan de geldende NEN 1010 en NEN 3140 veiligheidsnormen. Je ontvangt 12 maanden garantie op het geleverde werk en de gemonteerde materialen.</p>
        </div>
      </div>

      <div class="faq" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <button class="faq-q" type="button" aria-expanded="false">
          <span itemprop="name">Hoe weet ik zeker of de storing bij mij thuis zit of bij netbeheerder Stedin?</span>
          <span>+</span>
        </button>
        <div class="faq-a" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">Kijk eerst of de buren of de straatverlichting wel stroom hebben. Zo ja, dan zit het probleem in je eigen installatie en helpen wij je graag direct. Zit de hele straat in het donker? Dan is er sprake van een netstoring en bel je het gratis Nationaal Storingsnummer (0800-9009) voor Stedin om onnodige voorrijkosten te voorkomen.</p>
        </div>
      </div>

      <div class="faq" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <button class="faq-q" type="button" aria-expanded="false">
          <span itemprop="name">Rekenen jullie voorrijkosten binnen de gemeente Utrecht?</span>
          <span>+</span>
        </button>
        <div class="faq-a" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">Nee, binnen de gemeente Utrecht rekenen wij overdag en 's avonds geen voorrijkosten. Je betaalt uitsluitend het transparante all-in uurtarief inclusief btw en diagnose.</p>
        </div>
      </div>

      <div class="faq" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
        <button class="faq-q" type="button" aria-expanded="false">
          <span itemprop="name">Hoe kan ik betalen bij een spoedklus?</span>
          <span>+</span>
        </button>
        <div class="faq-a" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
          <p itemprop="text">Je kunt na afloop en controle eenvoudig betalen via een digitaal betaalverzoek (zoals een Tikkie of iDEAL link), per bankoverschrijving of contant. Je ontvangt direct een gespecificeerde officiële factuur per e-mail voor je eigen administratie, verzekering of verhuurder.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Non-acute Callback Form -->
  <section class="lp-form-section soft" id="offerte">
    <div class="container form-layout">
      <div>
        <span class="eyebrow">GEEN ACUTE NOOD?</span>
        <h2>Vraag een terugbelverzoek aan.</h2>
        <p>Heeft het geen haast binnen het uur of wil je een meterkastinspectie inplannen? Laat je gegevens achter en we bellen je zo snel mogelijk terug om de situatie rustig te bespreken.</p>
        <div class="form-benefits" style="margin-top:20px">
          <div>✓ Binnen 2 uur reactie tijdens kantooruren</div>
          <div>✓ Vaste en vrijblijvende prijsopgave</div>
          <div>✓ Erkend elektricien met 12 maanden garantie</div>
        </div>
      </div>
      <form id="spoedForm" class="quote-form" action="https://formsubmit.co/d0d9de6bb2a30083d92c3fe4775b9ce6" method="POST">
        <input type="hidden" name="_subject" value="Terugbelverzoek - Spoed elektricien landingspagina">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <label>Naam<input name="name" required placeholder="Voor- en achternaam"></label>
        <label>Telefoonnummer<input name="phone" type="tel" required placeholder="06 ..."></label>
        <label>Wat is er aan de hand?<textarea name="message" rows="4" required placeholder="Bijv. aardlekschakelaar valt soms uit, stopcontact vonkt, kookplaat aansluiten..."></textarea></label>
        <button class="btn btn-primary full" type="submit">Terugbelverzoek Versturen</button>
        <div id="formResult" class="form-result" hidden></div>
      </form>
    </div>
  </section>
</main>

<footer class="lp-footer">
  <div class="container">
    <p style="margin:0 0 6px;font-weight:700">INO Techniek en Installatie · Erkend Elektricien Utrecht</p>
    <p style="margin:0">Tel: <a href="tel:+31628763775" style="color:inherit;text-decoration:underline">06 28 76 37 75</a> · E-mail: <a href="mailto:info@ino-elektra.nl" style="color:inherit;text-decoration:underline">info@ino-elektra.nl</a> · KvK Utrecht</p>
  </div>
</footer>

<!-- Floating Mobile Emergency Bar (Finger-friendly >=48px) -->
<div class="mobile-bar-emergency" role="navigation" aria-label="Directe spoedacties">
  <a href="tel:+31628763775" class="m-btn-call" id="mobileEmergencyCall">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    <span>Bel Nu (24/7)</span>
  </a>
  <a href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20nu%20een%20stroomstoring%20en%20stuur%20hierbij%20een%20foto." target="_blank" rel="noopener" class="m-btn-whatsapp" id="mobileEmergencyWhatsApp">
    <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
    <span>WhatsApp Foto</span>
  </a>
</div>

<script src="script.js?v=6"></script>
</body>
</html>"""

print("Pages batch 2 defined")
