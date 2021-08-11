# this code recursively adds up every integer that comes before a given value

def rec(i, n):
    if n == 0:
        return i
    else:
        return i + rec(i + 1, n-1)

x = int(input("value: "))
print(rec(0, x))
