# === Python Modules ===
from typing import List, Dict
import spacy
from spacy.cli import download

# === Try loading english data; if missing, download it automatically ===
def load_spacy_model(
        model_name: str = "en_core_web_sm"
):
    """
    Downloads the english model from spacy if not available.

    Args:
        - model_name (str): Name of the model to download/load.

    returns:
        - model: Loaded model
    """
    try:
        return spacy.load(model_name)
    
    except OSError:
        print(f"Model: {model_name} not founded. Downloading...")
        download(model = model_name)
        return spacy.load(model_name)