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
* "Custom Summarizer": Extracts a concise summary of the document. The summary logic adapts to the length of the document, ensuring that short documents get shorter summaries while longer ones are summarized more comprehensively.
