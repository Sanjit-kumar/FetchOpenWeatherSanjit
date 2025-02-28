import requests


def get_coordinates_from_api(location_input):

    api_key = "f897a99d971b5eef57be6fafa0d83239"
    base_url1 = "http://api.openweathermap.org/geo/1.0/direct"
    base_url2 = "http://api.openweathermap.org/geo/1.0/zip"


    if location_input.isdigit():
        url = f"{base_url2}?appid={api_key}&zip={location_input},us"
    else:
        url = f"{base_url1}?appid={api_key}&q={location_input}"

    try:

        response = requests.get(url)
        response.raise_for_status()


        if location_input.isdigit():

            data = response.json()
            return {
                "latitude": data["lat"],
                "longitude": data["lon"],
                "name": data["name"]
            }
        else:

            data = response.json()
            if data:
                return {
                    "latitude": data[0]["lat"],
                    "longitude": data[0]["lon"],
                    "name": data[0]["name"]
                }
            else:
                return f"No location found for '{location_input}'."

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return f"Location not found or invalid input for '{location_input}'."
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Error connecting to the API: {req_err}"


def main():

    locations = input("Enter multiple locations (city, state, zip code), separated by commas: ").split(",")
    for location in locations:
        location = location.strip()
        coords = get_coordinates_from_api(location)
        if isinstance(coords, dict):
            print(
                f"Coordinates for {coords['name']}: Latitude - {coords['latitude']}, Longitude - {coords['longitude']}")
        else:
            print(coords)


if __name__ == "__main__":
    main()
