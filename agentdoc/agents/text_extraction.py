import os
from enum import StrEnum, auto
from typing import Union

import pdfplumber


class Extension(StrEnum):
    PDF = auto()


class TextExtractionAgent:
    def extract(self, file_path: str) -> Union[str, None]:
        file_extension = os.path.splitext(file_path)[1][1:].lower()

        if file_extension == Extension.PDF:
            return self.extract_text_from_pdf(file_path)
        else:
            raise TypeError(f"Unsupported file format: {file_extension}")

    def extract_text_from_pdf(self, file_path: str) -> str:
        """Extracts text from a PDF file."""
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text.strip()
