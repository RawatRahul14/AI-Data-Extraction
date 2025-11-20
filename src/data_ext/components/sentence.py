# === Python Modules ===
from typing import List

# === Utils ===
from data_ext.utils.common import (
    load_spacy_model
)

# === Main Body Function ===
def extract_sentences(
        text: str
) -> List[str]:
    """
    Split raw text into meaningful, well-formed sentences by removing
    newline artifacts and preserving full sentence boundaries.

    Args:
        text (str): String containing text from the pdf

    returns:
        sentences (List[str]): List of the sentences
    """
    try:
        ## === Loading the English Model ===
        nlp = load_spacy_model()

        ## === Extracting the sentences ===
        docs = nlp(text = text)
        sentences = [s.text.strip() for s in docs.sents]

        ## === Cleaning the sentences ===
        sentences = [s.replace("\n", " ").strip() for s in sentences]

        return sentences
    
    except Exception as e:
        raise ValueError(f"Error Extracting the sentences: {e}")