def с(n: int):
    print(n)

    def d(f):
        print(100)

        def w(*args, **kwargs):
            r = f(*args, **kwargs)

            print(r + 1)

            return r

        return w

    return d


@с(10)
def a():
    return 20


@с(30)
@с(40)
def b():
    return 50


a()


print(b())
