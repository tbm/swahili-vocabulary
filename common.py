"""
Common functions
"""

from pathlib import Path

CACHE = Path("~/.cache/swahili-anki")


def get_audio(text):
    """
    Get audio file (where available) for a given Swahili text
    """

    text = text.split(',')[0]
    text = text.split(';')[0]
    text = text.split(' (')[0]
    if text.startswith('-a '):
        text = text[3:]
    text = text.lstrip('-')
    text = text.rstrip('-')
    text = text.replace(' ', '_')
    audio = CACHE.expanduser() / f"Sw-ke-{text}.opus"
    if audio.exists():
        return audio
    return ""
