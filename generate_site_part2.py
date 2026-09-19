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
  <title>Spoed elektricien Utrecht | Nu bereikbaar | INO Techniek en Installatie</title>
  <meta name="description" content="Spoed elektricien nodig in Utrecht? INO is 24/7 bereikbaar bij stroomstoring of kortsluiting. Bel direct 06 28 76 37 75, snel ter plaatse.">
  <meta name="robots" content="index, follow">
  <link rel="stylesheet" href="style.css?v=6">
  <style>
    .lp-header{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.97);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
    .lp-header .nav-wrap{height:76px;justify-content:space-between}
    .lp-call-btn{display:inline-flex;align-items:center;gap:8px;background:var(--green);color:#10220d;padding:12px 18px;border-radius:10px;font-weight:800;font-size:14px}
    .lp-hero{padding:50px 0 40px;background:linear-gradient(135deg,#fbfdfb 0%,#f2faf0 55%,#eef9ff 100%)}
    .lp-badge{display:inline-flex;align-items:center;gap:8px;background:#eafbe6;color:var(--green-dark);border:1px solid #c9edbd;padding:8px 14px;border-radius:999px;font-weight:800;font-size:13px;margin-bottom:18px}
    .lp-badge .dot{width:8px;height:8px;border-radius:50%;background:var(--green-dark);animation:lp-pulse 1.6s infinite}
    @keyframes lp-pulse{0%{opacity:1}50%{opacity:.35}100%{opacity:1}}
    .lp-hero h1{font-size:clamp(34px,5.4vw,56px);letter-spacing:-2px}
    .lp-big-actions{display:flex;flex-direction:column;gap:12px;max-width:420px;margin:26px 0}
    .lp-big-call{display:flex;align-items:center;justify-content:center;gap:10px;background:var(--green);color:#10220d;padding:20px 22px;border-radius:14px;font-weight:800;font-size:22px;box-shadow:0 10px 30px rgba(76,180,54,.28)}
    .lp-big-call:hover{background:#58c63b}
    .lp-sub-actions{display:flex;gap:10px}
    .lp-sub-actions .btn{flex:1}
    .lp-trust{display:flex;gap:22px;flex-wrap:wrap;font-size:13px;font-weight:700;color:var(--muted)}
    .lp-trust span{display:flex;align-items:center;gap:6px}
    .lp-reasons{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
    .lp-reason{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px}
    .lp-reason .n{font-size:26px}
    .lp-price-strip{background:var(--dark);color:#fff;padding:22px 0}
    .lp-price-strip .container{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px}
    .lp-price-strip strong{color:var(--green)}
    .lp-form-section{padding:60px 0}
    .lp-form-section .form-layout{grid-template-columns:.9fr 1.1fr}
    .lp-footer{padding:28px 0;border-top:1px solid var(--line);text-align:center;color:#89928b;font-size:12px}
    @media (max-width:760px){
      .lp-reasons{grid-template-columns:1fr}
      .lp-sub-actions{flex-direction:column}
      .lp-form-section .form-layout{grid-template-columns:1fr}
    }
  </style>
</head>
<body>

<header class="lp-header">
  <div class="container nav-wrap">
    <a class="brand" href="index.html" aria-label="INO Techniek en Installatie">
      <img src="logo.png" alt="INO Techniek en Installatie logo">
    </a>
    <a class="lp-call-btn" href="tel:+31628763775">06 28 76 37 75</a>
  </div>
</header>

<main>
  <section class="lp-hero">
    <div class="container hero-grid-2col" style="margin-bottom: 30px;">
      <div>
        <span class="lp-badge"><span class="dot"></span> Nu bereikbaar — 24/7 storingsdienst</span>
        <h1>Spoed elektricien nodig in Utrecht?</h1>
        <p class="lead">Stroomstoring, kortsluiting of rook uit de meterkast? INO staat dag en nacht voor je klaar in Utrecht en omstreken. Bel nu, geen wachtrij, direct een vakman aan de lijn.</p>

        <div class="lp-big-actions">
          <a class="lp-big-call" href="tel:+31628763775">Bel direct: 06 28 76 37 75</a>
          <div class="lp-sub-actions">
            <a class="btn btn-whatsapp full" href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20heb%20een%20elektrische%20storing%20en%20heb%20met%20spoed%20hulp%20nodig." target="_blank" rel="noopener">WhatsApp</a>
            <a class="btn btn-secondary full" href="#offerte">Liever terugbelverzoek</a>
          </div>
        </div>

        <div class="lp-trust">
          <span>✓ Sinds 2021 actief in Utrecht</span>
          <span>✓ NEN 3140 VP</span>
          <span>✓ Meestal binnen het uur ter plaatse</span>
          <span>✓ 12 mnd garantie op werk</span>
        </div>
      </div>
      <div class="hero-image-wrapper">
        <img src="storingsdienst-meting.jpg" alt="Storingsdienst elektricien Utrecht doormeten groepenkast multimeter" class="showcase-img" loading="eager" referrerPolicy="no-referrer">
        <div class="hero-badge-floating">Storingsdienst · Nauwkeurige foutmeting NEN 3140</div>
      </div>
    </div>
    <div class="container">
      <div class="lp-reasons">
        <div class="lp-reason"><h3>Direct een vakman</h3><p>Geen callcenter, geen wachtrij — je krijgt direct een ervaren elektricien aan de lijn.</p></div>
        <div class="lp-reason"><h3>24/7 bereikbaar</h3><p>Ook 's avonds, in het weekend en op feestdagen staan we voor je klaar bij een storing.</p></div>
        <div class="lp-reason"><h3>Vooraf duidelijke prijs</h3><p>Je weet waar je aan toe bent voordat we beginnen — geen verrassingen achteraf.</p></div>
      </div>
    </div>
  </section>

  <section class="lp-price-strip">
    <div class="container" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:18px">
      <div>
        <strong style="display:block;font-size:15px">Transparante tarieven bij spoed & storingen (incl. btw):</strong>
        <span style="font-size:13px;opacity:.9">Overdag € 90/u · Buiten kantooruren € 120/u · Vanaf 22:00 en weekenden € 145/u · Gratis voorrijkosten in Utrecht!</span>
      </div>
      <a class="btn btn-light" href="tel:+31628763775">Bel direct <strong>06 28 76 37 75</strong></a>
    </div>
  </section>

  <section class="lp-form-section soft" id="offerte">
    <div class="container form-layout">
      <div>
        <span class="eyebrow">GEEN ACUTE SPOED?</span>
        <h2>Vraag een terugbelverzoek aan.</h2>
        <p>Laat je gegevens achter en we bellen je zo snel mogelijk terug om de situatie te bespreken.</p>
      </div>
      <form id="spoedForm" class="quote-form" action="https://formsubmit.co/d0d9de6bb2a30083d92c3fe4775b9ce6" method="POST">
        <input type="hidden" name="_subject" value="Terugbelverzoek - Spoed elektricien landingspagina">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <label>Naam<input name="name" required placeholder="Voor- en achternaam"></label>
        <label>Telefoon<input name="phone" required placeholder="06 ..."></label>
        <label>Wat is er aan de hand?<textarea name="message" rows="4" required placeholder="Bijv. groep valt steeds uit, geen stroom in de keuken..."></textarea></label>
        <button class="btn btn-primary full" type="submit">Terugbelverzoek versturen</button>
        <div id="formResult" class="form-result" hidden></div>
      </form>
    </div>
  </section>
</main>

<footer class="lp-footer">
  <div class="container">© 2026 INO Techniek en Installatie · 06 28 76 37 75 · info@ino-elektra.nl</div>
</footer>

<div class="mobile-bar-optimized">
  <a href="tel:+31628763775" class="mobile-btn-call">Direct Bellen</a>
  <a href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20wil%20graag%20een%20foto%20sturen%20voor%20een%20prijsindicatie" target="_blank" rel="noopener" class="mobile-btn-whatsapp">WhatsApp Foto</a>
</div>

<script src="script.js?v=6"></script>
</body>
</html>"""

print("Pages batch 2 defined")
