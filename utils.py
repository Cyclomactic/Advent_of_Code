from time import time


def timer(func):
    def wrap_function(*args, **kwargs):
        t1 = time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            t2 = time()
            print(f'Function {func.__name__!r} executed in {(t2-t1): .4f}s')
    return wrap_function
