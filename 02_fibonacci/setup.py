
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(name = 'fibonacci', sources = ['fibonacci.pyx'])
setup(ext_modules = cythonize(ext))
