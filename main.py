from src.knowledge_agent.Util.logger import Logger
from src.knowledge_agent.Loader.DocumentLoader import DocumentLoader

def main():
    # Create a logger instance.
    logger = Logger(__name__).get_logger()

    # Create a DocumentLoader instance.
    document_loader = DocumentLoader(logger=logger)

    # Get the list of document paths in the knowledge folder.
    documents_path = document_loader.get_documents_path()

    # Load and display the content of each document.
    for document_path in documents_path:
        document_elements = document_loader.load_document(document_path)
        document_loader.display_document_content(document_elements)


    return

# enter point of the script.
if __name__ == "__main__":
    main()