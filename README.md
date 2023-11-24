# Meme Generator
A multimedia application to dynamically generate memes, including an image with an overlaid quote.

# Table of Contents
* Installation
* Usage
* File Structure
* Dependencies
* Contributing
* License
* Contact

# Installation
### Clone the repository:

git clone https://github.com/chenzhou93/Udacity-Meme-Generator.git

### Install the required dependencies:

pip install -r requirements.txt

# Usage
Run the Meme Generator:

python main.py [quote_body] [quote_author] [image_path]
quote_body (optional): The body of the quote.
quote_author (optional): The author of the quote.
image_path (optional): The path to the image file.
If any argument is not provided, a random selection will be used.

The generated meme will be saved in the output directory.

# File Structure
.
├── MemeGenerator.py
├── QuoteEngine
│   ├── CSVIngestor.py
│   ├── DocxIngestor.py
│   ├── Ingestor.py
│   ├── IngestorInterface.py
│   ├── PDFIngestor.py
│   ├── QuoteModel.py
│   ├── TextIngestor.py
│   └── __init__.py
├── README.md
├── _data
│   ├── DogQuotes
│   │   ├── DogQuotesCSV.csv
│   │   ├── DogQuotesDOCX.docx
│   │   ├── DogQuotesPDF.pdf
│   │   ├── DogQuotesTXT.txt
│   │   └── test.txt
│   ├── SimpleLines
│   │   ├── SimpleLines.csv
│   │   ├── SimpleLines.docx
│   │   ├── SimpleLines.pdf
│   │   └── SimpleLines.txt
│   └── photos
│       └── dog
│           ├── xander_1.jpg
│           ├── xander_2.jpg
│           ├── xander_3.jpg
│           └── xander_4.jpg
├── app.py
├── meme.py
├── requirements.txt
└── templates
    ├── base.html
    ├── meme.html
    └── meme_form.html

# Dependencies
Pillow
python-docx
pandas
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License.

# Contact
If you have any questions or feedback, feel free to contact me at chenzhoux93@gmail.com.