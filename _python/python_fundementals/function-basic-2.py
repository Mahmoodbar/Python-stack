def countdown(a):
    for a in range (a,0,-1):
        print(a)

print(countdown(9))

def printreturn(a,b):
    print(a)
    return b
print(printreturn(5,7))

def first_length(a):
    sum = a[0] + len(a)
    return sum

print(first_length([1,2,3,4,5,6,10]))

def values(a):
    b = []
    if len(a) < 2:
        return False
    for x in range(len(a)):
        if a[1] < a[x]:
            b.append(a[x])
    return b


print(values([5,4,2,1,8]))


def length_value(a,c):
    b = []
    for i in range (a):
        b.append(c)
    return b
print(length_value(8,7))
