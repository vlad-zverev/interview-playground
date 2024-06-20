class P:
    def __init__(self) -> None:
        print(1)


class A(P):
    def __init__(self, a: int) -> None:
        super().__init__()
        print(a)

    def __new__(cls, *a, **k) -> "A":
        print(1)
        return super().__new__(cls)

    def __call__(self) -> None:
        print(1)

    def __str__(self) -> str:
        return "1"

    def __getitem__(self, v) -> None:
        return v

    def __enter__(self) -> int:
        print(1)
        return 1

    def __exit__(self, *a) -> None:
        print(1)

    def __len__(self) -> int:
        return 1

    def __bool__(self) -> bool:
        print(1)
        return True


print(1)

a = A(1)

print(a)
a()
print(a[1])
print(len(a))

with a as b:
    print(b)

if a:
    print(1)
