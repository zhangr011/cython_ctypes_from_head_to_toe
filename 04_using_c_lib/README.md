
The sources compiler directive gives the path of the C files that setuptools is going to compile and link (statically) into the resulting extension module. In general all relevant header files should be found in include_dirs. Now we can build the project using:

```python
# queue.pyx
# distutils: sources = 3rd/c-algorithms/src/queue.c
# distutils: include_dirs = 3rd/c-algorithms/src/

cimport cqueue
```

```shell
$ python setup.py build_ext -i
```

for dynamic linking:

```shell
$ cd 3rd/c-algorithms/
$ bash autogen.sh
$ ./configure
$ make
$ sudo make install
```

Afterwards the file /usr/local/lib/libcalg.so should exist.

In this approach we need to tell the setup script to link with an external library. To do so we need to extend the setup script to install change the extension setup from

```python
ext_modules = cythonize([Extension("queue", ["queue.pyx"])])
```

to

```python
ext_modules = cythonize([
    Extension("queue", ["queue.pyx"],
              libraries=["calg"])
    ])
```

If the libcalg is not installed in a ‘normal’ location, users can provide the required parameters externally by passing appropriate C compiler flags, such as:

```shell
CFLAGS="-I/usr/local/otherdir/calg/include"  \
LDFLAGS="-L/usr/local/otherdir/calg/lib"     \
    python setup_dy.py build_ext -i
```
Before we run the module, we also need to make sure that libcalg is in the LD_LIBRARY_PATH environment variable, e.g. by setting:

```shell
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
```

Once we have compiled the module for the first time, we can now import it and instantiate a new Queue:

```shell
$ export PYTHONPATH=.
$ python -c 'import queue; Q = queue.Queue()'
```

However, this is all our Queue class can do so far, so let’s make it more usable.

then you can use the queue.Queue like this:

```python
>>> import queue
>>> Q = queue.Queue()
```
