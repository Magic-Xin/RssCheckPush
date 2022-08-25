import json
import os
import requests
import feedparser

from datetime import datetime


def jsonloader(filename):
    with open(filename) as f:
        return json.load(f)


def send_push(title):
    token = os.environ['PUSH_TOKEN']
    url = "https://api2.pushdeer.com/message/push?pushkey=" + token + "&text=" + title
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, headers=headers)
    print(r.text)


def main():
    config = jsonloader('config.json')
    feed = feedparser.parse(config['feed'])
    for entry in feed.entries:
        for keyword in config['keywords']:
            if entry.title.find(keyword) != -1:
                date = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%S%z")
                now = datetime.utcnow()
                if date.date() == now.date() and now.hour - date.hour <= 6:
                    send_push(entry.title+"\n"+entry.published)


if __name__ == '__main__':
    main()
