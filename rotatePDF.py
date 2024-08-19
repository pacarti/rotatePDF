#!/usr/bin/python
# -*- coding: utf-8 -*-


def convertScopeIntoAB(scope):
    rmDash = scope.split('-')
    # return rmDash
    ABlist = []   
    ABlist.append(int((rmDash[0].lstrip('[')).rstrip()))
    ABlist.append(int((rmDash[1].rstrip(']')).lstrip()))

    return ABlist

import PyPDF2, os, sys, re, ast

os.chdir(os.path.dirname(os.path.abspath(__file__)))


pagesRegex = re.compile(r'^\[(\d+\s*,{1}\s*)+\d+\]$')

pagesScopeRegex = re.compile(r'^\[(\d+\s?\-?\s?\d+)+\]$')


pdfFilename = sys.argv[1]
if sys.argv[1] == '--help': 
    print("Syntax: for one-paged PDFs rotatePDF.py [PDF File] [iteration of 90 degrees to rotate]")
    print("For multiple-paged PDFs: rotatePDF.py [PDF File] [page to rotate] [iteration of 90 degrees to rotate]")
    exit()

pdfFile = open(pdfFilename, 'rb')

pdfReader = PyPDF2.PdfReader(pdfFile)

if len(pdfReader.pages) == 1:
    try:
        rotationAngle = int(sys.argv[2])
        page = pdfReader.pages[0]
        page.rotate(rotationAngle)
        pdfWriter = PyPDF2.PdfWriter()
        pdfWriter.add_page(page)
    except ValueError:
        print("For one-paged PDFs, 2nd argument has to be the rotation angle. The value must be literal and a multiple of 90 degrees!(90, 180, 270)")
        exit()
    except IndexError:
        print("For one-paged PDFs, pass the rotation angle after the file name!")
        exit()    

else:
    try:   
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
                for index, number in enumerate(pageNumsList):
                    pageNumsList[index] = number-1


            elif moScope != None:
                scope = moScope.group()
                scopeABList = convertScopeIntoAB(scope)
                # print(scopeABList)
                scopeStart = scopeABList[0]
                scopeEnd = scopeABList[1]


        rotationAngle = int(sys.argv[3])

    except IndexError:
        print("For multiple-paged PDFs, pass the pages to rotate after the file name and rotation angle after! Use \'--help\' argument for more information")
        exit()    


    pdfWriter = PyPDF2.PdfWriter()


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

        for pageI in range(len(pdfReader.pages)):
            if pageI in pageNumsList:
                page = pdfReader.pages[int(pageI)]
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