def fun(a,b):
    for z in range(b+1):
        if pow(z,2)>=a and pow(z,2)<=b:
            print(z, end=" ")
x = int(input())
y = int(input())
fun(x,y)