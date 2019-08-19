import requests
import json
import sys
import subprocess
import web_parser
def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

URL = "http://www.biblioceeteps.com.br/Default.aspx/GridItems"
HEADERS = {'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
           'Connection': 'keep-alive',
           'Content-Length': '128',
           'Content-Type': 'application/json; charset=UTF-8',
           'Cookie': 'ASP.NET_SessionId=xq4yngrceqq0qh0rnslhxmyy; unidade=22',
           'Host': 'www.biblioceeteps.com.br',
           'Origin': 'http://www.biblioceeteps.com.br',
           'Referer': 'http://www.biblioceeteps.com.br/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 OPR/62.0.3331.116',
           'X-Requested-With': 'XMLHttpRequest'}

class Request():

    def __init__(self, cutter, book_name):
        self.cutter = cutter
        self.book_name = book_name
        self.params = '{"paging":{"Take":5,"Skip":0},"sorting":null,"filters":{"unidade":"105"},"value":"' + book_name + '"}'

    def run(self):
        response = requests.post(URL, headers=HEADERS, data=self.params)
        response_json = response.json()
        book_id = extract_values(response_json, 'Id')
        # Executes the parser script, passing along the book's id and it's Cutter
        web_parser.WebParser(book_id[0], self.cutter).run()