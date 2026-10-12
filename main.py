from torch import chunk

from src.knowledge_agent.Util.logger import Logger
from src.knowledge_agent.Loader.DocumentLoader import DocumentLoader
from src.knowledge_agent.Chunker.DocumentChunker import DocumentChunker
from src.knowledge_agent.Embedder.DocumentEmbedder import DocumentEmbedder

def main():
    # Create a logger instance.
    logger = Logger(__name__).get_logger()

    # Create a DocumentLoader instance.
    loader = DocumentLoader(logger=logger)
    chunker = DocumentChunker(logger=logger)
    embedder = DocumentEmbedder(logger=logger)

    # Get the list of document paths in the knowledge folder.
    file_paths = loader.get_files_path()

    # Load and display the content of each document.
    for path in file_paths:
        # load the file to document and display the content.
        document = loader.load_file_to_document(file_path=path)

        # chunk the document and display the content of each chunk.
        if document:
            chunks = chunker.chunk_document(document=document)
            for i, chunk in enumerate(chunks):
                embedded_chunk = embedder.embed_chunk(document_text=chunk.text)

    return

# enter point of the script.
if __name__ == "__main__":
    main()