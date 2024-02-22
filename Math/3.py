import math
n = float(input())
l = float(input())
z = l/(2*math.tan(math.pi/n))
print(round(n*l*z/2,0))