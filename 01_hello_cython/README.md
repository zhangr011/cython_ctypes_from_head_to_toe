To use this to build your Cython file use the commandline options:

```bash
$ python setup.py build_ext --inplace
```

Which will leave a file in your local directory called helloworld.so in unix or helloworld.pyd in Windows. Now to use this file: start the python interpreter and simply import it as if it was a regular python module:

```python
>>> import hello_cython
hello cython.
```
