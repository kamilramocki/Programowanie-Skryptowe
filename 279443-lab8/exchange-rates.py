import requests
from datetime import datetime, timedelta


def get_current_rate(currency):
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/")
    data = response.json()
    return data["rates"][0]["mid"]


def get_last_5_days_rates(currency):
    today = datetime.now().date()
    rates = {}
    for i in range(1, 6):
        date = today - timedelta(days=i)
        formatted_date = date.strftime("%Y-%m-%d")
        response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{formatted_date}/")
        if response.status_code == 404:
            print(f"Brak danych dla daty: {formatted_date}")
            continue
        data = response.json()
        rates[formatted_date] = data["rates"][0]["mid"]
    return rates


def display_rates(currency):
    current_rate = get_current_rate(currency)
    print(f"Aktualny kurs {currency}: {current_rate}")

    last_5_days_rates = get_last_5_days_rates(currency)
    print("Kursy z ostatnich 5 dni:")
    for date, rate in last_5_days_rates.items():
        print(f"{date}: {rate}")
        difference = rate - current_rate
        print(f"Różnica: {difference}")


currency = input("Podaj kod waluty (np. USD): ")
display_rates(currency)
