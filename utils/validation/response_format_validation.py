
class ResponseFormatValidation:
    def validate_brotli_response(self, payload: dict):
        assert payload.get("brotli") is True, (
            f"brotli | expected: True | actual: {payload.get('brotli')}"
        )

        assert payload.get("method") == "GET", (
            f"method | expected: GET | actual: {payload.get('method')}"
        )

        headers = payload.get("headers")
        assert isinstance(headers, dict), (
            f"headers | expected: dict | actual: {type(headers)}"
        )


        assert "Accept-Encoding" in headers, (
            f"headers.Accept-Encoding | expected present | actual keys: {list(headers.keys())}"
        )

        origin = payload.get("origin")
        assert isinstance(origin, str) and origin, (
            f"origin | expected non-empty str | actual: {origin}"
        )
