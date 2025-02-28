def test_get_coordinates_from_api_valid_city_name():
    expected_response = [{"lat": 37.7749, "lon": -122.4194, "name": "San Francisco"}]
    with patch("FetchSanjitOpenWeather.requests.get") as mock_get:
        mock_get.return_value.json.return_value = expected_response
        mock_get.return_value.status_code = 200

        result = get_coordinates_from_api("San Francisco")
        assert result == {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "name": "San Francisco",
        }


def test_get_coordinates_from_api_valid_zip_code():
    expected_response = {"lat": 40.7128, "lon": -74.006, "name": "New York"}
    with patch("FetchSanjitOpenWeather.requests.get") as mock_get:
        mock_get.return_value.json.return_value = expected_response
        mock_get.return_value.status_code = 200

        result = get_coordinates_from_api("10001")
        assert result == {
            "latitude": 40.7128,
            "longitude": -74.006,
            "name": "New York",
        }


def test_get_coordinates_from_api_location_not_found():
    with patch("FetchSanjitOpenWeather.requests.get") as mock_get:
        mock_get.return_value.json.return_value = []
        mock_get.return_value.status_code = 200

        result = get_coordinates_from_api("InvalidCity")
        assert result == "No location found for 'InvalidCity'."


def test_get_coordinates_from_api_invalid_response_404():
    with patch("FetchSanjitOpenWeather.requests.get") as mock_get:
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value.status_code = 404

        result = get_coordinates_from_api("InvalidInput")
        assert result == "Location not found or invalid input for 'InvalidInput'."


def test_get_coordinates_from_api_request_exception():
    with patch("FetchSanjitOpenWeather.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("API connection error")

        result = get_coordinates_from_api("ConnectionErrorCase")
        assert result == "Error connecting to the API: API connection error"
