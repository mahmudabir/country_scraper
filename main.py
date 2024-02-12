from helpers import common_helper, country_scraper, json_helper
from helpers.csv_helper import list_to_csv_file

file_path: str = "countries.json"


def main():
    country_raw_data = country_scraper.get_country_raw_data()
    country_list = country_scraper.to_country_list(country_raw_data)
    json_string = json_helper.data_to_json_string(country_list)
    json_helper.save_json_string_into_file(json_string, file_path)

    country_list = []
    country_list = country_scraper.generate_data_from_json_file(file_path)

    list_to_csv_file(country_list, "country_list.csv")


if __name__ == "__main__":
    main()

    try:
        print("\nPress any key to continue...")
        common_helper.wait_for_key()
    except Exception as ex:
        pass
