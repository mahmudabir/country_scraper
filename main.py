from helpers import country_scraper, json_helper, common_helper

file_path: str = 'countries.json'


def main():
    country_raw_data = country_scraper.get_country_raw_data()
    country_list = country_scraper.to_country_list(country_raw_data)
    json_string = json_helper.data_to_json_string(country_list)
    json_helper.save_json_string_into_file(json_string, file_path)

    country_list = []
    country_list = country_scraper.generate_data_from_json_file(file_path)


if __name__ == "__main__":
    main()

    try:
        print('\nPress any key to continue...')
        common_helper.wait_for_key()
    except Exception as ex:
        pass
