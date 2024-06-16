# src/optimizean/userid.py

# PyPI Stats retains data for 180 days (https://pypistats.org/about)

import toml
import requests

from src.optimizean.utils import BadRequestError, load_config


# Filter and Summation the number of downloads from parsing data
def check_downloads_in_180(MIRROR_OR_NOT, response):
    if response.status_code == 200:
        data = response.json()["data"]
        mirror_stats = filter(lambda data: data["category"] == MIRROR_OR_NOT, data)
        num_downloads = map(lambda data: data["downloads"], mirror_stats)
        total_downloads_in_180 = sum(num_downloads)

        return total_downloads_in_180

    else:
        raise BadRequestError(f"Request failed with status code {response.status_code}")


# Parsing the number of downloads from pypistats
def sum_downloads_in_180():
    # Load Metadata from toml
    config: dict = load_config()

    # Set Config
    PACKAGE_NAME = config["tool"]["poetry"]["name"]
    PACKAGE_NAME = "numpy"  #  tmp pkg name
    MIRROR_OR_NOT = "without_mirrors"

    # API Requests
    url = f"https://pypistats.org/api/packages/{PACKAGE_NAME}/overall"
    response = requests.get(url)

    # Calculate the number of total downloads recent 180 days
    total_downloads_in_180 = check_downloads_in_180(MIRROR_OR_NOT, response)

    return total_downloads_in_180


if __name__ == "__main__":
    sum_downloads_in_180()
