from dotenv import load_dotenv
from document_loader import load_pdfs_from_directory
from text_splitter import split_documents
from vector_store import create_vector_store
from chat_model import create_rag_chain

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Load documents
    print("Document Loading Started...")
    docs = load_pdfs_from_directory('rag-datasets')
    
    print("Document Splitting Started..")
    document_chunks = split_documents(docs)

    # Initialize embeddings model and create vector store
    print("Vector Store Creation started...")
    vector_store = create_vector_store(document_chunks)
    print(f"Vector store created with {len(document_chunks)} chunks.")

    # Create RAG chain
    rag_chain = create_rag_chain(vector_store)

    print("Welcome to the MediCompanion Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_question = input("You: ")
        
        # Check if user wants to exit
        if user_question.lower() == 'exit':
            print("Thank you for using MediCompanion. Goodbye!")
            break

        # Fetch the answer
        response = rag_chain.invoke(user_question)

        # Print the final output
        print("MediCompanion:", response)

if __name__ == "__main__":
    main()
