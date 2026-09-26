# Richtlijnen voor AI-assistenten (Google AI Studio, Claude)
Kort en verplicht. Geldt voor v1 (Ino-elektra) en v2 (INOv2). Plak dit in je opdracht als je aan de site werkt.

## Taakverdeling
- Google AI Studio werkt alleen in **v1** (Ino-elektra). Claude werkt alleen in **v2** (INOv2).
- Niets live zetten zonder dat de eigenaar letterlijk "zet live" zegt.

## Waar staat wat
- Bedrijfsgegevens, prijzen, aanrijtijden, Google-score en reviews: **alleen** in `bouw/config.py`.
- In teksten altijd placeholders: `{{uur_dag}}`, `{{groepenkast_1f}}`, `{{aanrijtijd_utrecht}}`, `{{google_score}}` enz. Nooit een bedrag of cijfer hardcoden.
- Bewerk alleen de bron (`content/`, `bouw/`, `assets/`). Nooit de gegenereerde `*.html`, `*/index.html`, `style.css`, `script.js` in de root.
- Na elke wijziging `python3 build.py` (of `python3 build.py --test` als playwright er is) en alle aandachtspunten oplossen.

## Bevestigde feiten (niet van afwijken)
- Achtergrond eigenaar: 2,5 jaar monteur bij Stedin. Ervaring als VP'er bij Heijmans en Liander. Tevens in opleiding tot middenspanningsmonteur.
- Opleiding & Diploma's: MBO 2 Monteur Laagspanningsdistributie (Crebo 25769) en MBO 3 Commercieel medewerker.
- Netbeheer & Veiligheidscertificaten (Certwell):
  * BEI BLS: VP LS-NETTEN (Vakbekwaam Persoon Laagspanningsnetten, cert: 699d796e7cb94b5168e6b6da).
  * Aanwijzingen Stedin: VOP LS-meters en VOP G-meters (meter wisselen elektra & gas).
  * VCA VOL (Veiligheid voor Operationeel Leidinggevenden).
  * Asbestherkenning O&O (inclusief Module 4: Asbest in de meterkast).
  * Netbeheer Nederland: GPI DSO Professioneel & Training gasdetectie.
  * BHV (Safety Holland & Westpoort).
- NEN-normen: **NEN 3140 VP** gecertificeerd via PTC Opleidingen. **Niet** claimen dat er een cursus NEN 1010 is gedaan, wel dat alle installatiewerkzaamheden strikt worden uitgevoerd **conform / volgens NEN 1010**.
- Vakmanschap & diensten: al 4 jaar allround elektrotechniek voor nieuwbouw en renovatie (meterkast, krachtstroom, groepenkasten, laadpalen, thuisbatterijen, zonnepanelen, Perilex, sleuven frezen, leidingen leggen, kabels trekken, stopcontacten in-/opbouw, hotelschakelingen, verlichting afmonteren).
- Groepenkast all-in: 1-fase € 640, 3-fase € 760.
- Perilex aansluiten € 120, nieuwe kookgroep € 150. Er bestaat geen € 275.
- Aanrijtijd vanuit Overvecht: gemeente Utrecht 5–30 min, daarbuiten 15–40 min. Geen andere tijden noemen.
- **Niet** NEN 1010-gecertificeerd, wel werken **volgens** NEN 1010. **Wel** NEN 3140-gecertificeerd.
- Google: toon exact wat Google toont (`google_score` / `google_aantal` in config). Nu 5,0 uit 37.
- Ruim 85% van de storingen is binnen het eerste uur opgelost.
- Voltfix (Amsterdam) is een bevriende elektricien: link alleen op /werkgebied/ en /contact/, nooit in header of footer.

## Nooit doen
- Reviews, namen, cijfers, certificaten of aanrijtijden verzinnen. Bij twijfel: vragen.
- Nooit persoonlijke certificaatnummers (zoals STIPEL cert-ID's) of specifieke opleidersinstituten (zoals PTC) publiek op de website tonen (fraudegevoelig en onnodig).
- Nooit interne netbeheerders-aanwijzingen (zoals Stedin VOP meters) publiek op de site claimen (dit is voorbehouden aan werk in opdracht van de netbeheerder en wekt verwarring).
- `AggregateRating`- of `Review`-schema over het eigen bedrijf (Google verbiedt dit).
- Uitleg hoe klanten zelf aan de groepenkast of leidingen werken.
- Wijkpagina's maken door alleen de plaatsnaam te wisselen (doorway pages).
- Sitewide links naar andere bedrijven (ziet Google als linkruil).
- Google Analytics laden vóór akkoord in de cookiemelding.

## Code en snelheid
- Interne links altijd met slash: `/offerte/`, nooit `/offerte` (op GitHub Pages laadt dat de pagina twee keer).
- `style.css` max 55 KB, `script.js` max 30 KB, pagina max 80 KB HTML. De build waarschuwt.
- CSS/JS die maar op één pagina nodig is: in `assets/extra/<naam>.css|js` en in de front-matter `"extra": ["<naam>"]`. Niet in `style.css`.
- Geen `backdrop-filter`, geen zware animaties, geen externe scripts of fonts (Inter staat lokaal).
- Afbeeldingen: origineel in `assets/foto/`, altijd met `alt`. De build maakt WebP in meerdere formaten met breedte/hoogte.
- Mobiel: geen enkele pagina mag breder zijn dan 390 px (`python3 build.py --test` controleert dit).

## SEO
- Title max 60 tekens, description 120–160, precies één H1 met zoekwoord.
- Structured data alleen via `bouw/layout.py` (JSON-LD), geen microdata.
- Schrijfstijl: je/jij, zakelijk-vriendelijk, korte zinnen, duidelijke prijzen.
