import re
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

only_body = SoupStrainer('body')
androwarnHTML = BeautifulSoup(open("com.google.android.apps.docs_1572456480.html"), features="html.parser",
                              parse_only=only_body)

analysisResults = androwarnHTML.find_all('div', attrs={"class": "tab-pane"})
resultIndex = 0
for item in analysisResults:
    if 3 < resultIndex < len(analysisResults)-17:
        h2tag = re.findall("<h2>(.*?)<*/*h2>", str(item))
        h3tag = re.findall("<h3>(.*?)<*/*h3>", str(item))
        print(h2tag)
        print(h3tag)
    resultIndex = resultIndex + 1

# To Do Pull specific values and store into excel document
