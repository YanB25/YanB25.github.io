---
title: Shell Basic
categories: Linux
tag: shell
date: 2017-12-01 16:39:00 +0800
published: true

---
# Define a Variable
To define a variable, simply use `variable-name=value` without and space.  
```sh
$ a=5 # set a to 5
$ b = 5 # Opps, error
$ c=3+2 # Opps, does not work, 
        # which will be explained soon.
```
If you are interesting in the value stored in `c` in the third case above, you can try `echo`
```sh
$ echo $c
3+2
```
Strangely enough, it would output `3+2` instead of `5`, far from our ideal behaviour.  
The correct command to assign `5` to `c` would be discussed soon.
As shown above, `$` is uesd to refer to a variable.
```sh
$ echo a
a
$ echo $a
5
$ vim ${a}.cpp # equivelant to vim 5.cpp
               # {} can be ignored
``` 
# Tree Kinds of Quote
## Single Quote
A single quote will make anything inside it a plain text.
```sh
$ echo 'I am $USER, and today is `date`'
I am $USER, and today is `date`
```
Nothing will be translated.
## Double Quote
Similar to single quote, double quote makes it a string. However, double quote allow `$` to access to the variable and back quote to execute a command.
```sh
$ echo "I am $USER, and today is `date`"
I am yb, and today is 2017年 12月 01日 星期五 18:30:17 CST
```
## Back Quote
Whatever inside the back quote(not a single quote!) would be treated as a command to run.
```sh
$ expr 4 + 2
6
$ a=`expr 4 + 2`
$ echo $a
6
```
# run a shell
put your `bar.sh` to the path below  
`~/.local/bin`
and your script can be executed globally by current user.
