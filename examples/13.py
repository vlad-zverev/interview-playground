def a(d: list[int] = []) -> list[int]:
    d.append(1)
    return d


for i in range(5):
    d = a()

print(d)
