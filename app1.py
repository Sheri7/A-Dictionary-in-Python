
import json
import difflib

from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),1,cutoff=0.7)) > 0:
        yn = input("Did you mean %s instead ?? Y if yes, N if no :: " %get_close_matches(w,data.keys(),1,cutoff=0.7)[0])
        if yn == "Y" :
            return data[get_close_matches(w,data.keys(),1,cutoff=0.7)[0]]
        else :
            return "Word Not Found !! "

    else :
        return "Word does nt exists"

word = input("Enter the word :: ")

output = (translate(word.lower()))

if type(output) == list :
    for item in output :
        print(item)
else :
    print(output)
