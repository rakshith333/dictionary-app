import json
from difflib import get_close_matches #generates a list

data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:# if the list atleast generates 1 or more strings which has close matches then it will enter the conditional
        yn = input("Did you mean %s instead? Enter Y is yes or N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "the word dooesnt exisit"
        else:
            return "we couldnt understand your entry"
    else:
        return "The word doesnt exisit please double check"


word = input("Enter a word: ")
output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
