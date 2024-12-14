from pdf2docx import Converter

pdf_file="samplePDF.pdf"
docx_file="samplePDF.docx"

cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()