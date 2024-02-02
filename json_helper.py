import json


def save_json_string_into_file(json_string: str, file_path: str):
    # Open a file in write mode
    with open(file_path, "w") as f:
        # Write the JSON string to the file
        f.write(json_string)


def read_file_as_string(file_path: str):
    content: str = ''

    # Open the file in read mode
    with open(file_path, "r") as f:
        # Read the file as a string
        content = f.read()

    return content


def json_string_to_data(json_string: str):
    data = json.loads(json_string)
    return data


def data_to_json_string(data):
    data = json.dumps(data, default=lambda x: x.__dict__, indent=4)
    return data
