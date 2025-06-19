#q1
# for c in range(1,1001):
#     if c%15==0:
#         print("FuzzBuzz")
#     elif c%5==0:
#         print("Buzz")
#     elif c%3==0:
#         print("Fuzz")
#     else:
#         print(c)
#q2
# a=0
# b=int(input("Please enter a number: "))
# while a<b:
#     a += 1
#     print("*"*a)
# while a>0:
#     a-=1
#     print("*"*a)
#q3
a=int(input("Please enter a number:"))
for i in range(2,a):
    if a%i==0:
        print("It is not a first number")
        break
    elif i==a-1:
        print("It is a first number")