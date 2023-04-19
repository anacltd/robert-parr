from json import JSONDecodeError

import requests

from robert_parr import config, logger

URL_QUERY = "https://api.notion.com/v1/databases/{id}/query"
URL_UPDATE = "https://api.notion.com/v1/pages/{id}"

HEADERS = {
    "Authorization": "Bearer " + config.get('notion', 'secret'),
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


class HttpError(Exception):
    pass


def _request(method: str, url: str, **kwargs):
    """ Handles an HTTP request """
    try:
        response = requests.Session().request(method, url, **kwargs)
        response.raise_for_status()
        try:
            results = response.json()
        except JSONDecodeError:
            results = response.content
    except requests.exceptions.HTTPError as http_error:
        response = http_error.response
        try:
            json_response = response.json()
            msg = json_response.get("msg") or json_response.get("error")
        except ValueError:
            msg = response.text or None
        logger.error(msg)
        raise HttpError(
            f'HTTP error {response.status_code} for request {method} {response.url} ({msg})') from http_error
    except ValueError:
        results = None
    return results


def query_database(database_id: str):
    """
    Send a POST request to a db to retrieve data from it
    :param database_id: the id of the db you want to retrieve the data of
    :return:
    """
    return _request(
        method="POST",
        url=URL_QUERY.format(id=database_id),
        headers=HEADERS
    )


def update_database_row(row_id: str, data: str):
    """
    Send a PATCH request to a db to update a specific row
    :param row_id: the id of the row you want to update
    :param data: the data you want to fill the row with
    :return: the status code of the request
    """
    _request(
        method="PATCH",
        url=URL_UPDATE.format(id=row_id),
        headers=HEADERS,
        data=data
    )
