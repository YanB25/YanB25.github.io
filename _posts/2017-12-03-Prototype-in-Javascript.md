---
title: Prototype Chain in Javascript
categories: language detail
tag: javascript
date: 2017-12-03 16:39:00 +0800
published: false

---
This article gives a thorough explanation on prototype chain. I assume the reader has a grasp of basic grammar in javascript and knowledge of `object` and `function`.   
It's good if you are familiar with an object-oriented language, but don't be afraid if you don't, as their techniques behind `object` are quite different.  
Javascipt uses a techniques called `prototype chain`to implement inheritance. Before going into details, let's review some basic points.

# Object
## What is Object
Roughly speaking, an object is a combination of datas and operations.  
```js
var person = {
    name: "Benson",
    age: 19,
    greet: function(name) {
        return "hello " + name;
    }
};
```
## Another Way to Define an Object
We can define a constructor as a template to define objects.
```js
// Person is a constructor
function Person(name, age) {
    this.name = name;
    this.age = age;
    this.greet = function(name) {
        return "hello " + name;
    }
}
var person = new Person("Benson", 19);
```
You may feel puzzled by
```js
... new Person("Benson", 19);
```
especially if you are familiar with any oop language.  
Here, `Person` is a constructor, and thus it is a function. In javascript, it is also an object, because every function is a special type of an object.  
What it does exactly is assigning to `person` an instance of a function, with properties `name` and `age` initialized to "benson" and 19.  
## Class Syntax
You may have encountered the keyword `class` in javascript.
```js
class Person {
   constructor(name, age) {
       this.name = name;
       this.age = age;
   }
   greet(name) {
       return "hello " + name;
   } 
};
```
It is worth noting that the expression is no more than a syntax sugar. Javascript does not support real `class`. It will be explained later.

# Prototype
javascript is a object-**based** language, compared to object-oriented languages like `java` and `C++`.  
JavaScript does not have a class definition separate from the constructor. All javascript has is just `object` and its corresponding `constructor`.  
`Constructor` is a function(thus is also an object, to be exact) used to construct an object. 
```js
// in javescript
function Person(name, age) {
    this.name = name;
    this.age = age;
}
var person = new Person("Benson", 19);
```
## Prototype Used to Store Shared Variable
Every instance of a constructor has its own individual copy of variable. It does not make sense to have multiple copies of a shared variable, such as a method. 
To deal with the wasting of space, javescript use an object called `prototype object` to keep the shared variables. Every object keeps a link(or reference) pointing to a prototype object. All the object constructed from the same constructor automatically keeps the same link.
We modidy the code a bit and move the function `greet` to `prototype object`.
```js
// Person is a constructor
function Person(name, age) {
    this.name = name;
    this.age = age;
}
Person.prototype.greet = function(name) {
    return "hello " + name;
}
var p1 = new Person("Lily", 19);
var p2 = new Person("Sary", 20);
p1.greet === p2.greet // true
```
## Detail Behind Prototype

# Prototype Chain
## Prototype Used to Implement Inheritance
## Detail Behind Prototype Chain 

# What is Prototype
``` cpp
// in C++
class Person {
public:
    Person(string name, int age) : name(name), age(age) {}
private:
    string name;
    int age;
};
Person person = new Person("Benson", 19);
```
So, how to implement inheritance and relate similar objects in javascript, you may ask?  
Javascript uses prototypical object(or `prototype`) to allow inheritance.  
So, `prototype` is actually an object that assigns to another object's `constructor` to build an inheritance hierarchy.  
Any object will automatically "get" all the poperties and method from its prototype.
# How to Creat the Hierarchy

