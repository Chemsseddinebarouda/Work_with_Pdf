# to use this script you should instal PyPDF2 using this line : !pip install PyPDF2

#Fonction To delete pages from pdfs  using pages to keep






from PyPDF2 import PdfWriter, PdfReader
pages_to_keep = [0,1] # page numbering starts from 0
infile = PdfReader('source.pdf', 'rb')
output = PdfWriter()

for i in pages_to_keep:
    p = infile.pages[i] 
    output.add_page(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)

#Fonction To delete pages from pdfs using pages to delete


from PyPDF2 import PdfWriter, PdfReader
pages_to_delete = [3, 4, 5] # page numbering starts from 0
infile = PdfReader('source.pdf', 'rb')
output = PdfWriter()

for i in range(len(infile.pages) ):
    if i not in pages_to_delete:
        p = infile.get_page(i)
        output.add_page(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)
