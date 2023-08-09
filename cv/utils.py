import json
import os

from cv.settings import CV_DATA_FILEPATH


def read_cv_data_from_file(filename: str) -> dict:
    """
    Reads and returns CV data from a given JSON file.
    """

    if not os.path.exists(filename):
        raise ValueError(f"Invalid file path provided: {filename}")

    with open(filename) as file:
        data = json.load(file)

    return data


def get_cv_data(section: str | None = None) -> dict | str:
    """
    Fetch CV data for a given section. If no section is provided,
    returns the full CV data.
    """

    data = read_cv_data_from_file(CV_DATA_FILEPATH)
    if not section:
        return data

    if section not in data:
        return {"error": f"No data found for section: {section}"}

    return data[section]
