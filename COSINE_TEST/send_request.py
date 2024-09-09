
# import requests
# import json
# url = 'http://127.0.0.1:5002/sldservice1/train_recomender'
# resp = requests.post(url, json = {'json_url':'https://github.com/SehejSoni/converted-jsons'})
# print(resp.text)





import requests
import json
url = 'http://127.0.0.1:5002/sldservice1/recomender'
with open('Pinos Puente 1- TOC_18_05_2021.json') as f: data = json.load(f)
resp = requests.post(url, json = data)
print(resp.text)