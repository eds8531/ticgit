
import pickle
import requests
import json
import ast


app_id = '86931dcd'
app_key = 'ed68a9f46caa69102ef0e3a720aeb191'

language = 'en'
word_id = 'grapefruit'

url = 'https://od-api.oxforddictionaries.com/api/v2/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
definition = r.text

print(definition)

# print(ast.literal_eval(definition)['results'][0]['id'])
# print(ast.literal_eval(definition)['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
