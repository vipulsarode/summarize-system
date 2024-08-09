import os
from langchain_groq import ChatGroq
from pdf_extractor import scrape_pdf_text
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

llama3 = ChatGroq(api_key = api_key, model = 'llama3-70b-8192', temperature = 0.5, max_tokens= 512)

text = scrape_pdf_text('/Users/vipulsarode/Work/RA/summarize-system/data/unet.pdf')

messages = [
    (
        "system",
        "You are a helpful assistant specializing in reading and understanding Machine Learning and AI research papers. You need to understand the following paper first and then summarize it in a easy to understand way.",
    ),
    ("human", text),
]
ai_msg = llama3.invoke(messages)
print(ai_msg.content)




