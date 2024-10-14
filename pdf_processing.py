from custom_summarizer import custom_summarizer
from custom_keyword_extractor import custom_keyword_extractor
from mongodb_storage import insert_pdf_metadata, update_pdf_data
import time
import logging

def process_pdf(pdf_id, pdf_path, start_time):
    print(f"Processing PDF {pdf_id} located at {pdf_path}.")
    try:
        # Read the PDF content and process it
        summary = custom_summarizer(pdf_path)
        keywords = custom_keyword_extractor(pdf_path)

        # Prepare the metadata and update MongoDB
        metadata = {
            "pdf_id": pdf_id,
            "path": pdf_path,
            "summary": summary,
            "keywords": keywords
        }

        # Insert metadata into MongoDB (if it's a new PDF)
        insert_pdf_metadata(metadata)

        # Update the PDF data with the summary and keywords
        update_pdf_data(pdf_id, {"summary": summary, "keywords": keywords})

        processing_time = time.time() - start_time  # Calculate processing time
        print(f"PDF {pdf_id} processed successfully in {processing_time:.2f} seconds.")
        print(f"Summary: {summary}")
        print(f"Keywords: {keywords}")
        
    except Exception as e:
        logging.error(f"Error processing PDF {pdf_id}: {e}")



