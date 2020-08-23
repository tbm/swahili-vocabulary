"""
Define Anki models for Swahili vocabulary
"""

import genanki

STYLE = """
.card {
  font-family: arial;
  font-size: 24px;
  text-align: center;
  color: black;
  background-color: white;
}
"""

VOCAB_REVERSE = genanki.Model(
    1380469471,
    "Swahili vocabulary note",
    fields=[
        {
            "name": "Swahili",
        },
        {
            "name": "English",
        },
    ],
    templates=[
        {
            "name": "Vocabulary Card (front)",
            "qfmt": "{{Swahili}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{English}}",
        },
        {
            "name": "Vocabulary Card (back)",
            "qfmt": "{{English}}",
            "afmt": "{{FrontSide}}<hr id=\"answer\">{{Swahili}}",
        },
    ],
    css=STYLE,
)
