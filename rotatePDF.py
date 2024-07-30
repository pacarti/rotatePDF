# RotatePDF - rotates chosen page or scope of pages of a PDF file by chosen iteration of 90 degrees

# Step2: rotate chosen page by chosen angle
# Step3: rotate chosen scope of pages by chosen angle

import PyPDF2, os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pdfFilename = sys.argv[1]

pdfFile = open(pdfFilename, 'rb')

pdfReader = PyPDF2.PdfReader(pdfFile)

pageNum = sys.argv[2]

page = pdfReader.pages[int(pageNum) - 1]

page.rotate(int(sys.argv[3]))

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