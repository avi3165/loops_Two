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
a=0
b=int(input("Please enter a number: "))
while a<b:
    a += 1
    print("*"*a)
while a>0:
    a-=1
    print("*"*a)