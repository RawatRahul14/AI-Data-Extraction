# === Python Modules ===
from typing import List
from pydantic import BaseModel, Field

# === AI Agent Output Schema ===
class ExtractedFact(BaseModel):
    """
    Structured representation of a single extracted fact extracted from a sentence.
    Includes the generated key, extracted value, confidence score, and optional
    contextual notes derived strictly from the same sentence.
    """
    key: str = Field(
        ...,
        description = "The extracted attribute name (clean, standardized key)"
    )
    value: str = Field(
        ...,
        description = "The exact text value taken directly from the sentence"
    )
    confidence: float = Field(
        ...,
        description = "Model-generated confidence score for this key:value pair"
    )
    comments: str | None = Field(
        default = None,
        description = "Optional context or clarifications strictly derived from the same sentence"
    )

class KeyValueExtract(BaseModel):
    """
    List of all extracted key-value pairs derived from a single sentence.
    """
    key_value_list: List[ExtractedFact] = Field(
        ...,
        description = "All extracted key-value facts from the sentence."
    )