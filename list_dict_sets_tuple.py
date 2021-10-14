# Lists  []

spam= ['cats', 'dogs', 'mice', 'sheeps']   # declaration
print(spam)
print(spam[1])      #getting individual value
print(spam[-1])
print('The {} are afraid of {}'.format(spam[-2], spam[0]))
print(spam[1:3])         #sublist with slices->> end range not included
print(spam[0:-1])
print(spam[:2])           #considers keys 0:2
print(spam[1:])           #considers keys 1: last key
spam2= spam[:]            #copy list
spam.append('cows')       #append item to a list
print(spam)
print(spam2)
print(len(spam))          #getting length
spam[2] = 'bulls'         #changing value with index
print(spam)
spam[3] = spam[2]         #RHS value assigns to LHS
print(spam)
scam=['1','2','three']
spam1= spam + scam        #list concatenation
print(spam1)
spam = spam + ['1', '2', '3', '4']
print(spam)
scam1 = scam * 3          #list replication
print(scam1)
del scam1[2]
print(scam1)

supplies = ['pens', 'pencils','sharpner', 'erasers', 'staplers' ]          # Loops with list
for i, supply in enumerate(supplies):                                      # later???
    print('Index {} in supplies is for {}'.format(str(i), supply))

name = ['rumi', 'rusi', 'mana', 'nash', 'pats']
age = [43, 45, 32, 4, 56]
for n, a, in zip(name, age):                                           # ??? later
    print('{} is {} years ols'.format(n, a))

cat = ['fat', 'orange', 'loud']                      # multiple assignment trick
# size = cat[0]
# color = cat[1]
# disposition = cat[2]                 #or
size, color, disposition = cat
print(color)
a, b = 'Alice', 'bob'
a, b = a, b                            # swaping values
print(a)

spam = 'Hello'
spam += ' World!'        # Augmented assignment operators
print (spam)

hello = ['save world']
hello *= 3
print(hello)

name = ['rumi', 'rusi', 'mana', 'nash', 'pats']
print(name.index('rusi'))                         # index()
name.append('sushi')                              # append()
name.insert(2, 'roodi')                           # insert()
print(name)
name.remove('pats')                              # remove()
print(name)
name.sort()                                      # sort()
print (name)
name.sort(reverse = True)                        # reverse sort()
print(name)
name.sort (key = str.lower)                      # sorting regular aplphabetical order
print(name)
sorted (name)                              # not working
print(name)


# Tuple   ()    ordered, indexed, immutable

pyteam = ('jaya', 'mahesh', 'shiva', 'radha', 2, 5, 6)          # declarion
print(pyteam[0])
print(pyteam[1:5])
print(type(pyteam))                #type of datatype
print(len(pyteam))                 #length of datatype
listname = ['jk','kk', 'dm', 'mn']
tuplenum = (1,2,3,4,5,6,7)
tuple([listname])                     # converting list > tuple   run in console
list((tuplenum))                        #converting tuple > list   run in console
print(listname)
print(tuplenum)


#  Dictionaries and Structuring data          {}   unordered, not indexed, includes key(), value(), item()

mcat = {'size' : 'fat', 'color' : 'orange', 'disposition' : 'loud'}
print(type(mcat))                                     # type of dict
print(len(mcat))
# print(mcat[2])                         #indexing individual throws error
mcat = {'size' : 'fat', 'color' : 'orange', 'disposition' : 'loud'}
for v in mcat.values():                                                        #values()
    print(v)
mcat = {'size' : 'fat', 'color' : 'orange', 'disposition' : 'loud'}
for k in mcat.keys():                                                          #keys
    print(k)
mcat = {'size' : 'fat', 'color' : 'orange', 'disposition' : 'loud'}
for i in mcat.items():                                                         #items
    print(i)
for k, v in mcat.items():
    print('keys: {}, values: {}'.format(k, v))
grp = {'name' : 'varad', 'age' : 20, 'name' : 'jaya', 'age' : 30}
# >>>'jaya' in grp.values()                                        # checking whether keys or value present in dict?
# True
# >>> 'age' in grp.values()
# False
# >>> 'age' in grp.keys()
# True
# >>> 'age' in grp
# True
picnic_items = {'apples' : 5, 'cups': 4, 'glasses': 2}
print('I am bringing {} cups'.format(str(picnic_items.get('cups', 0))))          #get() method
print('I am bringing {} straws'.format(str(picnic_items.get('strwas',0))))         # get() passing default value
if 'straws' not in picnic_items:                                               #checking if item is in the dict and add it
    picnic_items ['straws'] = 2
print(picnic_items)
picnic_items.setdefault('cokes', 4)                                      #setdefault()
print(picnic_items)
picnic_items.setdefault('straws',6)              # dict key values are immutable
print(picnic_items)

                                                             # Pretty Printing

import pprint
message = 'It was a bright cold day in April and, the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)

                                                        # merge two dicts
x = {'a' : 1, 'b' : 2}
y = {'b' : 3, 'c' : 4}
z= {**x, **y}
print(z)


#  set    {}   set([])   unordered, no duplicate, supports maths operations> union, intersection, diff & sym diff

my_set = {1, 2, 3, 4}                  #set initialization
my_set = ([1, 2, 3, 4])
print(type(my_set))
print(len(my_set))
s = {}
print(type(s))           # do no define empty set with curly braces>> it treats as a dict
s = {1, 2, 3, 3, 4, 5, 6, 6, 7, 7}
print(s)                            # set has unique values
# print(s[0])                         # not indexed, unordered
s.add(8)                           #add()
print(s)
s.update([4, 5, 6, 7, 8, 9, 10])     #update([])
print(s)
s.remove(10)                        #remove() >> removes element
print(s)
# s.remove(10)                        # error if element is not present
print(s)
s.discard(9)                       #removes element passed
print(s)
s.discard(9)                   # no error is element is missing
print(s)
s1 = {1, 2, 3, 4}
s2 = ([3, 4, 5, 6])
s3 = {5, 6, 7, 8, 9, 3, 4}
print(s1.union(s2))            # s1 | s2 , union() creates new set containing all elements
# print(s1 | s2 )
print(s1.intersection(s2, s3))   #intersection s1 & s2 & s3  >> ans = {3,4}
print(s1.difference(s2))         # difference()  s1 - s2 >> ans={1, 2}
# print(s2.difference(s1))         # s2 - s2 >> ans = {4}
print(s1.symmetric_difference(s2))   #s1 ^ s2 >> ans = {1, 2, 5, 6}



