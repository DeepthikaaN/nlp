import re

patterns = [
    ("[0-9]+", "THe student strenght is but the perfect score is "),
    ("[A-Z][a-z]+", "Athi and Meenakshi handle the NLP"),
    ("[aeiou]+", "Natual Language processing Essentials"),
    ("[a-z]+@[a-z]+\.com", "Gmail is person@gmail.com")
    ]

for pattern, text in patterns:
    print("Pattern", pattern)
    print("Text", text)
    matches = re.findall(pattern, text)
    if matches:
          print("Matches found", matches)
    else:
        print("NO matches found")
    
