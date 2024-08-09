import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from pdf_extractor import scrape_pdf_text



text = scrape_pdf_text('/Users/vipulsarode/Work/RA/summarize-system/data/unet.pdf')
print(text)