def project5_2():
    a = int(input("Введите предел от 1 до n: "))
    b = []
    c = a
    while len(b)!=a-1:
        for i in range(2,a+1):
            if c%i==0:
                b.append(i)
            else:
                b.clear()
                c+=a
                break
    return c

print(project5_2())