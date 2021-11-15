def gcd(a, b):
    """aとbは非負のint型とする。
       aとbの最大公約数を返す。"""
    while a != b:
        if a > b:
            return gcd(a-b, b)
        else:
            return gcd(a, b-a)
    return a

a, b, c = (input().split())
a, b, c = int(a), int(b), int(c)
min = gcd(a, b)

if c % min == 0:
    pass
    # print("x=%d, y=%d" %((c//min)*x, (c//min)*y))
else:
    print("not exist")