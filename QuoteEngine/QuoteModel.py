"""Defines the Quote structure"""
class QuoteModel():
    """Defines the Quote structure"""
    def __init__(self, quote=None, author=None):
        self.author = author
        self.quote = quote

    def __str__(self):
        return f"\"{self.quote}\" - {self.author}"
