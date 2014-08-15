import os
import doctest
import unittest

optionflags = doctest.NORMALIZE_WHITESPACE + doctest.ELLIPSIS



def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        doctest.DocFileSuite('../../README.rst',
                             package='pyecma',
                             optionflags=optionflags)])
    return suite