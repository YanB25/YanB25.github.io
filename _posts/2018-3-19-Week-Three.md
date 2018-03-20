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

# 5-8至5-10
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
    if new_user in user:
        print('has been used!')
    else:
        user.append(new_user)
```



```
