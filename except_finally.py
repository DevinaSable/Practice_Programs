def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e:
        print('error : Invalid Argument : {}'.format(e))
    finally:
        print('---Division finished---Ans is---')       # executes everytime with exception


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
