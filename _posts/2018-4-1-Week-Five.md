---
title: Week Five Assignment
categories: Assignment
date: 2018-03-07 16:46:00 +0800
published: true

---
# ch10 
``` python
# 10-1
# assume that there is a file called `learning_py.txt` in current directory
with open('learning_py.txt', 'r') as f:
    s = f.read()
    print(s)
with open('learning_py.txt', 'r') as f:
    for line in f:
        print(line, end='')
with open('learning_py.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')

# 10-2
with open('learning_py.txt', 'r') as f:
    s = f.read()
    print(s.replace('python', 'java'))
with open('learning_py.txt', 'r') as f:
    for line in f:
        print(line.replace('python', 'java'), end='')
with open('learning_py.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.replace('python', 'java'), end='')

# 10-4
with open('guest.txt', 'w') as f:
    content = ""
    while True:
        name = input("please input guest name(q to exit):  ")
        if name == 'q':
            break
        content += name + '\n'
    f.write(content)

# 10-5
reasons = ""
while True:
    reason = input('why you love programming?(q to exit):  ')
    if reason == 'q':
        break
    reasons += reason + '\n'
with open('reasons.txt', 'w') as f:
    f.write(reasons)

# 10-8
try:
    with open('cats.txt') as catFile:
        cats = catFile.read()
        print(cats)
    with open('dogs.txt' as dogFile):
        dogs = dogFile.read()
        print(dogs)
except FileNotFoundError as e:
    print('file not found')
    print(e)

# 10-11
import json
num = input('input you loved number: ')
try:
    num = int(num)
except Exception:
    print('catch error, not number')

with open('loved_num.txt', 'w') as f:
    json.dump(num, f)

```

# ch 11
``` python
# 11- 1
# in city_functions.py
def city_and_country(city, country):
    return "{}, {}".format(city, country)
# in test_citie.py
import unitTest
from city_functions import city_and_country
class TestCities(unitTest.Testcase):
    def test_city_and_function(self):
        self.assertEqual(city_and_country('Peking', 'Chinese'), 'Peking, Chinese')
unitest.main()

# 11-3
import unittest
class Employee(object):
    def __init__(self, firstname, lastname, salary):
        self.fn = firstname
        self.ln = lastname
        self.s = salary
    def give_raise(self, add=5000);
        self.s += add
class EmployeeTest(unittest.Tesecase):
    def setUp(self):
        self.employee = Employee('Yan', 'Ben', 1e5)
    def test_give_default_raise(self):
        old_salary = self.employee.s
        self.employee.give_raise()
        self.assertEqual(old_salary+5000, self.employee.s)
    def test_give_custom_raise(self):
        for i in range(1000):
            old_salary = self.employee.s
            self.employee.give_raise(i)
            self.assertEqual(old_salary+i, self.employee.s)
```