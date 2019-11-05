import re
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

only_body = SoupStrainer('body')
androwarnHTML = BeautifulSoup(open("com.google.android.apps.docs_1572456480.html"), features="html.parser",
                              parse_only=only_body)
analysisResults = androwarnHTML.find_all('div', attrs={"class": "tab-pane"})
resultList = androwarnHTML.find_all('ul', attrs={"class": "nav nav-list"})
liList = re.findall("<li.*", str(resultList))
iteration = 0
lowerBound = 0
upperBound = 0
for liTag in liList:
    iteration = iteration + 1
    if liTag == '<li class="nav-header">Analysis Results</li>':
        lowerBound = iteration
    if liTag == '<li class="nav-header">Apk File</li>':
        upperBound = iteration
upperIndex = upperBound - lowerBound + 3

resultIndex = 0
for liTag in analysisResults:
    if 3 < resultIndex < upperIndex:
        h2tag = re.findall("<h2>(.*?)<*/*h2>", str(liTag))
        h3tag = re.findall("<h3>(.*?)<*/*h3>", str(liTag))
        print(h2tag)
        print(h3tag)
    resultIndex = resultIndex + 1

# To Do Pull specific values and store into excel document
# To Do add comments
