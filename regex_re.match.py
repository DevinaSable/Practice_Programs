import re
def findMonthAndDate(string):

    regex = r"([a-zA-z]+) (\d+)"
    match = re.match(regex, string)

    if match == None:
        print("Not a valid date")
        return
    print("Given Data: %s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Date: %s" % (match.group(2)))

# Driver code
findMonthAndDate("June 24")
print("")
findMonthAndDate("I was born on JUne 24")