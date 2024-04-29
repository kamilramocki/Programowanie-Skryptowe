import requests

topic = input("Podaj temat: ")

url = (f"https://newsapi.org/v2/everything?q={topic}&from=2024-04-27&sortBy=popularity&apiKey"
       f"=4fab0f3a97954b168268e2b726bd654a")

data = requests.get(url).json()
response = requests.get(url)

for article in data['articles']:
    source_name = article['source']['name']
    title = article['title']
    print(f"Źródło: {source_name}")
    print(f"Tytuł: {title}")
    print()
