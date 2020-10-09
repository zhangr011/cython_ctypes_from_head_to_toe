Cython has a way to visualise where interaction with Python objects and Python’s C-API is taking place. For this, pass the annotate=True parameter to cythonize(). It produces a HTML file.
If a line is white, it means that the code generated doesn’t interact with Python, so will run as fast as normal C code. The darker the yellow, the more Python interaction there is in that line.

```shell
$ python ./setup.py build_ext --inplace
```

then run the main.py

```shell
$ python ./main.py
```

the result looks like this:

```shell
primes_c took 0.0020139217376708984 seconds
primes_python took 0.013990163803100586 seconds
```
