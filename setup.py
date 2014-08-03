from setuptools import setup, find_packages
import os

version = '1.0'

def alltests():
    import os
    import sys
    import unittest
    # use the zope.testrunner machinery to find all the
    # test suites we've put under ourselves
    import zope.testrunner.find
    import zope.testrunner.options
    here = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
    args = sys.argv[:]
    defaults = ["--test-path", here]
    options = zope.testrunner.options.get_options(args, defaults)
    suites = list(zope.testrunner.find.find_suites(options))
    return unittest.TestSuite(suites)

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='pyecma',
      version=version,
      description="Javascript interpreter written in python",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Interpreters',
        'Operating System :: OS Independent',
        ],
      keywords='Python3, Python, Javascript, ECMA, ECMAScript, grako',
      author='Samuel Riolo',
      author_email='samuel.riolo@googlemail.com',
      url='---',
      license='lgpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      test_suite='__main__.alltests', 
      install_requires=[
          'setuptools',
          'grako',
          # -*- Extra requirements: -*-
      ],
      tests_require=[
        'zope.testrunner',
      ],
      entry_points={
          'console_scripts': ['pyecma = pyecma.console:run'],
      },
      )
