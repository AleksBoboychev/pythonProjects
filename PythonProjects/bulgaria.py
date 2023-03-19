birthday = { 
    "Vasil Levski" : "18/7/1837",
    "Hristov Botev" : "6/1/1848",
    "Georgi Rakovski" : "14/4/1821",
    "Panayot Hitov" : "11/11/1830", 
    "Paisius of Hilendar" : "n/n/1722"   
}

print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in birthday:
    print(name)

print('Who\'s birthday do you want to look up?')
name = input()

if name in birthday:
    print('{}\'s birthday is {}.'.format(name, birthday[name]))
else:
    print('Sadly, we don\'t have {}\'s birthday.'.format(name))