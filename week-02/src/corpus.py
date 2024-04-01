import string
import re
from PyPDF2 import PdfReader


class Corpus:
    """
    Loads the text from a PDF file and converts it to plain text
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self._load_text()

    def _load_text(self):
        """
        Loads the text
        """
        print("Loading the text...")
        pdf_text = ""
        with open(self.file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_text += page.extract_text()
        print("Done!")
        return pdf_text

    def _lower_text(self):
        """
        Lowers the text
        """
        self.text = self.text.lower()

    def _remove_punctuation(self):
        """
        Removes punctuation from the text
        """
        translator = str.maketrans("", "", string.punctuation)
        self.text = self.text.translate(translator)

    def _remove_digits(self):
        """
        Removes digits from the text
        """
        translator = str.maketrans("", "", string.digits)
        self.text = self.text.translate(translator)

    def _remove_roman_numerals(self):
        """
        Removes Roman numerals from the text
        """
        self.text = re.sub(r"\b[IVXLCDM]+\b", "", self.text)

    def process_text(
        self,
        lower_text: bool = True,
        remove_punctuation: bool = True,
        remove_digits: bool = True,
        remove_roman_numerals: bool = True,
    ) -> None:
        """
        Public method to process the text
        """
        if remove_roman_numerals:
            self._remove_roman_numerals()
        if lower_text:
            self._lower_text()
        if remove_punctuation:
            self._remove_punctuation()
        if remove_digits:
            self._remove_digits()

    def get_text(self):
        """
        Get all text
        """
        return self.text

    def get_words(self):
        """
        Get all words from the text
        """
        return self.text.split()
