from pdf_ingestion import fetch_dataset_from_local_file, fetch_pdf
from pdf_processing import process_pdf
from concurrent.futures import ThreadPoolExecutor
import time

def run_pipeline():
    print("Starting the PDF processing pipeline...")
    
    dataset = fetch_dataset_from_local_file()
    if not dataset:
        print("No dataset found. Exiting pipeline.")
        return
    
    print(f"Dataset loaded with {len(dataset)} PDFs to process.")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for pdf_id, url in dataset.items():
            print(f"Fetching PDF {pdf_id} from URL: {url}")
            pdf_path = fetch_pdf(pdf_id, url)
            if pdf_path:
                print(f"PDF {pdf_id} fetched successfully. Processing...")
                start_time = time.time()  # Start timing
                future = executor.submit(process_pdf, pdf_id, pdf_path, start_time)
                futures.append(future)
            else:
                print(f"Failed to fetch PDF {pdf_id} from URL: {url}")

    # Wait for all futures to complete
    for future in futures:
        try:
            future.result()  # Raises exception if the function call failed
        except Exception as e:
            print(f"An error occurred during processing: {e}")

    print("PDF processing pipeline completed.")

if __name__ == "__main__":
    run_pipeline()



