from collections import Counter
import fitz  # PyMuPDF
import re

def clean_text(text):
    # Remove unwanted characters and normalize spaces and line breaks
    text = re.sub(r'\n+', ' ', text)  # Replace newlines with spaces
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = text.strip()  # Remove leading and trailing whitespace
    return text

def generate_summary(text):
    # Clean the text before summarization
    text = clean_text(text)
    
    # Break text into sentences
    sentences = text.split('. ')
    
    # Logic to handle different document lengths
    if len(sentences) < 5:
        summary = ' '.join(sentences[:1]) + '...'
    elif len(sentences) < 20:
        summary = ' '.join(sentences[:3]) + '...'
    elif len(sentences) < 50:
        summary = ' '.join(sentences[:2] + sentences[len(sentences)//2:len(sentences)//2 + 2] + sentences[-2:]) + '...'
    else:
        summary = ' '.join(sentences[:3] + sentences[len(sentences)*1//3:len(sentences)*1//3 + 3] + sentences[len(sentences)*2//3:len(sentences)*2//3 + 3] + sentences[-3:]) + '...'
    
    return summary

def custom_summarizer(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        
        for page in doc:
            text += page.get_text()
        
        summary = generate_summary(text)
        print(f"Summary generated for {pdf_path}.")
        return summary
    except Exception as e:
        print(f"Error in summarizing PDF {pdf_path}: {e}")
        return ""
