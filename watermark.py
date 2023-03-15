import sys
import os
import PyPDF2
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import red

# Get args
watermark_string = sys.argv[1]
input_file = sys.argv[2]


# Init - Create the watermark files
ca_portrait = Canvas('tmp-portrait.pdf', pagesize = A4)
ca_landscape = Canvas('tmp-landscape.pdf', pagesize = landscape(A4))

def draw_string(ca):
    width = ca._pagesize[0]
    height = ca._pagesize[1]
    ca.setFont('Times-Roman', 12)
    ca.setFillColor(red)
    ca.drawRightString(width - 25, height - 25, watermark_string)
    return ca

draw_string(ca_portrait).save()
draw_string(ca_landscape).save()

#### Use the created watermarks to watermark a file

source_pdf = PyPDF2.PdfReader(open(input_file, 'rb'))

landscape_file = open('tmp-landscape.pdf', 'rb')
watermark_landscape = PyPDF2.PdfReader(landscape_file)
portrait_file = open('tmp-portrait.pdf', 'rb')
watermark_portrait = PyPDF2.PdfReader(portrait_file)
output = PyPDF2.PdfWriter()

for page in source_pdf.pages:
    # Check rotation
    if page.mediabox.width < page.mediabox.height:
        page.merge_page(watermark_portrait.pages[0])
    else:
        page.merge_page(watermark_landscape.pages[0])
    output.add_page(page)


file_name = input_file.split('.pdf')[0] + '-watermarked.pdf'
with open(file_name, 'wb') as file:
    output.write(file)



landscape_file.close()
portrait_file.close()
os.remove('tmp-portrait.pdf')
os.remove('tmp-landscape.pdf')