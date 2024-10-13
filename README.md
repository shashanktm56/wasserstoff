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
