from time import time

file_v = 'text'
file = '2023/Day6/input/' + file_v + '.txt'

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

@timer
def main():
    pass
main()
