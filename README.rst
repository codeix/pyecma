.. contents::

Description
===========

PyEcma is Python JavaScript interperter.


.. code-block:: python
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

