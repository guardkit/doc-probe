"""doc-probe: small, predictable statistics about plain text."""


def word_count(text: str) -> int:
    """Return the number of words in ``text``; words are separated by whitespace only."""
    return len(text.split())
