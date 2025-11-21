# === Pipelines ===
from data_ext.pipelines.extract_data_pipeline import DataExtract
from data_ext.pipelines.extract_info_pipeline import InfoExtract

# === Main file ===
def main():
    try:
        print(">>>>>>>> Data Extraction Pipeline Started <<<<<<<<")
        sentences = DataExtract().main()
        print(">>>>>>>> Data Extraction Pipeline Completed <<<<<<<<")

        print(">>>>>>>> Info Extraction Pipeline Started <<<<<<<<")
        file = InfoExtract(sentences = sentences).main()
        print(file.get("file_path"))
        print(">>>>>>>> Info Extraction Pipeline Compeletd <<<<<<<<")

    except Exception as e:
        raise ValueError(f"Error running main.py: {e}")
    
if __name__ == "__main__":
    main()