def test (n) :
    a = [1 ,1]
    while len(a) < n: a += [sum(a[-2:])]
    return a[:n]
n=10
print("\n find the first",n,"fibonacci number:")
print(test(n))