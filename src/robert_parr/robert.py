import requests
from bs4 import BeautifulSoup

from robert_parr import logger

URL = "https://dictionnaire.lerobert.com/definition/{word}"


def retrieve_word_definition(word: str) -> (str, str):
    """
    Retrieves a word's definition from the Le Robert dictionary
    :param word: the word to retrieve the definition of
    :return: a tuple (word's definition, word's synonyms)
    """
    default = ""
    to_request = word.lower().replace(' ', '-')
    page = requests.get(URL.format(word=to_request))
    page_parser = 'html.parser'
    soup = BeautifulSoup(page.content, page_parser)
    word_syn = soup.findAll('span', {"class": "d_rvh"}) or soup.findAll('span', {"class": "d_xpl"})
    synonyms = ', '.join([w.text for w in word_syn])
    word_def = soup.findAll('span', {"class": "d_dfn"})
    multiple_defs = [t.text for t in word_def]
    if len(multiple_defs) == 1:
        d = multiple_defs[0]
    elif len(multiple_defs) > 1:
        d = '\n'.join([f"{i + 1}. {m}" for i, m in enumerate(multiple_defs)])
    else:
        d = default
    s = synonyms if synonyms else default
    logger.info(f"Scrapped data:\n{d}\n_{s}_")
    return d, s
