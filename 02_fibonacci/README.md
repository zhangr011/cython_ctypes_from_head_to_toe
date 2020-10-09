Build the extension with the same command used for the hello_cython.pyx:

```shell
$ python setup.py build_ext --inplace
```

Then run the fib.py:

```shell
$ python ./fib.py
```

The result looks like this:

```shell
fib_py took 0.0016863346099853516 seconds
fib_c took 7.867813110351562e-06 seconds
```
