# What Does It Take To Be An Expert At Python? by James Powell.
# https://www.youtube.com/watch?v=7lmCu8wz8ro&t=2479s

from time import time


def ntimes(n):
    def timer(func):
        def f(*args, **kwargs):
            before = time()
            for _ in range(n):
                rv = func(*args, **kwargs)
            after = time()
            print("elapsed", after - before)
            return rv

        return f

    return timer


@ntimes(2)
def add(x, y=10):
    return x + y


@ntimes(3)
def sub(x, y=10):
    return x - y


print("add(10)", add(10))
print("add(20,30)", add(20, 30))
print("add('a', 'b')", add("a", "b"))

print("sub(10)", sub(10))
print("sub(20,30)", sub(20, 30))
