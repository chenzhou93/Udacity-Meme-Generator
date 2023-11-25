"""CSV Ingestor module to handle csv file"""
from typing import List
import pandas
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """CSV Ingestor module to handle csv file"""
    allowed_extensions = ['csv']
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quote_model_list = []

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote_model = QuoteModel(row['body'], row['author'])
            quote_model_list.append(new_quote_model)

        return quote_model_list
