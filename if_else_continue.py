# example if continue syntax
while True:                        #to keep the whole logic run in loop
    print('Who are you')
    name = input()
    if name != 'rusi':
        continue                  #continue loop
    print('Hello Rusi, What is the password?  (It is a Fish)')
    passw = input()
    if passw == 'swordfish':
        break                      #terminate loop
    else:
        print('Try Again!')  # startover
print('Access Granted')



