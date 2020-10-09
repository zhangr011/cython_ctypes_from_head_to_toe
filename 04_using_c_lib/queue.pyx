# queue.pyx

# distutils: sources = 3rd/c-algorithms/src/queue.c
# distutils: include_dirs = 3rd/c-algorithms/src/

cimport cqueue

cdef class Queue:
    cdef cqueue.Queue* _c_queue

    def __cinit__(self):
        self._c_queue = cqueue.queue_new()
        if self._c_queue is NULL:
            raise MemoryError

    def __dealloc__(self):
        if self._c_queue:
            cqueue.queue_free(self._c_queue)
