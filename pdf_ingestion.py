import json
import requests
import os
import logging

PDF_FOLDER = 'pdfs/'

# Ensure the PDF folder exists
os.makedirs(PDF_FOLDER, exist_ok=True)

def fetch_dataset_from_local_file():
    dataset_path = 'AI-Internship-Task/Dataset.json'  # Update the path as needed
    try:
        with open(dataset_path, 'r') as f:
            dataset = json.load(f)
        print(f"Dataset loaded successfully with {len(dataset)} entries.")
        return dataset
    except Exception as e:
        logging.error(f"Error loading dataset from local file: {e}")
        return {}

def fetch_pdf(pdf_id, url):
    try:
        pdf_path = os.path.join(PDF_FOLDER, f'{pdf_id}.pdf')
        
        if os.path.exists(pdf_path):
            print(f"PDF {pdf_id} already downloaded.")
            return pdf_path
        
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded PDF {pdf_id} from {url}.")
        return pdf_path
    except Exception as e:
        logging.error(f"Error downloading PDF {pdf_id}: {e}")
        return None





