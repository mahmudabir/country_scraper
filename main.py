from helper import get_all_countries, generate_json_from_country_data_list, save_json_string_into_file


def main():
    country_data = get_all_countries()
    country_json = generate_json_from_country_data_list(country_data)
    save_json_string_into_file(country_json, 'countries.json')


if __name__ == "__main__":
    main()
