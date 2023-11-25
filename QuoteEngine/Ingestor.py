"""This module contains one commen class"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor

class Ingestor(IngestorInterface):
    """This is a common place to run varities of Ingestor classes"""
    ingestors = [DocxIngestor, PDFIngestor, TextIngestor, CSVIngestor]
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        #print('ingestor: ' + path)
        for ingestor in cls.ingestors:
            #print(ingestor)
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
 