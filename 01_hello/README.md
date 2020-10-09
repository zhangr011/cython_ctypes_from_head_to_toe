To use this to build your Cython file use the commandline options:

```bash
$ python setup.py build_ext --inplace
```

Which will leave a file in your local directory called hello_cython.so in unix or hello_cython.pyd in Windows. Now to use this file: start the python interpreter and simply import it as if it was a regular python module:

```python
>>> import hello_cython
hello cython.
```

To use ctypes, you need to load the .so file at first, for linux.

```
```
