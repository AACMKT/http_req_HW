import requests

from datetime import datetime, timedelta

now = (datetime.now(tz=None))
before = str((datetime.now(tz=None)).date() - timedelta(days=2))
dt_from = datetime.strptime(before, '%Y-%m-%d')

to_date = int(now.timestamp())
from_date = int(dt_from.timestamp())

url = "https://api.stackexchange.com/2.3/questions?fromdate={}" \
      "&todate={}&order=desc&sort=activity&tagged=python&site=stackoverflow".format(from_date, to_date)
response = requests.get(url)
data = response.json()
count = 0
for d in data['items']:
    count += 1
    print(f'Title of the question №{count}: "{d["title"]}"')
    print(f'Link to the question №{count}: "{d["link"]}"')
