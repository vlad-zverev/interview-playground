class A:
    def __init__(self, len: int) -> None:
        self.len = len

    def __len__(self) -> int:
        return len(self)


a = A(10)

print(len(a))
