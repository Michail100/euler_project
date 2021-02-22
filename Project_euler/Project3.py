import math
def project3(x):
    a = []
    r = math.ceil(math.sqrt(x))
    for i in range(2,r):
        if x%i == 0:
            if project3(i) == []:
                a.append(i)
    return a
print(max(project3(600851475143)))