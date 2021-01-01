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

.cloze {
  font-weight: bold;
  color: blue;
}

.footer {
  position: fixed;
  bottom: 0px;
  margin: auto;
  font-size: 14px;
  text-align: center;
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
        {
            "name": "Swahili_Audio",
        },
    ],
    templates=[
        {
            "name": "Vocabulary Card (front)",
            "qfmt": "{{Swahili}}<br />{{Swahili_Audio}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{English}}',
        },
        {
            "name": "Vocabulary Card (back)",
            "qfmt": "{{English}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Swahili}}<br />{{Swahili_Audio}}',
        },
    ],
    css=STYLE,
)

GRAMMAR = genanki.Model(
    1380469472,
    "Swahili grammar note",
    fields=[
        {
            "name": "Swahili",
        },
        {
            "name": "English",
        },
        {
            "name": "Lesson",
        },
    ],
    templates=[
        {
            "name": "Grammar Card",
            "qfmt": "{{English}}<hr>{{cloze:Swahili}}",
            "afmt": '{{English}}<hr id="answer">{{cloze:Swahili}}<p class=footer>{{Lesson}}</p>',
        },
    ],
    css=STYLE,
    model_type=genanki.Model.CLOZE,
)
