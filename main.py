from helper import *
from json_helper import *

file_path: str = 'countries.json'


def main():
    country_data = get_all_countries()
    country_json = generate_json_from_country_data_list(country_data)
    save_json_string_into_file(country_json, file_path)

    json_string = read_file_as_string(file_path)
    country_list: list[Country] = json_string_to_data(json_string)
    print(country_list)


if __name__ == "__main__":
    main()
