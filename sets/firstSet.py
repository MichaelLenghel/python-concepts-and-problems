# Code adapted from Corey Shafer
print(set("my name is Eric and Eric is my name".split()))

a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)


print(a.intersection(b))
print(b.intersection(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))

arr