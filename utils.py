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


# counter = [0]


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, value):
        # global counter
        # counter[0] = counter[0] + 1
        return (
            isinstance(value, Point)
            and self.x == value.x
            and self.y == value.y
        )

    def __hash__(self):
        return self.x + self.y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y)
