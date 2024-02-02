import re

import requests
from bs4 import BeautifulSoup

from models import Country
import json


def get_all_countries():
    # URL of the website
    url = "https://www.scrapethissite.com/pages/simple/"

    # Send a GET request to the URL
    response = requests.get(url, timeout=5)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and print the title of the page
        title = soup.title.text.strip()
        print(f"Title: {title}\n")

        content_item = soup.find_all("div", {"class": "col-md-4 country"})

        country_data: list[str] = []

        for item in content_item:
            country = item.text.strip()
            country = re.sub(r" +(?!\n+)", " ", country).strip()
            country = re.sub(r'\n+', '\n', country).strip()
            country = re.sub(r'\n( *)\n', '\n', country)
            country_data.append(country)

        return country_data
    else:
        return []


def generate_json_from_country_data_list(country_data: list[str]):
    countries: list[Country] = []

    for country_str in country_data:
        country_str_temp = country_str.strip().split('\n')  # rows in array
        country_name = country_str_temp[0].strip()
        capital_name = country_str_temp[1].split(':')[1].strip()
        population = int(country_str_temp[2].split(':')[1].strip())
        area = float(country_str_temp[3].split(':')[1].strip())

        country: Country = Country(country_name, capital_name, population, area)
        countries.append(country)

    json_string = json.dumps(countries, default=lambda x: x.__dict__, indent=4)

    return json_string


def save_json_string_into_file(json_string: str, file_path: str):
    # Open a file in write mode
    with open(file_path, "w") as f:
        # Write the JSON string to the file
        f.write(json_string)
