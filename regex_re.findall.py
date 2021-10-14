import re

string = """My number is 8976179141 and
            my husband's number is 9822847123"""

# a sample regular expression to find digits
regex = '\d+'

match = re.findall(regex, string)
print(match)


