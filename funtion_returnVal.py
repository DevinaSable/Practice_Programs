# function return none value

spam= print('hello!')
spam is None


# funtion return a statement
import random
# declared function
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'                    # return keyword followed by statement
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Reply hazy, try again'
    elif answerNumber == 4:
        return 'my reply is no'
    elif answerNumber == 5:
        return 'yes'
    elif answerNumber == 6:
        return 'Concentrate and try again'
    elif answerNumber == 7:
        return 'Outlook is not so great'
    elif answerNumber == 8:
        return 'Very doubtful'
    elif answerNumber == 9:
        return 'Ask again later'

r = random.randint(1, 9)
fortune = getAnswer(r)        # called a function
print(fortune)
