import pdfplumber
import spacy            #NLP libraries used to extract data 

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
        return text.strip()
    

path = "Aadi_RESUME.docx.pdf"
print(extract_text_from_pdf(path))