from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.txt').read()
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
        "Programming Language :: Python",
        "Programming Language :: Python3",
        ],
      keywords='Python3, Python, Javascript, ECMA, ECMAScript, grako',
      author='Samuel Riolo',
      author_email='samuel.riolo@googlemail.com',
      url='---',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'build': ['grako']
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
