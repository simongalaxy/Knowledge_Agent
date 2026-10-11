from docling.chunking import HybridChunker


from src.knowledge_agent.Util.logger import Logger
from src.knowledge_agent.Util.Settings import settings


class DocumentChunker:
    def __init__(self, logger):
        # initialize the logger and the HybridChunker instance.
        self.logger = logger
        self.chunker = HybridChunker()

    def display_chunks_content(self, chunks) -> None:
        """
        Display the content of the chunked document elements.

        Args:
            chunks (list): A list of chunked document elements.
        """
        for i, chunk in enumerate(chunks):
            self.logger.info(f"Chunk {i + 1}: {chunk.content}")
            self.logger.info("*" * 10 + " End of chunk content " + "*" * 10)

        return


    def chunk_document(self, document):
        """
        Chunk the document elements using the HybridChunker.

        Args:
            document_elements (list): A list of document elements to be chunked.

        Returns:
            list: A list of chunked document elements.
        """
        chunk_iter = self.chunker.chunk(dl_doc=document)

        # show the content of the chunked document elements.
        self.display_chunks_content(chunks=chunk_iter)

        return chunk_iter

   