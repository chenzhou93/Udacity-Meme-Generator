"""Ingestor module to handle PDF file"""
from typing import List
import subprocess
import os
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingestor module to handle PDF file"""
    allowed_extensions = ['pdf']
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quote_model_list = []

        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        txt_path = './_data/DogQuotes/pdfToText.txt'
        exe = subprocess.call(['pdftotext','-layout', path, txt_path])

        txt_file = open(txt_path, "r")
        content = txt_file.readlines()

        for line in content:
            line_tmp = line.strip('\n\r').strip()
            if len(line_tmp) > 0:
                quote = line_tmp.split('-')[0]
                author = line_tmp.split('-')[1]
                model = QuoteModel(quote, author)
                quote_model_list.append(model)

        txt_file.close()
        os.remove(txt_path)

        return quote_model_list
