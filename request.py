import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)
parser = MyHTMLParser()
url = 'http://www.biblioceeteps.com.br/acervo/documento/detalhes/141219'
headers = {'Connection': 'keep-alive','Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
           'Host': 'www.biblioceeteps.com.br',
           'Referer': 'http://www.biblioceeteps.com.br/'}
           
response = requests.get(url, headers=headers, stream=True)
iterable = response.iter_lines()
page = ""
for line in iterable:
    page += line.decode('utf-8')
parsed_html = BeautifulSoup(page)

autor_span = parsed_html.find('span', attrs={'id': 'lblAutores'})
autor_name = autor_span.contents[1]

ano_span = parsed_html.find('span', attrs={'id': 'lblAno'})
ano_name = ano_span.contents[1]

editora_span = parsed_html.find('span', attrs={'id': 'lblEditora'})
editora_name = editora_span.contents[1]

paginas_span = parsed_html.find('span', attrs={'id': 'lblPaginas'})
paginas_name = paginas_span.contents[1]

isbn_span = parsed_html.find('span', attrs={'id': 'lblISBN'})
isbn_name = isbn_span.contents[1]

idioma_span = parsed_html.find('span', attrs={'id': 'lblIdioma'})
idioma_name = idioma_span.contents[1]

conhecimento_span = parsed_html.find('span', attrs={'id': 'lblAreaConhecimento'})
conhecimento_name = conhecimento_span.contents[1]

print(autor_name)
print(ano_name)
print(editora_name)
print(paginas_name)
print(isbn_name)
print(idioma_name)
print(conhecimento_name)
