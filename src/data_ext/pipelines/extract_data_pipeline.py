# === Python Modules ===
from pathlib import Path

# === Components ===
from data_ext.components.extract import extract_pdf
from data_ext.components.sentence import extract_sentences

# === Data Extraction Pipeline ===
class DataExtract:
    def __init__(
            self,
            data_path: str | Path
    ):
        self.data_path = data_path

    def main(self):
        try:
            ## === PDF -> Text ===
            text = extract_pdf(self.data_path)

            ## === Text -> Sentences ===
            sentences = extract_sentences(text = text)

            return sentences
        
        except Exception as e:
            raise ValueError(f"Error running the DataExtract Pipeline: {e}")