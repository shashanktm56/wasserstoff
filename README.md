# PDF Processing Pipeline
This project is a PDF processing pipeline that fetches, summarizes, and extracts keywords from PDF documents. The summaries and keywords are stored in a MongoDB database.
## Table of Contents
* Features
* Prerequisites
* Setup Instructions
  
## Features
* Fetch PDFs from URLs.
* Process multiple PDFs in parallel.
* Summarize content based on document length.
* Extract relevant keywords.
* Store metadata in MongoDB.

## Prerequisites
Before you begin, make sure you have the following installed:
* Python 3.x
* MongoDB
* Required Python packages

# Setup Instructions
## Clone the Repository
''' git clone  https://github.com/shashanktm56/wasserstoff.git
   cd wasserstoff '''
##  Install Python and Required Packages
* install the required Python packages using pip. The necessary dependencies are listed in the requirements.txt file.
 ''' pip install -r requirements.txt '''
* This will install all the necessary libraries like PyMuPDF, pymongo, requests, and others required for running the pipeline
##  Install and Configure MongoDB
* **Download MongoDB**: Follow the instructions from the official MongoDB website to download and install MongoDB.
* **Start the MongoDB Server**: Once installed, you can start the MongoDB service using the following command
> On Windows, you can start it by running '''mongod.exe'''
# System Requirements
Before running the project, make sure your system meets the following requirements:
## Operating System:
* Works on Windows
## Python Version:
* Python 3.7 or higher
## Python Packages:
Required Python packages are listed in requirements.txt. They will be installed via pip:
* pymupdf (for PDF processing)
* pymongo (for MongoDB integration)
* requests (for fetching PDFs from URLs)
* Other essential libraries (re, json, concurrent.futures, etc.)
## MongoDB:
* MongoDB server installed and running locally or accessible via a remote connection.
## Memory and Processing Power:
* At least 4GB of RAM recommended for processing PDFs and concurrency operations.
* Multi-core CPU recommended for faster parallel processing.


# Explanation of the Solution
## PDF Ingestion & Parsing
* The project starts by fetching a dataset of PDFs from a local file that contains PDF IDs and their corresponding URLs. The system downloads these PDFs if they aren’t already available locally.
* The ingestion process is concurrent (parallel), allowing multiple PDFs to be downloaded and processed simultaneously using Python’s ThreadPoolExecutor. This improves performance and ensures efficient use of system resources.
## Summarization & Keyword Extraction
Each PDF is processed by two core components:
* **Custom Summarizer**: Extracts a concise summary of the document. The summary logic adapts to the length of the document, ensuring that short documents get shorter summaries while longer ones are summarized more comprehensively.
* **Custom Keyword Extractor**: Extracts the most relevant and important keywords from the document. The keyword extraction is based on filtering out common stopwords and selecting domain-relevant terms from the text.
* These components have been carefully designed to handle various document lengths (short, medium, long) with appropriate summarization and keyword extraction logic.
## MongoDB Integration
The pipeline stores and updates the data (such as summary and keywords) for each PDF in a MongoDB database.
* **Initial Insertion**: When a new PDF is processed, its metadata is inserted into MongoDB.
* **Updates**: If a PDF has already been processed, its data (e.g., summary or keywords) is updated without creating duplicate entries. This ensures consistency and avoids redundancy in the database.
##  Concurrency & Performance Optimization
* The pipeline efficiently handles multiple PDFs concurrently using threading, which accelerates the overall processing speed, particularly for larger datasets.
* Error handling ensures that if any PDF fails to download or process, the pipeline logs the error without disrupting the processing of other PDFs.
* The design optimizes memory management by closing resources after use (such as PDF file handles) and handles corrupted or large files gracefully.
 ## Error Handling
The solution includes robust error handling at every stage:
* Errors during PDF downloading or processing are logged without stopping the pipeline.
* For corrupted or unreadable PDFs, appropriate error messages are displayed, and these files are skipped to avoid interruptions.
##  Scalability and Extensibility
* The solution is easily scalable. It can process a large number of PDFs by adjusting the number of worker threads for concurrent execution.
* The solution is also extensible—you can easily customize the summarization and keyword extraction algorithms as per specific domain requirements.
