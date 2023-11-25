import os
import random

# Import your Ingestor and MemeEngine classes
import argparse
from MemeGenerator import MemeGenerator as MemeEngine
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            #print('now parsing: ' + f)
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.quote, quote.author)
    return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    args = None

    parser = argparse.ArgumentParser(description="Udacity Meme Generator Project")

    parser.add_argument("--path", help="An image path")
    parser.add_argument("--body", help="A string quote body")
    parser.add_argument("--author", help="A string quote author")

    # Parse the command-line arguments
    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
