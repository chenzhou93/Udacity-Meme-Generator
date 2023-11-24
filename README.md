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
.<br/>
├── MemeGenerator.py<br/>
├── QuoteEngine<br/>
│   ├── CSVIngestor.py<br/>
│   ├── DocxIngestor.py<br/>
│   ├── Ingestor.py<br/>
│   ├── IngestorInterface.py<br/>
│   ├── PDFIngestor.py<br/>
│   ├── QuoteModel.py<br/>
│   ├── TextIngestor.py<br/>
│   └── __init__.py<br/>
├── README.md<br/>
├── _data<br/>
│   ├── DogQuotes<br/>
│   │   ├── DogQuotesCSV.csv<br/>
│   │   ├── DogQuotesDOCX.docx<br/>
│   │   ├── DogQuotesPDF.pdf<br/>
│   │   ├── DogQuotesTXT.txt<br/>
│   │   └── test.txt<br/>
│   ├── SimpleLines<br/>
│   │   ├── SimpleLines.csv<br/>
│   │   ├── SimpleLines.docx<br/>
│   │   ├── SimpleLines.pdf<br/>
│   │   └── SimpleLines.txt<br/>
│   └── photos<br/>
│       └── dog<br/>
│           ├── xander_1.jpg<br/>
│           ├── xander_2.jpg<br/>
│           ├── xander_3.jpg<br/>
│           └── xander_4.jpg<br/>
├── app.py<br/>
├── meme.py<br/>
├── requirements.txt<br/>
├── templates<br/>
│   ├── base.html<br/>
│   ├── meme.html<br/>
│   └── meme_form.html<br/>
└── tree.txt<br/><br/>


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