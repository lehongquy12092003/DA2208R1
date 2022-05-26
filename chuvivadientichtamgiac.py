import math
a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
p = (a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Chu vi tam giac la",p)
print("Dien tich tam giac la",S)
