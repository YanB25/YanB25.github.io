---
title: Week One Assignment
categories: Assignment
date: 2018-03-07 16:46:00 +0800
published: true

---
# Ch7
## 7-1 ~ 7-5
``` python
# 7-1
carName = input('what car do you like?\n')
print('let me see if I could find you a(n) {}'.format(carName))

# 7-2
num = input('how many people are there?\n')
if num > 8:
    print('no available table')
else:
    print('ok')

# 7-3
num = input('please input a number')
if num % 10 == 0:
    print('multiply of 10')
else:
    print('not multiply of 10')

# 7-4
while True:
    food = input('plase enter a food in pizza\n')
    if food == 'quit':
        break
    else:
        print('we will put {} into pizza.'.format(food))

# 7-5
while True:
    age = input('enter you age\n')
    if age < 3:
        print('free!')
    elif age < 12:
        print('10 dollars')
    else:
        print('15dollars')
```
## 7-6 ~ 
``` python
# 7-6
sandwich_orders = ['one', 'two', 'three']
finished_sandwich = []
for sand in sandwich_orders:
    print('I made your {} sandwich'.format(sand))
    finished_sandwich.append(sand)
print('done!')
for sand in finished_sandwich:
    print('we have {}'.format(sand))

```