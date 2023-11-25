"""Ingestor Interface"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Ingestor Interface"""
    allowed_extensions = []
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Given a file type, decide if class can ingest this type of file"""
        text = path.split('.')
        ext = text[-1]
        #print("file extension: " + ext)
        if ext in cls.allowed_extensions:
            return True
        return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Generate Quote object instances by extracting file content"""
