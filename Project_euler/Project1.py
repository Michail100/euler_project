def example1():
    a = int(input())
    res = []
    for i in range(3,a):
        if i%3==0 or i%5==0:
            res.append(i)
    return sum(res)


print(example1())


