import json

list = ['beans', 'carrots', 'potatoes', 'ham', 'lamb', 'chicken']

print(type(list))

new = json.dumps(list)

print(type(new))