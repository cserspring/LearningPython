import requests
from bs4 import BeautifulSoup
import re

urls = set()
main_site = "http://www.cnblogs.com/shuaiwhu"
def download_pages_from_site(site):
    if site not in urls and site is not None and site.startswith(main_site):
        urls.add(site)
        source_code = requests.get(site)
        plain_text = source_code.text
        lines = plain_text.split("\\n")
        fx = open(re.sub('[/?]', '.', site[7:]), "w", 1024, "utf-8")

        for line in lines:
            fx.write(line + "\n")
        fx.close()
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a'):
            download_pages_from_site(link.get('href'))

download_pages_from_site(main_site)