
from ctypes import *

libc = cdll.LoadLibrary('libc.so.6')
libc.printf(b'%s\n', b'hello ctypes.')
