def print_number(n: int):
    print(n)

    def decorator(func):
        print(100)

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            print(result + 1)

            return result

        return wrapper

    return decorator


@print_number(10)
def func1():
    return 20


@print_number(30)
@print_number(40)
def func2():
    return 50


func1()

f2 = func2()

print(f2)
