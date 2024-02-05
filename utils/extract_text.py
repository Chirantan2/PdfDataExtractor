import PyPDF2 as pdf2

def read_text(file_path, num_pages) -> str:
    file = open(file_path, 'rb')
    doc = pdf2.PdfReader(file)

    text = ''
    for page in range(num_pages):
        text = text + '\n' + doc.pages[page].extract_text()
    return text
