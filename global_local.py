# use of global nad local scope

def spam():                               # function declaration
    global eggs                      # global statement
    eggs = 'spam'                      # value assigned

eggs = 'Global'                          # value assigned out side the function
spam()                             # function called
print(eggs)                         # printed global value
