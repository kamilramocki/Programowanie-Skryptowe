import requests

ipstack_api_key = "43963cd91845a30c3ef783e2190dd2c8"


def get_location(ip):
    ipstack_url = f"http://api.ipstack.com/{ip}?access_key={ipstack_api_key}"
    ipstack_response = requests.get(ipstack_url)
    ipstack_data = ipstack_response.json()
    city = ipstack_data["city"]
    country = ipstack_data["country_name"]
    latitude = ipstack_data["latitude"]
    longitude = ipstack_data["longitude"]
    return city, country, latitude, longitude


print(get_location("8.8.8.8"))
