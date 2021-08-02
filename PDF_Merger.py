import PyPDF2
import os

def pdf_combiner(lis):
    merger = PyPDF2.PdfFileMerger()

    if len(os.listdir(lis)) < 1:
        print('"PDFs" folder is empty')

    for pdf in os.listdir(lis):
        print(pdf)
        merger.append(f'PDFs\\{pdf}')
    merger.write('super.pdf')

pdf_combiner('PDFs')
