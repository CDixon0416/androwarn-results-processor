import re
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.styles import Font

workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Androwarn"
headers = ['Project Name', 'Number of Permissions', 'Permissions', 'Number of Activities', 'Activities']
worksheet.append(headers)
worksheet['A1'].font = Font(bold=True, italic=True)
worksheet['B1'].font = Font(bold=True, italic=True)
worksheet['C1'].font = Font(bold=True, italic=True)
worksheet['D1'].font = Font(bold=True, italic=True)

only_body = SoupStrainer('body')
androwarnHTML = BeautifulSoup(open("com.google.android.apps.docs_1572456480.html"), features="html.parser",
                              parse_only=only_body)

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

analysisResults = androwarnHTML.find_all('div', attrs={"class": "tab-pane"})
resultIndex = 0
excelH3Tag = ""
titleFlag = 1

for liTag in analysisResults:
    if titleFlag == 1:
        worksheet['A' + str(resultIndex+2)] = 'titleofapk'
        worksheet['A' + str(resultIndex+2)].alignment = Alignment(wrap_text=True, vertical='top')
        worksheet.column_dimensions['A'].width = 40
        titleFlag = 0
    if 3 < resultIndex < upperIndex:
        h2tag = re.findall("<h2>(.*?)<*/*h2>", str(liTag))
        h3tag = re.findall("<h3>(.*?)<*/*h3>", str(liTag))
        worksheet['B' + str(resultIndex-2)] = h2tag[0]
        worksheet['B' + str(resultIndex-2)].alignment = Alignment(wrap_text=True, vertical='top')
        worksheet.column_dimensions['B'].width = 40
        worksheet['C' + str(resultIndex-2)] = len(h3tag)
        worksheet['C' + str(resultIndex-2)].alignment = Alignment(wrap_text=True, vertical='top')
        worksheet.column_dimensions['C'].width = 40
        for i in range(len(h3tag)):
            excelH3Tag = excelH3Tag + h3tag[i] + '\n'
        worksheet['D' + str(resultIndex-2)] = excelH3Tag
        worksheet['D' + str(resultIndex-2)].alignment = Alignment(wrap_text=True, vertical='top')
        worksheet.column_dimensions['D'].width = 40
        excelH3Tag = ""
        titleFlag = 1
    resultIndex = resultIndex + 1

workbook.save("Androwarn Results.xlsx")

# To Do Pull specific values and store into excel document
# To Do Add comments
# To Do Add iteration through all files
