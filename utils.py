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


def color(color_num):
    # Black: 30, Red: 31, Green: 32, Yellow: 33
    # Blue: 34, Magenta: 35, Cyan: 36, White: 37
    print(f'test test [{color_num}misThisRed?[0m test test')
