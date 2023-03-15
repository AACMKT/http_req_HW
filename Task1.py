import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)

data = response.json()
char = {}
heroes = ["Hulk", "Captain America", "Thanos"]
for hero in data:
    if hero['name'] in heroes:
        char[hero['name']] = hero['powerstats']['intelligence']
res = max(char)

print(f'The most intelligent hero form: {", ".join(map(str, heroes))}; is {res} with IQ {char[res]}')
