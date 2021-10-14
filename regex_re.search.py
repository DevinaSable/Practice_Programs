import re

regex = r"([a-zA-z]) (\d+)"
match = re.search(regex, "I was born on June 24")

if match != None:
    print("Match at index % s")
