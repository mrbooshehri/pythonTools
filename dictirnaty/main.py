import sys
import json
import urllib.request 

arg = sys.argv[1]

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{arg}"
data = urllib.request.urlopen(url).read().decode()
obj = json.loads(data)

if type(obj) is dict:
    print ("Word not found")
else:
    word = obj[0]['word']
    meaning = obj[0]['meanings'][0]['definitions'][0]
    definition = meaning ['definition'] 
    synonym = meaning ['synonyms']
    example = meaning ['example']
    print(f"Word: {word}\n\nDefinition:\n{definition}\n\nSynonyms:\n{synonym}\n\nExample:\n{example}") 

