D_ds = {"1":"Phở gà","2":"Phở bò"}
def hienthi(D):
    print("------------------")
    print()
    if len(D)==0:
        print("Chưa có sản phẩm nào")
    for i in D:
        print(i,":",D[i])
    print()
    print("------------------")
def themsanpham(D):
    while True:
        ma_id = input("Mời nhập vào ID, nếu muốn thoát chức năng thì nhập 0 ")
        if ma_id == "0":
            return
        if ma_id in D:
            print("ID đã tồn tại, mời nhập vào ID khác:")
        else:
            break
    name = input("Mời nhập tên sản phẩm: ")
    D[ma_id] = name
def suasanpham(D):
    while True:
        ma_id = input("Mời nhập vào ID, nếu muốn thoát chức năng thì nhập 0 ")
        if ma_id == "0":
            return
        if ma_id not in D:
            print("ID không tồn tại, mời nhập vào ID khác")
        else:
            break
    name = input("Mời nhập tên sản phẩm mới: ")
    D[ma_id]=name
def xoasanpham(D):
    while True:
        ma_id = input("Mời nhập vào ID, nếu muốn thoát chức năng thì nhập 0")
        if ma_id == "0":
            return
        if ma_id not in D:
            print("ID không tồn tại, mời nhập ID khác: ")
        else:
            break
    chac_xoa = input("Nếu bạn muốn chắc chắn muốn xóa sản phẩm thì ấn C, ngược lại gõ bất kì ")
    if chac_xoa == "C":
        D.pop(ma_id)
        print("Sản phẩm đã được xóa")
print("Nhập H - hiển thị sản phẩm")
print("Nhập T - thêm sản phẩm")
print("Nhập S - sửa sản phẩm")
print("Nhập X - xóa sản phẩm")
hienthi(D_ds)
while True:
    tinh_nang = input("Mời nhập vào tính năng!")
    if tinh_nang == "H":
        hienthi(D_ds)
    elif tinh_nang == "T":
        themsanpham(D_ds)
    elif tinh_nang == "S":
        suasanpham(D_ds)
    elif tinh_nang == "X":
        xoasanpham(D_ds)
    elif tinh_nang == "0":
        break
