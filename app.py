import random
import os
import requests
from flask import Flask, render_template, abort, request

# Import Ingestor and MemeEngine classes
from MemeGenerator import MemeGenerator as MemeEngine
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes_tmp = []
    for file in quote_files:
        quotes_tmp.append(Ingestor.parse(quote_files))

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs_tmp = []
    for file in os.listdir(images_path):
        file_path = os.path.join(images_path, file)
        imgs.append(file_path)

    return quotes_tmp, imgs_tmp


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    #
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img_size = len(imgs)
    quote_size = len(quotes)

    img = imgs[random.randint(0, img_size)]
    quote = quotes[random.randint(0, quote_size)]

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    #
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    r = requests.get(request.form['image_url'])

    img_path = f'./_data/photos/dog/xander_tmp_{random.randint(10, 100)}.png'

    with open(img_path, 'wb') as img:
        img.write(r.content)
        print('saved')
        print('tmp : ' + img_path)

    quote = QuoteModel(quote=request.form['body'], author=request.form['author'])
    path = meme.make_meme(img_path, quote.quote, quote.author)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
