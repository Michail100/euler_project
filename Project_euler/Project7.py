def project7(n):
    def cikl():
        a = []
        c = 4
        d = []
        while len(a)!=n-2:
            for i in range(2,c):
                if c%i == 0:
                    c+=1
                    d.clear()
                    break
                else:
                    d.append(c)
                    if len(d)==c-2:
                        a.append(c)
                    if i == c-1:
                        c+=1
            d.clear()
        return a
    return cikl()[-1]
print(project7(10001))