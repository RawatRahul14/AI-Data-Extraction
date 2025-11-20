# === Python Modules ===
import pdfplumber
from pathlib import Path

# === Main Body Function ===
def extract_pdf(
        path: Path | str
) -> str:
    """
    Extracts the textual data from the pdf.

    Args:
        - path (Path | str): Path to the input file.

    return:
        - text (str): Extracted text in string form.
    """
    if not path:
        raise ValueError("Path argument is not provided.")

    try:
        ## === Opening file ===
        with pdfplumber.open(path) as file:
            text = "/n".join([p.extract_text() for p in file.pages if p.extract_text()])

        return text
    
    except Exception as e:
        raise ValueError(f"Error extracting data: {e}")