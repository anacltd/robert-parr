import requests

from robert_parr import config

URL_QUERY = "https://api.notion.com/v1/databases/{id}/query"
URL_UPDATE = "https://api.notion.com/v1/pages/{id}"

HEADERS = {
    "Authorization": "Bearer " + config.get('notion', 'secret'),
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


def query_database(database_id: str) -> dict:
    """
    Send a POST request to a db to retrieve data from it
    :param database_id: the id of the db you want to retrieve the data of
    :return:
    """
    return requests.request(
        method="POST",
        url=URL_QUERY.format(id=database_id),
        headers=HEADERS
    ).json()


def update_database_row(row_id: str, data: str):
    """
    Send a PATCH request to a db to update a specific row
    :param row_id: the id of the row you want to update
    :param data: the data you want to fill the row with
    :return:
    """
    return requests.request(
        method="PATCH",
        url=URL_UPDATE.format(id=row_id),
        headers=HEADERS,
        data=data
    )
