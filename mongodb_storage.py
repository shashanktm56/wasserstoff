import pymongo
import logging

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pdf_database"]
collection = db["pdf_collection"]

# Insert PDF metadata into MongoDB, checking for duplicates
def insert_pdf_metadata(metadata):
    try:
        # Use upsert to avoid duplicates
        collection.update_one(
            {"pdf_id": metadata["pdf_id"]},  # Check for existing pdf_id
            {"$set": metadata},              # Update if exists, insert if not
            upsert=True                       # Create a new document if no match is found
        )
    except Exception as e:
        logging.error(f"Error inserting/updating PDF metadata: {e}")

# Update PDF data (summary, keywords, etc.) in MongoDB
def update_pdf_data(pdf_id, data):
    try:
        collection.update_one(
            {"pdf_id": pdf_id},
            {"$set": data},
            upsert=True  # Ensure we create the document if it doesn't exist
        )
    except Exception as e:
        logging.error(f"Error updating PDF {pdf_id}: {e}")
