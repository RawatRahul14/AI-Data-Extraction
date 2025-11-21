# AI-Data-Extraction

A modular pipeline for extracting structured key-value information from PDF documents.  
The system performs PDF text extraction, sentence segmentation, LLM-based information extraction, confidence-based key refinement, and final export to XLSX.

---

## Features

- PDF text extraction using pdfplumber  
- Sentence segmentation using SpaCy  
- LLM-based key:value extraction using gpt-4o-mini  
- Pydantic schema validation for structured outputs  
- Confidence-driven key reuse and refinement  
- Exporting final structured dataset to Excel  
- Modular pipeline architecture (DataExtract and InfoExtract)

---

## Badges

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green)
![OpenAI](https://img.shields.io/badge/OpenAI-gpt--4o--mini-orange)
![SpaCy](https://img.shields.io/badge/SpaCy-NLP-blue)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-success)

---

## Folder Structure

```swift
Directory structure:
└── rawatrahul14-ai-data-extraction/
    ├── README.md
    ├── main.py
    ├── requirements.txt
    ├── research.ipynb
    ├── setup.py
    ├── data/
    │   └── Output.xlsx
    └── src/
        ├── __init__.py
        └── data_ext/
            ├── __init__.py
            ├── components/
            │   ├── __init__.py
            │   ├── extract.py
            │   ├── extract_info.py
            │   └── sentence.py
            ├── pipelines/
            │   ├── __init__.py
            │   ├── extract_data_pipeline.py
            │   └── extract_info_pipeline.py
            ├── schema/
            │   └── __init__.py
            └── utils/
                ├── __init__.py
                └── common.py
```


---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/RawatRahul14/AI-Data-Extraction
cd AI-Data-Extraction
```


### Step 2: Create and Activate Virtual Environment
`On Windows:`
```bash
python -m venv .venv
.venv\Scripts\activate
```

`On Linux/Mac:`
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:
```.env
OPENAI_API_KEY = your_api_key_here
```


---

## Pipeline Overview

### Stage 1: PDF Extraction  
Extract raw text from the PDF using pdfplumber.

### Stage 2: Sentence Splitting  
Split text into well-formed sentences using SpaCy.

### Stage 3: LLM-Based Extraction  
Each sentence is processed by gpt-4o-mini, returning:

- key  
- value  
- confidence  
- comments  

### Stage 4: Confidence-Based Key Merging  
If a key repeats across sentences, confidence logic determines whether to reuse or replace it with a clearer key.

### Stage 5: Export to XLSX  
Final structured data exported to `data/Output.xlsx`.

---

## Running the Pipeline

```bash
python main.py
```