import ollama

from knowledge_agent.Util.logger import Logger
from knowledge_agent.Util.Settings import settings


class DocumentEmbedder:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.embedding_model = settings.ollama_embedding_model


    def embed_chunk(self, document_text: str) -> list:
        """
        Embed the document text using the Ollama embedding model.

        Args:
            document_text (str): The text of the document to be embedded.

        Returns:
            list: A list of embeddings for the document.
        """
        single = ollama.embed(
            model=self.embedding_model,
            input=document_text
        )
        embedded_text = single['embeddings'][0]
        return embedded_text
