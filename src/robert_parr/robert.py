import requests
from bs4 import BeautifulSoup

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
    word_syn = soup.find('span', {"class": "d_rvh"}) or soup.find('span', {"class": "d_xpl"})
    word_def = soup.findAll('span', {"class": "d_dfn"})
    multiple_defs = [t.text for t in word_def]
    if len(multiple_defs) == 1:
        d = multiple_defs[0]
    elif len(multiple_defs) > 1:
        d = '\n'.join([f"{i + 1}. {m}" for i, m in enumerate(multiple_defs)])
    else:
        d = default
    s = word_syn.text if word_syn else default
    return d, s
