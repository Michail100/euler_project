x,y = map(int,input("Введите два числа: ").split())
a = f"{x*y}"
def project4(a):
    if len(a) == 0:
        return True
    if len(a) == 1:
        return True
    if a[0] == a[-1]:
        project4(a[1:-1])
        return True
    else:
        return False
print(project4(a))