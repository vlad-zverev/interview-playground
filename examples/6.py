class A:
    def __init__(self, a: int) -> None:
        print(a)

    def __call__(self) -> None:
        print(1)

    def __enter__(self) -> int:
        print(1)
        return 1

    def __exit__(self, *a) -> None:
        print(1)


print(1)

a = A(1)

with a as b:
    print(b)
    a()

print(1)
