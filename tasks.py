from dotenv import load_dotenv
from document_loader import load_pdfs_from_directory
from text_splitter import split_documents
from vector_store import create_vector_store
from chat_model import create_rag_chain
from logger_config import logger
from rich.console import Console
from rich import print
import sys
import argparse

def setup_argument_parser():
    """
    Setup command-line argument parser for greater flexibility in configuring paths.
    """
    parser = argparse.ArgumentParser(description="MediCompanion Chatbot Setup")
    parser.add_argument(
        '--dataset-dir', type=str, default='rag-datasets', help='Directory for the PDF datasets'
    )
    return parser

def load_environment_variables():
    try:
        logger.info("Loading environment variables...")
        load_dotenv()
        logger.info("Environment variables loaded successfully.")
    except Exception as e:
        logger.error("Failed to load environment variables.", exc_info=True)
        sys.exit(1)

def load_documents_from_directory(directory: str):
    try:
        logger.info(f"Starting to load documents from the directory: {directory}...")
        docs = load_pdfs_from_directory(directory)
        logger.info(f"Successfully loaded {len(docs)} documents.")
        return docs
    except Exception as e:
        logger.error("Failed to load documents.", exc_info=True)
        sys.exit(1)

def split_documents_into_chunks(docs):
    try:
        logger.info("Splitting documents into smaller chunks...")
        document_chunks = split_documents(docs)
        logger.info(f"Split documents into {len(document_chunks)} chunks.")
        return document_chunks
    except Exception as e:
        logger.error("Failed to split documents.", exc_info=True)
        sys.exit(1)

def create_vector_store_from_chunks(document_chunks):
    try:
        logger.info("Creating the vector store...")
        vector_store = create_vector_store(document_chunks)
        logger.info("Vector store created successfully.")
        return vector_store
    except Exception as e:
        logger.error("Failed to create vector store.", exc_info=True)
        sys.exit(1)

def initialize_rag_chain(vector_store):
    try:
        logger.info("Initializing the RAG chain...")
        rag_chain = create_rag_chain(vector_store)
        logger.info("RAG chain initialized successfully.")
        return rag_chain
    except Exception as e:
        logger.error("Failed to initialize the RAG chain.", exc_info=True)
        sys.exit(1)

console = Console()
def handle_user_interaction(rag_chain):
    # Welcome message (colored and bold)
    console.print("\n[bold cyan]Welcome to the MediCompanion Chatbot![/bold cyan]")
    console.print("[yellow]Type 'exit' to end the conversation.[/yellow]\n")

    while True:
        try:
            # Get user input (colored)
            user_question = console.input("[green]You: [/green]")

            # Check if the user wants to exit
            if user_question.lower() == 'exit':
                logger.info("User exited the chatbot.")
                console.print("[bold red]Thank you for using MediCompanion. Goodbye![/bold red]\n")
                break

            # Fetch the answer from the RAG chain
            response = rag_chain.invoke(user_question)
            logger.info("Processed user question successfully.")

            # Print the chatbot's response with color
            console.print(f"[bold magenta]MediCompanion:[/bold magenta] [white]{response}[/white]\n")

        except Exception as e:
            logger.error("An error occurred during chatbot interaction.", exc_info=True)
            console.print("[bold red]An error occurred. Please try again.[/bold red]\n")