import requests
from bs4 import BeautifulSoup

from helpers import logger

ROBERT_URL = "https://dictionnaire.lerobert.com/definition/{word}"
BKP_URL = "https://www.le-dictionnaire.com/definition/{word}"
HTML_PARSER = 'html5lib'


def robert_lookup(word: str) -> (str, str):
    """
    Retrieves a word's definition from the Le Robert dictionary
    :param word: the word to retrieve the definition of
    :return: a tuple (word's definition, word's synonyms)
    """
    default = ""
    to_request = word.lower().replace(' ', '-')
    page = requests.get(ROBERT_URL.format(word=to_request))
    if page.status_code != 200:
        return "", ""
    soup = BeautifulSoup(page.content, HTML_PARSER)
    word_def = soup.findAll('span', {"class": "d_dfn"})
    if not word_def:
        return "", ""
    word_syn = soup.findAll('span', {"class": "d_rvh"}) or soup.findAll('span', {"class": "d_xpl"})
    synonyms = ', '.join(w.text for w in word_syn)
    multiple_defs = [t.text for t in word_def]
    if len(multiple_defs) == 1:
        d = multiple_defs[0]
    elif len(multiple_defs) > 1:
        d = '\n'.join(f"{i + 1}. {m}" for i, m in enumerate(multiple_defs))
    else:
        d = default
    s = synonyms or default
    logger.info(f"Scrapped data:\n{d}\n_{s}_")
    return d, s


def bkp_lookup(word: str) -> (str, str):
    """
    Retrieves a word's definition from the Le Dictionnaire website (in case none was found in Le Robert)
    :param word: the word to retrieve the definition of
    :return: a tuple (word's definition, word's synonyms)
    """
    to_request = word.lower().replace(' ', '-')
    page = requests.get(BKP_URL.format(word=to_request))
    soup = BeautifulSoup(page.content, HTML_PARSER)
    word_def = soup.findAll('li')
    multiple_defs = [t.text for t in word_def]
    if len(multiple_defs) == 1:
        d = multiple_defs[0]
    elif len(multiple_defs) > 1:
        d = '\n'.join(f"{i + 1}. {m}" for i, m in enumerate(multiple_defs))
    else:
        d = ""
    logger.info(f"Scrapped data:\n{d}")
    return d, ""


def retrieve_word_definition(word: str) -> (str, str):
    """ Tries to retrieve a word's definition from Le Robert, else from Le Dictionnaire """
    result = robert_lookup(word)
    if result == ('', ''):
        result = bkp_lookup(word)
    return result
