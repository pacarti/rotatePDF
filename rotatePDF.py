# rotatePDF.py - rotates chosen page or scope of pages of a PDF file by chosen iteration of 90 degrees

# Step3: rotate chosen scope of pages by chosen angle

import PyPDF2, os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    pdfFilename = sys.argv[1]
    if sys.argv[1] == '--help': 
        print("Syntax: rotatePDF.py [PDF File] [page to rotate] [iteration of 90 degrees to rotate]")
        exit()

    pdfFile = open(pdfFilename, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfFile)

    pageNum = sys.argv[2]

    page = pdfReader.pages[int(pageNum) - 1]

    page.rotate(int(sys.argv[3]))
except IndexError:
    print("ERROR: Incorrect parameters count.")
    print("Syntax: rotatePDF.py [PDF File] [page to rotate] [iteration of 90 degrees to rotate]")

pdfWriter = PyPDF2.PdfWriter()

# pdfWriter.add_page(page)

for pageI in range(len(pdfReader.pages)):
    if pageI == int(pageNum) - 1:
        pdfWriter.add_page(page)
    else:
        pdfWriter.add_page(pdfReader.pages[pageI])

resultPdfFileNameBase = pdfFilename.split('.pdf')[0]

resultPDFFile = open(resultPdfFileNameBase + '_rotated.pdf', 'wb')

pdfWriter.write(resultPDFFile)

resultPDFFile.close()

pdfFile.close()