# === Python Modules ===
import os
import json
from typing import List, Dict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tqdm import tqdm

# === Schema ===
from data_ext.schema import KeyValueExtract

# === Loading API key's ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# === AI Agent Main Body Function ===
def extraction(
        sentences: List[str]
) -> List[Dict[str, str | None]]:
    """
    Process a list of cleaned sentences and extract structured key-value
    information from each one using the AI agent. Returns a flattened list
    of dictionaries where each dictionary represents a single extracted fact
    with its key, value, and optional contextual comments.
    """
    if OPENAI_API_KEY is None:
        raise ValueError("Couldn't find OPENAI_API_KEY.")

    try:
        ## === LLM Model ===
        llm = ChatOpenAI(
            model = "gpt-4o-mini",
            temperature = 0
        ).with_structured_output(KeyValueExtract)

        ## === Prompt ===
        prompt = """
        You are an AI agent that extracts structured key:value facts from a single sentence.

        INPUTS
        sentence:
            A single sentence extracted from a resume/profile/HR-style PDF.

        confidence:
            A dictionary mapping previously generated keys to their confidence scores.
            Example: {"First Name": 0.92, "Current Organization": 0.88}

        OBJECTIVE
        From the given sentence, extract factual attributes about the person and produce
        key:value pairs following a consistent HR-style schema.
        Use confidence to decide whether to reuse existing keys or create improved ones.

        KEY RULES
        Style & Format 
        - Keys must be clean, professional, HR-friendly, and written in Title Case.
        - Keys must describe direct factual attributes (e.g., "Date of Birth", "Current Organization").
        - Values must preserve EXACT wording from the sentence (no paraphrasing).
        - Also the comments can only be the extracted from the original text (no paraphrasing).

        Reuse vs Create (Confidence Logic)
        1. If the sentence expresses a fact that clearly matches an existing key in key_confidence,
            reuse that key (only if the meaning matches with high confidence).
        2. If the existing key feels:
            - too generic
            - too vague
            - mismatched
            - or a more precise key name can be created

            THEN create a NEW key with a clearer, more specific name.
        """

        ## === Key-Confidence Pairs ===
        key_confidence: Dict[str, float] = {}

        ## === Final extracted rows ===
        all_rows: List[Dict[str, str | float | None]] = []

        ## === Process each sentence ===
        for sent in tqdm(sentences, desc = "Extracting Info", ncols = 80):
            response: KeyValueExtract = llm.invoke(
                [
                    ("system", prompt),
                    ("user", f"Extract key-value pairs from this sentence:{sent}.\n\nKeys and confidence Scores: {json.dumps(key_confidence, indent = 2)}")
                ]
            )

            ## === Flatten each ExtractedFact ===
            for fact in response.key_value_list:

                ## === Update key confidence ===
                key_confidence[fact.key] = fact.confidence

                ## === Check if this key already exists in all_rows ===
                updated = False
                for rows in all_rows:
                    if rows.get("key") == fact.key:
                        rows["value"] = fact.value
                        rows["comments"] = fact.comments
                        updated = True
                        break

                ## === Append new row if key not found ===
                if not updated:
                    all_rows.append({
                        "key": fact.key,
                        "value": fact.value,
                        "comments": fact.comments
                    })

        return all_rows

    except Exception as e:
        raise ValueError(f"Error Extracting Key-Value pairs: {e}")