import os
from pprint import pformat
from typing import List

from docling.document_converter import DocumentConverter
from docling.datamodel.document import DoclingDocument


from src.knowledge_agent.Util.logger import Logger
from src.knowledge_agent.Util.Settings import settings

class DocumentLoader:
    def __init__(self, logger: Logger):
        # logger instance.
        self.logger = logger

        # knowledge folder path from settings.
        self.knowledge_folder = settings.knowledge_folder
        self.temp_folder = settings.temp_folder
        
        self.document_converter = DocumentConverter()


    def get_files_path(self) -> list[str]:
            """
            Get the list of document paths in the knowledge folder.
    
            Returns:
                list[str]: List of document paths.
            """
            try:
                # Get the list of document paths in the knowledge folder.
                files_path = [
                    os.path.join(self.knowledge_folder, file_name)
                    for file_name in os.listdir(self.knowledge_folder)
                    if os.path.isfile(os.path.join(self.knowledge_folder, file_name))
                ]
                self.logger.info(f"Files found in {self.knowledge_folder}: {files_path}")
                self.logger.info("*"*10 + " End of files list " + "*"*10)
                return files_path
            except Exception as e:
                self.logger.error(f"Error getting files path: {e}")
                return []

    def save_markdown_to_file(self, markdown_text: str, output_path: str) -> None:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown_text)
            self.logger.info(f"Markdown content saved to {output_path}.")
        except Exception as e:
            self.logger.error(f"Error saving markdown to file: {e}")
        return
    
    def save_result_to_json(self, result, output_path: str) -> None:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result.model_dump_json(indent=4))
            self.logger.info(f"Result saved to {output_path}.")
        except Exception as e:
            self.logger.error(f"Error saving result to JSON file: {e}")
        return


    def load_file_to_document(self, file_path: str) -> DoclingDocument | None:
        try:
            # Convert the document to text using DocumentConverter
            result = self.document_converter.convert(file_path)
          
            self.save_markdown_to_file(
                markdown_text=result.document.export_to_markdown(), 
                output_path=os.path.join(self.temp_folder, f"{result.document.origin.filename.replace(".", "_")}.md")
                )
            self.save_result_to_json(
                result=result, 
                output_path=os.path.join(self.temp_folder, f"{result.document.origin.filename.replace(".", "_")}.json")
            )

            self.logger.info(f"Document {file_path} loaded successfully.")
            # self.logger.info(f"Document content: /n%s", result.document.export_to_markdown())
            # self.logger.info("*"*10 + " End of document content " + "*"*10)
            return result.document
        except Exception as e:
            self.logger.error(f"Error loading document: {e}")
            return None


   