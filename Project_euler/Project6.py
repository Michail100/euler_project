def project6(n):
    def sumkv(n):
        b = [i**2 for i in range(1,n+1)]
        c = sum(b)
        return c
    def kvsum(n):
        d = [i for i in range(1,n+1)]
        e = sum(d)
        f = e**2
        return f
    return kvsum(n) - sumkv(n)



print(project6(100))
