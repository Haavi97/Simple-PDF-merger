import os
import sys
from sys import argv

from PyPDF2 import PdfFileReader, PdfFileWriter

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    paths = []
    output_file = 'merged.pdf'
    folder_flag = False
    for i in range(1, len(argv)):
        if '--output=' in argv[i]:
            output_file = argv[i].split('=')[-1]
        elif ('-m' in argv[i]) or ('--merge' in argv[i]):
            folder_flag = True
        elif argv[i] == '-h' or argv[i] == '--help':
            print('Usage: python mergepdf.py [file_paths] \[--output=output_file_path]\
                \n\t file_paths\tFiles to merge paths (full or relative)\
                \n\t --output=\toutput file name\
                \n\t -h --help\tshow this help\
                \nOrder of the given files will be the order they are merged')
        else:
            paths.append(argv[i])
    try:
        if folder_flag:
            paths = list(map(lambda x: 'pdfs' + os.sep + x,
                        filter(lambda x: x[-4:] == '.pdf', os.listdir('pdfs'))))
        merge_pdfs(paths, output=output_file)
        print('Succesfully merged to file: {}'.format(output_file))
    except:
        print('\n\tPlease, check the input parameters\
            \n\n\tUsage help: python mergepdf.py -h')
