from tasks import (
    load_environment_variables,
    load_documents_from_directory,
    split_documents_into_chunks,
    create_vector_store_from_chunks,
    initialize_rag_chain,
    handle_user_interaction,
    setup_argument_parser
)

def main():
    
    parser = setup_argument_parser()
    args = parser.parse_args()
    load_environment_variables()
    docs = load_documents_from_directory(args.dataset_dir)
    document_chunks = split_documents_into_chunks(docs)
    vector_store = create_vector_store_from_chunks(document_chunks)
    rag_chain = initialize_rag_chain(vector_store)
    handle_user_interaction(rag_chain)

if __name__ == "__main__":
    main()
