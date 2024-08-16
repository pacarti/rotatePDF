#!/usr/bin/python
# -*- coding: utf-8 -*-


# rotatePDF.py - rotates chosen page or scope of pages of a PDF file by chosen iteration of 90 degrees

# Step3.2.: Rotate chosen pages given in scope(e.g. 5-11)


def convertScopeIntoAB(scope):
    rmDash = scope.split('-')
    # return rmDash
    ABlist = []   
    ABlist.append(int((rmDash[0].lstrip('[')).rstrip()))
    ABlist.append(int((rmDash[1].rstrip(']')).lstrip()))

    return ABlist

import PyPDF2, os, sys, re, ast

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# pagesRegex = re.compile(r'^\[(\d+\,+\s?)+\]$')
# pagesRegex = re.compile(r'^\[(\d+,?\s?)+\]$')
pagesRegex = re.compile(r'^\[(\d+\s*,{1}\s*)+\d+\]$')

pagesScopeRegex = re.compile(r'^\[(\d+\s?\-?\s?\d+)+\]$')

try:
    pdfFilename = sys.argv[1]
    if sys.argv[1] == '--help': 
        print("Syntax: rotatePDF.py [PDF File] [page to rotate] [iteration of 90 degrees to rotate]")
        exit()

    pdfFile = open(pdfFilename, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFile)

    pageNum = sys.argv[2]

    if pageNum[0] == '[':
        mo = pagesRegex.search(pageNum)
        moScope = pagesScopeRegex.search(pageNum)
        if mo == None and moScope == None:
            print("Type multiple pages to rotate in quotes and square brackets, separated by comma. E.g.: '[2, 4, 6]'")
            print("For scope, type START page followed by dash and FINISH page in square brackets and commas. E.g.: '[1 - 5]'")
            exit()
        elif mo != None:
            pageNumsList = ast.literal_eval(pageNum)
            # print(pageNumsList)

            '''
            if moScope == None:
                        print("For scope, type START page followed by dash and FINISH page in square brackets and commas. E.g.: '[1 - 5]'")
                        exit()
            '''

        elif moScope != None:
            scope = moScope.group()
            scopeABList = convertScopeIntoAB(scope)
            # print(scopeABList)
            scopeStart = scopeABList[0]
            scopeEnd = scopeABList[1]

    # sys.argv[2].split(',') 

    rotationAngle = int(sys.argv[3])

except IndexError:
    print("ERROR: Incorrect parameters count.")
    print("Syntax: rotatePDF.py [PDF File] [page to rotate] [iteration of 90 degrees to rotate]")

pdfWriter = PyPDF2.PdfWriter()

# pdfWriter.add_page(page)

# If not multiple pages were typed, then rotate single page that was selected:
if 'pageNumsList' not in globals() and 'scopeABList' not in globals():    
    page = pdfReader.pages[int(pageNum) - 1]

    page.rotate(rotationAngle)
    
    for pageI in range(len(pdfReader.pages)):
        if pageI == int(pageNum) - 1:
            pdfWriter.add_page(page)
        else:
            pdfWriter.add_page(pdfReader.pages[pageI])
elif 'scopeABList' not in globals():
    # pageNum = '' # NULL the pageNum variable to use it in a loop
    # for pageNum in pageNumsList:

# BUG - adds the page to be rotated twice - once non-rotated and once rotated.

    for pageI in range(len(pdfReader.pages)):
        if pageI in pageNumsList:
            page = pdfReader.pages[int(pageI-1)]
            page.rotate(rotationAngle)
            pdfWriter.add_page(page)
        else:
            pdfWriter.add_page(pdfReader.pages[pageI])

else:
    for pageI in range(scopeStart-1):
        pdfWriter.add_page(pdfReader.pages[pageI])
    for pageI in range(scopeStart, scopeEnd+1):
        page = pdfReader.pages[int(pageI-1)]
        page.rotate(rotationAngle)
        pdfWriter.add_page(page)
    for pageI in range(scopeEnd+1, len(pdfReader.pages)+1):
        pdfWriter.add_page(pdfReader.pages[pageI-1])


resultPdfFileNameBase = pdfFilename.split('.pdf')[0]

resultPDFFile = open(resultPdfFileNameBase + '_rotated.pdf', 'wb')

pdfWriter.write(resultPDFFile)

resultPDFFile.close()

pdfFile.close()