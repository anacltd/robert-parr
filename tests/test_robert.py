import pytest

from robert_parr.robert import robert_lookup

TEST_WORDS = [
    (
        "tester", (
            '1. Soumettre à des tests.\n'
            '2. Contrôler, éprouver.\n'
            '3. Disposer de ses biens par testament, faire un testament.',
            'essayer, expérimenter'
        )
    ),
    (
        "programmation", (
            "1. Établissement, organisation des programmes (cinéma, radio, télévision).\n"
            "2. Élaboration et codification d'un programme (4).",
            'Langages de programmation (ex. basic, cobol, fortran, pascal).'
        )
    ), (
        "python", (
            "Serpent des forêts tropicales d'Afrique et d'Asie, de très grande taille (jusqu'à 10\xa0m),"
            " qui broie sa proie entre ses anneaux avant de l'avaler.",
            ""
        )
    ), (
        "magnanerie", (
            "Local où se pratique l'élevage des vers à soie.",
            ""
        )
    ), (
        "indestructible", (
            "1. Qui ne peut pas être détruit ou semble impossible à détruire.\n"
            "2. Que rien ne peut altérer.",
            "indéfectible"
        )
    )
]


@pytest.mark.parametrize("word,output", TEST_WORDS)
def test_robert_scrapping(word, output):
    assert robert_lookup(word) == output
