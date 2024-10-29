import os
import warnings
from langchain_community.document_loaders import PyMuPDFLoader

# Suppress warnings
warnings.filterwarnings("ignore")

def load_pdfs_from_directory(directory):
    """Load PDF files from a specified directory and return their contents."""
    pdf_paths = []

    # Gather PDF file paths
    for root, dirs, files in os.walk(directory):
        pdf_paths.extend(os.path.join(root, file) for file in files if file.lower().endswith('.pdf'))

    # Load documents from each PDF file
    docs = []
    for pdf in pdf_paths:
        print(f"processing pdf: {pdf}")
        try:
            loader = PyMuPDFLoader(pdf)
            docs.extend(loader.load())
        except Exception as e:
            print(f"Error loading {pdf}: {e}")
            
    return docs
