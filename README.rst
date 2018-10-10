Temporarily modify the current process's environment
====================================================

This is a StackOverflow question study which helps understanding: `Temporarily modify the current process's environment <https://stackoverflow.com/a/34333710/1513933>`_.

Getting Started
---------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

To clone the project from Github, you can do::

    git clone https://github.com/laurent-laporte-pro/stackoverflow-q2059482.git

Prerequisites
-------------

To see this study in action, you need Python (version 2 or 3).

To run the tests, you can use:

- `PyTest <https://docs.pytest.org>`_ framework,
- `Tox <https://tox.readthedocs.io>`_ test command line tool.


Installing
----------

This library in not available on `PyPi <https://pypi.org/>`_, you need to install it from source.

Create and activate a `virtualenv <https://virtualenv.pypa.io>`_ an run::

    pip install -e .

Also, to play with the tests, you can install the tests dependencies::

    pip install -e .[test]


Usage Demonstration
-------------------

For the demonstration, we make the assumption that we have some environment variables:

>>> import os

>>> os.environ['DEMO_USER'] = "John"
>>> os.environ['DEMO_HOME'] = "/home/john"
>>> os.environ['DEMO_EDITOR'] = "emacs"
>>> os.environ['DEMO_COLOR'] = "blue"

Now, imagine we have a function which needs to access the environment variables:

>>> def welcome():
...     env = os.environ
...     print("Welcome in your {DEMO_HOME}, {DEMO_USER}!".format(**env))
...     print("The sun is {DEMO_COLOR} and the temperature is {DEMO_TEMP}°C".format(**env))

If we use this function as-is, we wil run into problems: environment variables can have wrong values or be missing. For instance, with this function an exception is raised:

>>> welcome()
Traceback (most recent call last):
  ...
KeyError: 'DEMO_TEMP'

If we want to use this function we need to update the environment variables before the call.
To do that, we use the ``modified_environ`` context manager:

>>> from demo.environ_ctx import modified_environ

>>> with modified_environ('DEMO_EDITOR', DEMO_HOME='castle', DEMO_COLOR='yellow', DEMO_TEMP='26'):
...     welcome()
Welcome in your castle, John!
The sun is yellow and the temperature is 26°C

After that call, the environment variables are restored to their original states:

>>> os.environ['DEMO_USER']
'John'
>>> os.environ['DEMO_HOME']
'/home/john'
>>> os.environ['DEMO_EDITOR']
'emacs'
>>> os.environ['DEMO_COLOR']
'blue'

And extra variables are removed:

>>> os.environ['DEMO_TEMP']
Traceback (most recent call last):
  ...
KeyError: 'DEMO_TEMP'


Authors
-------

* **Laurent LAPORTE** - *Initial work* - `GitHub profile <https://laurent-laporte-pro.github.io/>`_

License
-------

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

Acknowledgments
---------------

* `Sridhar Ratnakumar <https://stackoverflow.com/users/55246/sridhar-ratnakumar>`_   Original Poster on StackOverflow.
