import re
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

span = SoupStrainer('body')
soup = BeautifulSoup(open("com.google.android.apps.docs_1572456480.html"), features="html.parser", parse_only=span)

print(re.findall("This application reads the ISO country code equivalent for the SIM provider's country code", str(soup.find_all('h3'))))
# print(soup.find_all('h2'))

# Test another application to determine if the results are always laid out the same
# Pull specific values and store into excel document
