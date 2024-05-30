from .b import B


class A:
    def __init__(self, b: B) -> None:
        self._b = b

    def __str__(self) -> str:
        return "a"
