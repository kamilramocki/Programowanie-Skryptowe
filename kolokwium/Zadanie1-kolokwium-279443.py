import requests

ipstack_api_key = "YOUR_API_KEY"


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
