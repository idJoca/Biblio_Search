import requests
from HttpExceptions import *
from bs4 import BeautifulSoup
import sys

# The headers are the same for all connections
# If necessary, pass a new one via sys args
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
# The URL used to download the page and parse it
URL = sys.argv[1]
# If sys args is longer than 2 then, a header was sent
if (len(sys.argv) > 1):
    # Uses the new header
    HEADERS = sys.argv[2]

def recover_page(url, headers): 
    """
    Execute a http get and fetch the website's html code.
    Because the page is, probably, bigger than the
    requests library's default buffer, the page is
    recovered in stream mode, piece by piece.
    """
    # Executes the get protocol
    response = requests.get(url, headers=headers, stream=True)
    # If, for some reason, the returned status code
    # It's not 200, raise an exception
    if (response.status_code != 200):
        # Custom exception
        raise HttpStatusCodeError("Error recovering page")
    # Recovers the page as an iterable,
    # Something that can be deal with slowly
    iterable = response.iter_lines()
    # Str object, where the page will be loaded to
    page = ""
    # Concatenates the whole page to 'page'
    for line in iterable:
        # Also, because the page is in bytes
        # we need to decode it to utf-8.
        # i.e.: human-readable
        page += line.decode('utf-8')
    return page

def recover_element(parsed_html, search_attrs, wanted_attr=None):
    """
    By passing the parsed html object and the attributes,
    within the tags, the content can be recovered.
    Keep in mind that the element is assumed to not be
    an attribute, but rather actual data. Also, any
    other tag is ignored.
    If you need to recover an attribute, also pass the
    'wanted_attr' variable.
    """
    # Look for the attributes in the html code
    whole_tag = parsed_html.find(attrs=search_attrs)
    # If 'wanted_attr' was passed, just return
    # it's value within the tag
    if (wanted_attr is not None):
        return whole_tag.attrs[wanted_attr]
    else:
        # If not, search over the children
        # for an element that is not an actual tag
        for element in whole_tag.children:
            # If the element do not contains
            # the 'attrs' it's not an tag, but
            # an actual text
            if not (hasattr(element, 'attrs')):
                # therefore, return it
                return element

page = recover_page(URL, HEADERS)
parsed_html = BeautifulSoup(page, features="html.parser")
print(recover_element(parsed_html, {'id': 'lblTitulo'}))