import requests
from HttpExceptions import *
from bs4 import BeautifulSoup

URL = 'http://www.biblioceeteps.com.br/acervo/documento/detalhes/141219'
HEADERS = {'Connection': 'keep-alive','Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                         AppleWebKit/537.36 (KHTML, like Gecko) \
                         Chrome/76.0.3809.100 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml; \
                     q=0.9,image/webp,image/apng,*/*;q=0.8, \
                     application/signed-exchange;v=b3',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
           'Host': 'www.biblioceeteps.com.br',
           'Referer': 'http://www.biblioceeteps.com.br/'}

def recover_page(url, headers):  
    response = requests.get(url, headers=headers, stream=True)
    if (response.status_code != 200):
        raise HttpStatusCodeError()
    iterable = response.iter_lines()
    page = ""
    for line in iterable:
        page += line.decode('utf-8')

    return page

def recover_element(parsed_html, search_attrs, wanted_attr=None):
    whole_tag = parsed_html.find(attrs=search_attrs)
    if (wanted_attr is not None):
        return whole_tag.attrs[wanted_attr]
    else:
        for element in whole_tag.contents:
            if (element.find("strong")):
                return element

page = recover_page(URL, HEADERS)
parsed_html = BeautifulSoup(page, features="html.parser")

print(recover_element(parsed_html, {'id': 'lblTitulo'}))