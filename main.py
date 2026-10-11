from torch import chunk

from src.knowledge_agent.Util.logger import Logger
from src.knowledge_agent.Loader.DocumentLoader import DocumentLoader
from src.knowledge_agent.Chunker.DocumentChunker import DocumentChunker

def main():
    # Create a logger instance.
    logger = Logger(__name__).get_logger()

    # Create a DocumentLoader instance.
    document_loader = DocumentLoader(logger=logger)
    document_chunker = DocumentChunker(logger=logger)

    # Get the list of document paths in the knowledge folder.
    file_paths = document_loader.get_files_path()

    # Load and display the content of each document.
    for path in file_paths:
        # load the file to document and display the content.
        document = document_loader.load_file_to_document(file_path=path)

        # chunk the document and display the content of each chunk.
        if document:
            chunks = document_chunker.chunk_document(document=document)

    return

# enter point of the script.
if __name__ == "__main__":
    main()