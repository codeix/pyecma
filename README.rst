.. image:: https://travis-ci.org/codeix/pyecma.svg?branch=master
    :target: https://travis-ci.org/codeix/pyecma

.. contents::

Description
===========

PyEcma is Python JavaScript interperter.


Examples
========

Import PyEcma
-------------
>>> import pyecma


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
3.0
>>> print(app.b)
7.0
>>> print(app.c)
9.0
>>> print(app.d)
18.0
>>> print(app.e)
54.0

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
>>> print(app.factorial(5))
120.0


Bidirectional
-------------



>>> js = r"""
...     a = 1;
...     function increment(){
...         a++;
...     }
... """
>>> app = pyecma.parse(js)
>>> print(app.a)
1.0
>>> app.a = 2
>>> app.a
2
>>> app.increment()
>>> print(app.a)
3.0



