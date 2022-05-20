from bs4 import BeautifulSoup

def extract_code_from_html(html):
    codes = BeautifulSoup(html, "html.parser").find_all("code")

    return [item.text for item in codes]