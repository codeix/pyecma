.. contents::

Description
===========

PyEcma is Python JavaScript interperter.


Examples
========

Basic Expressions
-----------------

>>> js = r"""
...     var a = 1 + 2;
...     var b = 1 + 2 * 3;
...     var c = (1 + 2) * 3;
...     var d = (1 + 2) * (3 + 3);
...     var e = (1 + 2 * 4) * ((2 + 1) * 2);
... """
>>> app = pyecma.parse(js)
>>> print(app.a)
3
>>> print(app.b)
7
>>> print(app.c)
9
>>> print(app.d)
18
>>> print(app.e)
54

Function and Recursion
------------------------

>>> js = r"""
...     function factorial (fac){
...       if(fac > 1)
...           return fac * factorial(fac-1);
...       else
...         return fac;
...     }
... """
>>> app = pyecma.parse(js)
>>> app.factorial(5)
120


Bidirectional
-------------



>>> js = r"""
...     a = 1;
...     function increment(){
...         a++;
...     }
... """
>>> app = pyecma.parse(js)
>>> app.a
1
>>> app.a = 2
>>> app.a
2
>>> app.increment()
app.a
3

