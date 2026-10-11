import os
from pprint import pformat
from unstructured.partition.auto import partition
from unstructured.chunking.title import chunk_by_title
from unstructured.documents.elements import Element
from unstructured.staging.base import convert_to_dict

help("unstructured.chunking")  # This will display the help information for the unstructured library.

from src.knowledge_agent.Util.logger import Logger
from src.knowledge_agent.Util.Settings import settings


class DocumentLoader:
    def __init__(self, logger: Logger):
        # logger instance.
        self.logger = logger

        # knowledge folder path from settings.
        self.knowledge_folder = settings.knowledge_folder


    def get_documents_path(self) -> list[str]:
        """
        Get the list of document paths in the knowledge folder.

        Returns:
            list[str]: List of document paths.
        """
        try:
            # Get the list of document paths in the knowledge folder.
            documents_path = [
                os.path.join(self.knowledge_folder, file_name)
                for file_name in os.listdir(self.knowledge_folder)
                if os.path.isfile(os.path.join(self.knowledge_folder, file_name))
            ]
            self.logger.info(f"Documents found in {self.knowledge_folder}: {documents_path}")
            self.logger.info("*"*10 + " End of documents list " + "*"*10)
            return documents_path
        except Exception as e:
            self.logger.error(f"Error getting documents path: {e}")
            return []


    def load_document_to_partition(self, document_path: str) -> list[Element]:
        try:
            return partition(filename=document_path)
        except Exception as e:
            self.logger.error(f"Error loading document: {e}")
            return []


    def chunk_partition_by_titles(self, document_elements: list[Element]) -> list[Element]:
        try:
            return chunk_by_title(document_elements)
        except Exception as e:
            self.logger.error(f"Error chunking document: {e}")
            return []


    def display_chunks_content(self, chunks: list[Element]) -> None:
       self.logger.info(f"Document content: {pformat(convert_to_dict(chunks))}")

       return