import re

import json_helper
import scraping_helper
from models import Country


def get_country_raw_data():
    # URL of the website
    url = "https://www.scrapethissite.com/pages/simple/"

    # Send a GET request to the URL
    response = scraping_helper.get_http_response(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = scraping_helper.parse_html_content_as_string(response.text)

        # Extract and print the title of the page
        title = soup.title.text.strip()
        print(f"Title: {title}\n")

        content_item = scraping_helper.find_all_by_class_name(soup, "div", {"class": "col-md-4 country"})

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


def to_country_list(country_data: list[str]):
    countries: list[Country] = []

    for country_str in country_data:
        country_str_temp = country_str.strip().split('\n')  # rows in array
        country_name = country_str_temp[0].strip()
        capital_name = country_str_temp[1].split(':')[1].strip()
        population = int(country_str_temp[2].split(':')[1].strip())
        area = float(country_str_temp[3].split(':')[1].strip())

        country: Country = Country(country_name, capital_name, population, area)
        countries.append(country)

    return countries


def generate_data_from_json_file(file_path: str):
    json_string = json_helper.read_file_as_string(file_path)
    country_list: list[Country] = json_helper.json_string_to_data(json_string)
    return country_list
