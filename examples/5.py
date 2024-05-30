class A:
    def __init__(self, v: str) -> None:
        self.v = v

    def __add__(self, other: "A") -> "A":
        self.v += other.v
        return self


t = A("1") + A("2")

t = t + t

print(t.v)
