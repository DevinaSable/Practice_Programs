print('What is your name?')
name = input()
print('Hi {}, what is your profession?'.format(name))
prof = input()
if name == 'mana' and prof == 'adv':
    print('Hello Adv. Mohanish Patekar, please have a seat.')
elif name == 'mana' and prof == 'doc':
    print('Wecome Dr. Maheshan')
else:
    print('Hello {}. {}, the receptionist will see you soon'.format(prof, name))