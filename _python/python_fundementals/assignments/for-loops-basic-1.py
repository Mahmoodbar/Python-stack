for x in range (0,151,1):
    print(x)
for y in range (5,1000,1):
    print (5*y)

for x in range (1,100,1):
    if x%5 == 0 :
         print('coding')
    elif x%10 == 0:
        print('codingDojo')

sum = 0
for x in range(500000):
    if x % 2 != 0:
        sum = sum + x
print(sum)

for x in range(2018,0,-4):
    if x%2==0:
        print(x)

lowNum = 5
highNum = 30
mult = 2
for x in range (lowNum,highNum+1):
        if x%2==0:
            print(x)
