import requests

API_KEY = "6d2SphQoCqDLfEmbqhhKNNrRD1ndXAdJ"
ip = input("Podaj adres IP: ")


def get_shodan_data(ip):
    response = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={API_KEY}")
    data = response.json()
    print("Podstawowe dane:")
    print(f"Nazwa hosta: {data['hostnames']}")
    print(f"Kraj: {data['country_name']}")
    print(f"Miasto: {data['city']}")
    print("Lista otwartych portów:")
    for port in data['ports']:
        print(port)


get_shodan_data(ip)
