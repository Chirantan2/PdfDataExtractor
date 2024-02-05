import PyPDF2 as pdf2

def read_text(file_path, num_pages) -> str:
    """Reads text data from file

    Args:
        file_path (_type_): path to the file
        num_pages (_type_): num of pages to be extracted

    Returns:
        text data
    """

    file = open(file_path, 'rb')
    doc = pdf2.PdfReader(file)

    text = ''
    
    for page in range(num_pages):
        text = text + '\n' + doc.pages[page].extract_text()
    return text
