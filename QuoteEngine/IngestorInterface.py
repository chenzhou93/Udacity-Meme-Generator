"""Ingestor Interface"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Ingestor Interface"""
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Given a file type, decide if class can ingest this type of file"""
        ingestable_file_types = ('txt', 'csv', 'pdf', 'docx')
        text = path.split('.')
        ext = text[-1]
        print("file extension: " + ext)
        if ext in ingestable_file_types :
            return True
        return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Generate Quote object instances by extracting file content"""
