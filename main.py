from torch import chunk

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
        document_elements = document_loader.load_document_to_partition(document_path)
        chunked_documents = document_loader.chunk_partition_by_titles(document_elements=document_elements)
        document_loader.display_chunks_content(chunks=chunked_documents)


    return

# enter point of the script.
if __name__ == "__main__":
    main()