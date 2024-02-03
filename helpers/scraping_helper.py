import requests
from bs4 import BeautifulSoup


def get_http_response(url: str):
    return requests.get(url, timeout=5)


def find_all_by_class_name(soup: BeautifulSoup, name=None, class_value=None):
    if class_value is None:
        class_value = ''
    return soup.find_all(name, {'class': class_value})


def parse_html_content_as_string(content_str: str, features: str = 'html.parser'):
    return BeautifulSoup(content_str, features)
