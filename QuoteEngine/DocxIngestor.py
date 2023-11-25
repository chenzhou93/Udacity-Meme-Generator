"""Ingestor module to handle docx file"""
from typing import List
from docx import Document
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingestor module to handle docx file"""
    allowed_extensions = ['docx']
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quote_model_list = []

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        doc = Document(path)
        
        for para in doc.paragraphs:
            if para.text != "":
                para_text = para.text.split('-')
                quote = para_text[0]
                author = para_text[1]
                model = QuoteModel(quote, author)
                quote_model_list.append(model)

        return quote_model_list
