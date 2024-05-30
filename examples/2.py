def a(d: list[int], n: int) -> None:
    d.append(n)


d: list[int] = []


for i in range(10, 0, -1):
    a(d, i)

d.pop(0)

d = sorted(d)

print(d)
