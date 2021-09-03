import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        yesno = input("Did you mean %s instead? y/n: " % get_close_matches(word, data.keys())[0])
        if yesno == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yesno == "n":
            return "Word doesnt exist."
        else:
            "We didnt understand your entry"
    else:
        return "The word doesnt exist. Double check please."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
