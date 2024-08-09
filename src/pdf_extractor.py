from pdfminer.high_level import extract_text

def scrape_pdf_text(pdf_path):
    return extract_text(pdf_path)