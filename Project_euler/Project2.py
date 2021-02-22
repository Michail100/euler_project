def project2():
    def fib(x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        return fib(x-1) + fib(x-2)
    res = []
    y =0
    while fib(y)<4000000:
        if fib(y)%2 == 0:
            res.append(fib(y))
        y+=1
    return sum(res)
print(project2())