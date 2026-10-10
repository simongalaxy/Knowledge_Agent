import os
from pprint import pformat
from unstructured.partition.auto import partition
from unstructured.documents.elements import Element


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


    def load_document(self, document_path: str) -> list[Element]:
        try:
            return partition(filename=document_path)
        except Exception as e:
            self.logger.error(f"Error loading document: {e}")
            return []


    def display_document_content(self, document_elements: list[Element]) -> None:
        """
        Display the content of the document elements.

        Args:
            document_elements (list[Element]): List of document elements.
        """
        try:
            for i, element in enumerate(document_elements):
                self.logger.info(f"Element No. {i}/{len(document_elements)}: {element.text}")
                self.logger.info(f"Metadata: {pformat(element.metadata.to_dict(), indent=4)}")
                self.logger.info("#"*10 + " End of element " + "*"*10)
            self.logger.info("*"*10 + " End of document content " + "*"*10)

        except Exception as e:
            self.logger.error(f"Error displaying document content: {e}")

        return