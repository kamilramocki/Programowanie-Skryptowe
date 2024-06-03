import requests


def test_xss(url, params):
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>", "'><script>alert('XSS')</script>"]
    for payload in payloads:
        injected_params = {key: payload for key in params.keys()}
        response = requests.get(url, params=injected_params)
        if payload in response.text:
            print(f"Potential XSS vulnerability detected with payload: {payload}")
        else:
            print(f"No vulnerability detected with payload: {payload}")


url = "http://example.com/search"
params = {"query": "test"}
test_xss(url, params)
