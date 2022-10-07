import timeit


def f(a):
    return a ** 3


def mem(fun):
    cache = {}

    def wrap(*args):
        args, *_ = args
        if args in cache:
            return cache[args]
        else:
            res = fun(args)
            cache[args] = res
        return res
    return wrap


@mem
def f2(a):
    return a ** 3
print(timeit.timeit('f2(552212)', setup='from __main__ import f2', number=10000000))
print(timeit.timeit('f2(552212)', setup='from __main__ import f2', number=10000000))
print(timeit.timeit('f(552212)', setup='from __main__ import f', number=10000000))
print(timeit.timeit('f(552212)', setup='from __main__ import f', number=10000000))


# print(f(55222))
# print(f2(55222))