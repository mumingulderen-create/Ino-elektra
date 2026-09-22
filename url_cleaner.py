import re

PAGES_LIST = [
    "diensten", "groepenkast", "perilex",
    "laadpaal-installeren", "krachtstroom-aanleggen", "frezen-stopcontacten-verleggen",
    "tuinverlichting-buitenelektra", "spoed-elektricien-utrecht", "tarieven",
    "werkwijze", "werkgebied", "wijken", "vakmanschap",
    "reviews", "offerte", "afspraak", "faq", "contact"
]

def clean_urls_in_html(html_str):
    # 1. Canonical and og:url for homepage
    html_str = re.sub(r'https://ino-elektra\.nl/index(?:\.html|/)?', 'https://ino-elektra.nl/', html_str)
    
    # 2. Canonical and og:url for subpages: ensure https://ino-elektra.nl/{p}/ with trailing slash
    for p in PAGES_LIST:
        # Replace https://ino-elektra.nl/p.html or https://ino-elektra.nl/p (no slash) with https://ino-elektra.nl/p/
        html_str = re.sub(rf'https://ino-elektra\.nl/{p}(?:\.html|/?)(?=[\"\'\s#?]|$)', f'https://ino-elektra.nl/{p}/', html_str)

    # 3. Replace href="index.html" or href="/index.html" with href="/"
    html_str = re.sub(r'href=[\"\'](?:/)?index\.html([\"\'#?])', r'href="/\1', html_str)
    html_str = html_str.replace('href="//"', 'href="/"').replace('href="/#', 'href="/#').replace('href="/?', 'href="/?')

    # 4. Replace href to subpages: href="p.html", href="/p.html", href="p", href="/p" -> href="/p/"
    for p in PAGES_LIST:
        # Match href="p.html", href="/p.html", href="p", href="/p", href="p/", href="/p/" followed by quote, hash or query
        html_str = re.sub(rf'href=[\"\'](?:/)?{p}(?:\.html|/?)([\"\'#?])', rf'href="/{p}/\1', html_str)
        # Clean double slash in href="/p//#..." or href="/p//"
        html_str = html_str.replace(f'href="/{p}//', f'href="/{p}/')
        html_str = html_str.replace(f'href="/{p}/"', f'href="/{p}/"')
        html_str = html_str.replace(f'href="/{p}/\'', f'href="/{p}/\'')

    # 5. Root-relative assets and images so they load cleanly on any subpage level
    html_str = re.sub(r'href=[\"\'](?:/)?style\.css(\?[^\"\']*)?[\"\']', r'href="/style.css\1"', html_str)
    html_str = re.sub(r'src=[\"\'](?:/)?script\.js(\?[^\"\']*)?[\"\']', r'src="/script.js\1"', html_str)
    html_str = re.sub(r'(?<!this\.)src=[\"\'](?!https?://|/|data:)([^\"\']+\.(?:jpg|jpeg|png|svg|webp|ico))[\"\']', r'src="/\1"', html_str)
    html_str = re.sub(r'this\.src=[\"\'](?!https?://|/)([^\"\']+\.(?:jpg|jpeg|png|svg|webp|ico))[\"\']', r"this.src='/\1'", html_str)

    return html_str

