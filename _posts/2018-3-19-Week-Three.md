---
title: Week Three Assignment
categories: Assignment
date: 2018-03-19 10:16:40 +0800
published: true

---
# 第五章
## 5-3至5-7
``` python
# 5-3(1)
alien_color = 'red'
if alien_color == 'green':
    print('you get 5 points')
# 5-3(2)
alien_color = 'green'
if alien_color == 'green':
    print('you get 5 points')

# 5-4
if alien_color == 'green':
    print('you get 5 porints')
else:
    print('you get 10 points')

# 5-5
if alien_color == 'green':
    print('you get 5 points')
elif alien_color == 'yellow':
    print('you get 10 points')
else:
    print('you get 15 points')

# 5-6
if age < 2:
    print('baby')
elif age < 4:
    print('learning how to walk')
elif age < 13:
    print('child')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
elif:
    print('the old')

# 5-7
favourite_fruits = ['apple', 'orange', 'banana']
test_lists = ['apple', 'pinapple', 'orange', 'strawberry', 'cocco']
for test_fruit in test_lists:
    if test_fruit in favourite_fruits:
        print('oh, you like {} !'.format(test_fruit))
```

## 5-8至5-10
``` python
# 5-8
ls = ['admin', 'bens', 'walker', 'David', 'Sandy']
for name in ls:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello {}, thank you for logging in again'.format(name))
# 5-9
if ls == []:
    print('we need to find some user!')
else:
    # .... 
    # add codes in 5-8 here
# 5-10
user = ['admin', 'bens', 'walker', 'David', 'Sandy']
other_user = ['admin', 'Kerry', 'Lurra', 'Binchy', 'David']
for new_user in other_user:
    if new_user.lower() in [i.lower() for i in user]:
        print('has been used!')
    else:
        user.append(new_user)

# 5-11
ls = [i for i in range(1, 10)]
for item in ls:
    if item == 1:
        print("1st)
    elif item == 2:
        print("2nd)
    elif item == 3:
        print("3nd")
    else:
        print("{}th".format(item))
```
# Chp 6
## 6-1 ~ 6-
``` python
# 6-1
person = {
    'first_name': 'Bin',
    'last_name': 'Yan',
    'age': 20,
    'city': 'Beijing'
}
for key in person:
    print(key, person[key])

# 6-2
obj = {
    'Sandy': 4,
    'Lolla': 2,
    'Bull': 3,
    'King': 5,
    'Tang': 1
}
for name in obj:
    print(name, obj[name])

# 6-3
obj = {
    'for': 'for loop',
    'if': 'condition',
    'function': 'a map',
    'class': 'template for object',
    'array': 'continueous area for elements'
}
for kw in obj:
    print("{} : {}".format(kw, obj[kw]))

# 6-4
# The solution is the same as 6-3

# 6-7
def getPerson(firstname, lastname, age, city):
    return {
        'firstname': firstname,
        'lastname': lastname,
        'age': age,
        'city': city
    }
p1 = getPerson('Larry', 'lo', 19, 'Beijing')
p2 = getPerson('Sandy', 'Huang', 20, 'Shandong')
persons = [p1, p2]
for person in persons:
    for key in person:
        print(key, person[key])
    print()
```