import requests
import json
import csv
import config as cfg

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

settings = cfg.settings_local
#settings = cfg.settings_remote
endpoint = settings['endpoint']
token = settings['token']
listID = settings['list']
path = settings['path']
owner = settings['owner']

response = requests.get(endpoint+"lists/"+listID+"/accounts", auth=BearerAuth(token))
follow = response.json()

to_follow={}
for x in range(len(follow)):
    to_follow[x] = follow[x]['acct']
y=len(to_follow)
to_follow[y] = owner

cols = ['account']
with open(path, 'w', newline='') as csvfile:
    fieldnames = ['Account Address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for key in to_follow:
        writer.writerow({'Account Address': to_follow[key]})

