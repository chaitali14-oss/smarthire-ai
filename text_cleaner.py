
import re


def clean_resume_text(text: str) -> str:
    """Normalize whitespace and remove unwanted control characters."""
    if not isinstance(text, str):
        raise TypeError("Resume text must be a string.")

    # Replace non-breaking spaces with regular spaces.
    text = text.replace("\u00a0", " ")

    # Remove control characters while preserving newlines and tabs.
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)

    # Collapse repeated spaces and tabs.
    text = re.sub(r"[ \t]+", " ", text)

    # Remove unnecessary spaces around newlines.
    text = re.sub(r" *\n *", "\n", text)

    # Limit excessive blank lines to at most two consecutive newlines.
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
