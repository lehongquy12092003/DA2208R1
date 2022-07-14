L_mahoa = ["hello", "goodbye","thankyou","hello" ]
D_mahoa = {"xin chao":"hello","tam biet":"goodbye","cam on":"thankyou"}

def mahoanguoc(L_mahoa,D_mahoa):
    L_kq = []
    for i in L_mahoa:
        for j in D_mahoa:
            if i == D_mahoa[j]:
                L_kq.append(j)
                
    return L_kq
print(mahoanguoc(L_mahoa,D_mahoa))
