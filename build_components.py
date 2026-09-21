import os
import re

from emoji_cleaner import strip_emojis

# Header component template with clean URLs (no .html)
def make_header(active_nav=""):
    diensten_active = " active" if active_nav in ["diensten", "groepenkast", "perilex", "laadpaal", "krachtstroom", "frezen", "tuinverlichting", "spoed"] else ""
    tarieven_active = " class=\"active\"" if active_nav == "tarieven" else ""
    werkwijze_active = " class=\"active\"" if active_nav == "werkwijze" else ""
    werkgebied_active = " class=\"active\"" if active_nav == "werkgebied" else ""
    vakmanschap_active = " class=\"active\"" if active_nav == "vakmanschap" else ""
    reviews_active = " class=\"active\"" if active_nav == "reviews" else ""
    contact_active = " class=\"active\"" if active_nav == "contact" else ""
    
    return f"""<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="/" aria-label="INO Techniek en Installatie - Elektricien Utrecht">
      <img src="logo.png" alt="INO Techniek en Installatie - Elektricien Utrecht" width="200" height="54" loading="eager">
    </a>
    <button class="menu-btn" id="menuBtn" aria-label="Menu openen">☰</button>
    <nav id="nav">
      <div class="nav-dd">
        <a href="diensten" class="nav-dd-toggle{diensten_active}">Diensten <span class="caret" aria-hidden="true">▾</span></a>
        <div class="nav-dd-menu">
          <a href="diensten">Alle diensten</a>
          <a href="groepenkast">Groepenkast</a>
          <a href="perilex">Perilex &amp; kookgroep</a>
          <a href="laadpaal-installeren">Laadpalen</a>
          <a href="krachtstroom-aanleggen">Krachtstroom 400V</a>
          <a href="frezen-stopcontacten-verleggen">Frezen &amp; Elektra</a>
          <a href="tuinverlichting-buitenelektra">Tuinverlichting</a>
          <a href="spoed-elektricien-utrecht">24/7 Spoedservice</a>
        </div>
      </div>
      <a href="tarieven"{tarieven_active}>Tarieven</a>
      <a href="werkwijze"{werkwijze_active}>Werkwijze</a>
      <a href="werkgebied"{werkgebied_active}>Werkgebied</a>
      <a href="vakmanschap"{vakmanschap_active}>Vakmanschap</a>
      <a href="reviews"{reviews_active}>Reviews</a>
      <a href="contact"{contact_active}>Contact</a>
      <a class="nav-cta" href="offerte">Offerte aanvragen</a>
    </nav>
  </div>
</header>"""

# Footer component template with clean URLs (no .html)
def make_footer():
    return """<footer>
  <div class="container footer-grid">
    <div><img src="logo.png" alt="INO Techniek en Installatie logo" class="footer-logo" width="160" height="43" loading="lazy" decoding="async"><p>Techniek · Installatie · Innovatie</p></div>
    <div><h4>Diensten</h4><a href="diensten">Alle diensten</a><a href="groepenkast">Groepenkast vervangen</a><a href="perilex">Perilex &amp; kookgroep</a><a href="laadpaal-installeren">Laadpaal installatie</a><a href="krachtstroom-aanleggen">Krachtstroom 400V</a><a href="frezen-stopcontacten-verleggen">Frezen &amp; Elektra</a><a href="tuinverlichting-buitenelektra">Tuinverlichting</a><a href="spoed-elektricien-utrecht">24/7 Spoedservice</a></div>
    <div><h4>Informatie</h4><a href="tarieven">Tarieven</a><a href="werkwijze">Werkwijze</a><a href="werkgebied">Werkgebied</a><a href="wijken">Wijken &amp; regio</a><a href="vakmanschap">Vakmanschap</a><a href="reviews">Reviews</a><a href="faq">Veelgestelde vragen</a></div>
    <div><h4>Contact</h4><a href="tel:+31628763775">06 28 76 37 75</a><a href="https://wa.me/31628763775" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:info@ino-elektra.nl">info@ino-elektra.nl</a><a href="https://www.instagram.com/ino_techniek_en_installatie?stkn=YWEyc2QwcDh6dWNw&amp;utm_source=qr" target="_blank" rel="noopener">Instagram</a><a href="offerte">Offerte aanvragen</a><a href="afspraak">Afspraak aanvragen</a><a href="contact">Contact</a></div>
  </div>
  <div class="copyright">© 2026 INO Techniek en Installatie · Alle rechten voorbehouden</div>
</footer>

<div class="mobile-bar-optimized">
  <a href="tel:+31628763775" class="mobile-btn-call">Direct Bellen</a>
  <a href="https://wa.me/31628763775?text=Hallo%20INO%2C%20ik%20wil%20graag%20een%20foto%20sturen%20voor%20een%20prijsindicatie" target="_blank" rel="noopener" class="mobile-btn-whatsapp">WhatsApp Foto</a>
</div>

<script src="script.js?v=7"></script>"""

print("Components ready with clean URLs")
