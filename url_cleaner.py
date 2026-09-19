import re

PAGES_LIST = [
    "index", "diensten", "groepenkast", "perilex",
    "laadpaal-installeren", "krachtstroom-aanleggen", "frezen-stopcontacten-verleggen",
    "tuinverlichting-buitenelektra", "spoed-elektricien-utrecht", "tarieven",
    "werkwijze", "werkgebied", "wijken", "vakmanschap",
    "reviews", "offerte", "afspraak", "faq", "contact"
]

def clean_urls_in_html(html_str):
    # Replace canonical and og:url
    html_str = re.sub(r'(https://ino-elektra\.nl/)index\.html', r'\1', html_str)
    for p in PAGES_LIST:
        if p == "index":
            continue
        html_str = re.sub(rf'(https://ino-elektra\.nl/){p}\.html', rf'\1{p}', html_str)
        
    # Replace href="index.html" with href="/"
    html_str = re.sub(r'href=["\']index\.html(["\'#?])', r'href="/\1', html_str)
    html_str = html_str.replace('href="//"', 'href="/"').replace('href="/#', 'href="/#').replace('href="/?', 'href="/?')
    
    # Replace href="page.html" with href="page"
    for p in PAGES_LIST:
        if p == "index":
            continue
        # href="p.html"
        html_str = re.sub(rf'href=["\']{p}\.html(["\'#?])', rf'href="{p}\1', html_str)
        
    # Fix any accidental href="page" "
    return html_str
