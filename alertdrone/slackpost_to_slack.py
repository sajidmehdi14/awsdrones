# coding: utf-8
import requests
url = 'https://hooks.slack.com/services/!!!!!!!!/AAAAA/zzzzzzzzzzzzz' # Find from slack Web hooks for Apps
data = {"text": "Hallo World from python"}
requests.post(url,  json=data)
