import re
from collections import Counter
import fitz  # PyMuPDF

# A simple stopword list. Expand this list based on the domain for better results.
STOPWORDS = set([
    "the", "and", "is", "in", "it", "of", "to", "for", "on", "with", "as", "by", 
    "an", "or", "this", "that", "from", "at", "be", "are", "but", "not", "was", 
    "were", "will", "can", "if", "then", "so", "may", "we", "you", "about", "which", "who", "what", "when"
])

def clean_text(text):
    # Remove punctuation and make everything lowercase
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

def extract_keywords(text):
    # Clean the text
    text = clean_text(text)
    
    # Tokenize text into words
    words = text.split()
    
    # Filter out stopwords and very short words (e.g., < 3 characters)
    filtered_words = [word for word in words if word not in STOPWORDS and len(word) > 3]
    
    # Count word frequencies
    word_counts = Counter(filtered_words)
    
    # Extract the top 10 most common words as keywords
    keywords = [word for word, freq in word_counts.most_common(10)]
    
    return keywords

def custom_keyword_extractor(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        
        for page in doc:
            text += page.get_text()

        keywords = extract_keywords(text)
        print(f"Keywords extracted for {pdf_path}.")
        return keywords
    except Exception as e:
        print(f"Error in keyword extraction for PDF {pdf_path}: {e}")
        return []
