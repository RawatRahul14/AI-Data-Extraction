# === Python Modules ===
from typing import List, Dict
import pandas as pd

# === Components ===
from data_ext.components.extract_info import extraction

# === Info Extraction Pipeline ===
class InfoExtract:
    def __init__(
            self,
            sentences: List[str]
    ):
        self.sentences = sentences

    def list_to_xlsx(
            self,
            list_info: List[Dict[str, str | None]],
            filename: str = "data/Output.xlsx"
    ):
        try:
            ## === Convert list of dicts into DataFrame ===
            df = pd.DataFrame(list_info)

            ## === Save to Excel ===
            df.to_excel(filename, index = False)

            return filename
        
        except Exception as e:
            raise ValueError(f"Error exporting to XLSX: {e}")

    def main(self):
        try:
            ## === Text -> Dictionary ===
            list_info = extraction(self.sentences)

            ## === Save to XLSX ===
            file_path = self.list_to_xlsx(list_info)

            return {
                "data": list_info,
                "file_path": file_path
            }
        
        except Exception as e:
            raise ValueError(f"Error running the LLM Pipeline: {e}")