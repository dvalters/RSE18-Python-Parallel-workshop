The fundamental nature of Cython can be summed up as follows: Cython is Python with C data types.

Cython is Python: Almost any piece of Python code is also valid Cython code. (There are a few Limitations, but this approximation will serve for now.) The Cython compiler will convert it into C code which makes equivalent calls to the Python/C API.

But Cython is much more than that, because parameters and variables can be declared to have C data types. Code which manipulates Python values and C values can be freely intermixed, with conversions occurring automatically wherever possible. Reference count maintenance and error checking of Python operations is also automatic, and the full power of Python’s exception handling facilities, including the try-except and try-finally statements, is available to you – even in the midst of manipulating C data.

## Cython Hello World

As Cython can accept almost any valid python source file, one of the hardest things in getting started is just figuring out how to compile your extension.

So lets start with the canonical python hello world:

```python 
print("Hello World")
```

Save this code in a file named helloworld.pyx. Now we need to create the setup.py, which is like a python Makefile (for more information see Source Files and Compilation). Your setup.py should look like:

```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("helloworld.pyx")
)
```

To use this to build your Cython file use the commandline options:

```
$ python setup.py build_ext --inplace
```

Which will leave a file in your local directory called helloworld.so in unix or helloworld.pyd in Windows. Now to use this file: start the python interpreter and simply import it as if it was a regular python module:

```
>>> import helloworld
Hello World
```
