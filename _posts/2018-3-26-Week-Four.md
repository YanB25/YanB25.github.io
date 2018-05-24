---
title: Week Four Assignment (PART I)
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

# 7-7
while True:
    pass

```

# Chp 8
``` python
# 8-1
def display_message():
    print('I am learning function！‘)

display_message()

# 8-2
def favourite_book(title):
    print("my favourite book is {}".format(title))
favourite_book("Harry Poter")

# 8-3
def make_shirt(size, label):
    print('the size is {} and label is {}'.format(size, label))
make_shirt('M', 'hello world')
make_shirt(label="Show me your code", size="XL")

# 8-4
def make_shirt(size="L", label="I love Python"):
    print('the size is {} and label is {}'.format(size, label))
make_shirt()
make_shirt(size="M")
make_shirt(label="other")

# 8-5
def describe_city(city, contry="china"):
    print("{} is in {}".format(city, contry))
describe_city('Beijing')
describe_city('Guangzhou')
describe_city('Texas')

# 8-6
def city_country(city, country):
    print("{}, {}".format(city, country))
city_country('Beijing', 'China')
city_country('Shanghai', 'China')
city_country('Shandong', 'China')

# 8-7
def make_album(singer, song):
    return {singer: song}
print(make_album('Liu Ruoying', 'Weilai'))

# 8-8
dic = {}
while True:
    singer = input('enter singer name(enter q to quit)  ')
    if (singer == 'q'):
        break
    song = input('enter song:  ')
    dic[singer] = song
print(dic)

```