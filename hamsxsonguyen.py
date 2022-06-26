def sxsonguyen(num1,num2,num3):
    temp = 0
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    return num1, num2, num3
num1 = int(input("Nhap so thu nhat: "))
num2 = int(input("Nhap so thu hai: "))
num3 = int(input("Nhap so thu ba: "))
c = sxsonguyen(num1,num2,num3)
print(c)
