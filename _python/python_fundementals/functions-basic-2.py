# def a():
#     return 5
# print(a()) #5 

# def a():
#     return 5
# print(a()+a()) #10

# def a():
#     return 5
#     return 10
# print(a()) # 5

# def a():
#     return 5
#     print(10)
# print(a()) #5

# def a():
#     print(5)
# x = a()
# print(x) # 5

# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3)) #error

# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))#7

# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a()) #10

# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))#7
# print(a(5,3))#14
# print(a(2,3) + a(5,3))#21

# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))#8

# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)#300
# a()
# print(b)#500

# b = 500
# printcopy(b)#500
# def a():
#     b = 300
#     print(b)#300
#     return b#300
# print(b)#300
# a()
# print(b)#none

# b = 500
# print(b)#500
# def a():
#     b = 300
#     print(b)#300
#     return b#300
# print(b)
# b=a()
# print(b)

# def a():
#     print(1)#1
#     b()
#     print(2)#2
# def b():
#     print(3)#3
# a()#1

def a():
    print(1)#1
    x = b()#3
    print(x)
    return 10#10
def b():
    print(3)
    return 5
y = a()
print(y)