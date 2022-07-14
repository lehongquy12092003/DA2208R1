def somax(l):
    max = l[0]
    for i in range(len(l)):
        if max<l[i]:
            max = l[i]
    return max
print(somax([2,8,45,75,2,3]))
def solonnhi():
    m = max(2,8,45,75,2,3)
    m2=2
    for i in [2,8,45,2,3]:
        if i<m and i>=m2:
            m2 = i
    print(m2)
solonnhi()
