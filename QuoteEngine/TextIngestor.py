"""Ingestor module to handle txt file"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """Ingestor module to handle txt file"""
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quote_model_list = []

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        file = open(path, "r", encoding='UTF-8')
        content = file.readlines()
        for line in content:
            if len(line) > 0:
                quote = line.split('-')[0]
                author = line.split('-')[1]
                model = QuoteModel(quote, author)
                quote_model_list.append(model)

        file.close()

        return quote_model_list
