def spam(divideBy):
    try:                          # check.. why try is used?????
        return 42 / divideBy
    except ZeroDivisionError as e:        # builtin
        print('Error: Invalid Argument: {}'.format(e))        # prints error message under e

print(spam(12))
print(spam(2))
print(spam(0))
print(spam(1))

