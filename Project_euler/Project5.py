b = int(input("Введите максиальное число от 1 до n: "))
def project5(a):
    c = []
    for i in range(1,b+1):
        if a%i == 0:
            c.append(i)
            if len(c) == b:
                return a
    c.clear()
    return project5(a+b)

print(project5(232792500))