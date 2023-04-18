from json import dumps

from notion import query_database, update_database_row
from robert import retrieve_word_definition

# rich text definition for word definition and synonyms
DEF = {"type": "text", "text": {"content": "", }, "annotations": {"color": "default"}, "plain_text": ""}
SYN = {"annotations": {"color": "default", "italic": True}, "plain_text": "", "text": {"content": ""}, "type": "text"}


def get_rows_to_update(database_id: str) -> list:
    """
    Retrieves rows that are missing a definition from the database
    :param database_id: id of the database that have missing data
    :return: a list of rows to update
    """
    database_data = query_database(database_id=database_id)
    return list(filter(lambda x: not x['properties']['Meaning'].get('rich_text'), database_data['results']))


def update_row_with_data(row_to_update):
    """
    Retrieves the definition of a word in a row, updates the latter and make a PATCH call to the db
    :param row_to_update: the row in which the meaning of a word is lacking
    :return:
    """
    i = row_to_update.get('id')
    word_to_retrieve = row_to_update['properties']['Word']['title'][0]['plain_text']
    word_definition, word_synonym = retrieve_word_definition(word=word_to_retrieve)
    rich_text = []
    if word_definition:
        DEF['text']['content'] = word_definition + '\n'
        DEF['plain_text'] = word_definition + '\n'
        rich_text.append(DEF)
    if word_synonym:
        SYN['text']['content'] = word_synonym
        SYN['plain_text'] = word_synonym
        rich_text.append(SYN)
    row_to_update['properties']['Meaning']['rich_text'] = rich_text
    data = dumps({"properties": row_to_update['properties']})
    update_database_row(row_id=i, data=data)
