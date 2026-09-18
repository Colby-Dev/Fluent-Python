def factorial2(n):
    return 1 if n < 1 else n * factorial2(n-1)

print(factorial2(42))

#Using list comps
print([factorial2(n) for n in range(42)])