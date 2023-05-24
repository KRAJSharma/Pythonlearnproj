import json

data = json.load(open("data.json"))

def transalte(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else :
        print("Word is not present in dictionary ")
    

word = input("Enter word you want to search : \n")
output = transalte(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

