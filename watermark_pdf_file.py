import PyPDF2
from PyPDF2 import PdfWriter, PdfReader

tamplate = PyPDF2.PdfFileReader(open('my_vkr.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('218 wtr.pdf.', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(tamplate.getNumPages()):
    page = tamplate.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open('watermark_output.pdf', 'wb') as file:
        output.write(file)


