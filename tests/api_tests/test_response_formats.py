from utils.validation.response_format_validation import ResponseFormatValidation


class TestResponseFormats(ResponseFormatValidation):

    def test_brotli_returns_valid_response(self, http_client, config):
        response = http_client.get(f"{config.base_url}/brotli")

        assert response.status_code == 200
        assert response.headers["Content-Type"].startswith("application/json")
        assert response.headers.get("Content-Encoding") == "br"

        payload = response.json()
        super().validate_brotli_response(
            payload=payload,
        )
