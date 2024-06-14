# PyPI Stats retains data for 180 days (https://pypistats.org/about)

import requests
import toml


class BadRequestError(Exception):
    pass


def check_downloads_in_180(MIRROR_OR_NOT, response):
    if response.status_code == 200:
        data = response.json()["data"]
        mirror_stats = filter(lambda data: data["category"] == MIRROR_OR_NOT, data)
        num_downloads = map(lambda data: data["downloads"], mirror_stats)
        total_downloads_in_180 = sum(num_downloads)

        # print(data[0]["date"], data[-1]["date"])
        # print(total_downloads_in_180)

        return total_downloads_in_180

    else:
        raise BadRequestError(f"Request failed with status code {response.status_code}")


def main():
    with open("./pyproject.toml", "r") as file:
        toml_data = toml.load(file)

    # PACKAGE_NAME = toml_data["tool"]["poetry"]["name"]
    PACKAGE_NAME = "numpy"  #  tmp pkg name
    MIRROR_OR_NOT = "without_mirrors"

    url = f"https://pypistats.org/api/packages/{PACKAGE_NAME}/overall"
    response = requests.get(url)

    total_downloads_in_180 = check_downloads_in_180(MIRROR_OR_NOT, response)

    return total_downloads_in_180


if __name__ == "__main__":
    main()

    print(main())
