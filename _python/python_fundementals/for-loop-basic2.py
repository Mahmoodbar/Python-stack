def biggie_size(a):
   
    for i in range (len(a)):
        if a[i]>0:
            a[i]='big'
    return a
print(biggie_size([-1,2,3,-8]))

def count_positive(a):
    count = 0
    for i in range(len(a)):
        if i >0:
            count+=1
    a[len(a)-1] = count
    return a
print(count_positive([3, 5, -1, 2,5]))

def sum_total(a):
    sum = 0
    for i in range(len(a)):
        sum = sum+a[i]
    return sum
print(sum_total([-2,2,5,7]))

def average(a):
    avg = 0
    sum=0
    for i in range(len(a)):
        sum =sum+a[i]
    avg = sum/len(a)
    return avg
print(average([5,7,9,8,7]))
        
def length(a):
    return len(a)
print(length([4,6,8,3]))


def min(a):
    if len(a)<0:
        return False
    min=a[0]
    for i in range(len(a)):
        if a[i]<min:
            min=a[i]
    return min
print(min([5,3,2,1,7,8]))


def max(a):
    if len(a)<0:
        return False
    max=a[0]
    for i in range(1,len(a)):
        if a[i]>max:
            max=a[i]
    return max
print(max([5,3,2,1,7,8]))

def ultimate(a):
    myDictonary = {'sum': 0, 'avg': 0, 'min': a[0], 'max': a[0], 'length': len(a)}
    for i in range(len(a)):
        if a[i]<myDictonary['min']:
            myDictonary['min'] = a[i]
        if a[i]>myDictonary['max']:
            myDictonary['max'] = a[i]
        myDictonary ['sum'] = myDictonary['sum'] + a[i]
        myDictonary['avg']=myDictonary ['sum'] / len(a)
    return myDictonary
print(ultimate([7,8,2,6]))



def reverse_list(a):
    for i in range(0, (len(a)-1)//2):
        temp = a[i]
        a[i] = a[len(a)-1-i]
        a[len(a)-1-i] = temp
    return a
print(reverse_list([81,5,1,3]))