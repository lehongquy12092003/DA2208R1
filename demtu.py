vanban = "- A a a... Anh Tràng! Anh Tràng đã về chúng mày ơi! - Anh Tràng ơi bế em mấy... - Anh Tràng ơi đã uống rượu chưa? - Anh Tràng ơi!... Đứa túm đằng trước, đứa túm đằng sau, đứa cù, đứa kéo, đứa lôi chân không cho đi. Tràng chỉ ngửa mặt lên cười hềnh hệch. Cái xóm ngụ cư tồi tàn ấy mỗi chiều lại xôn xao lên được một lúc. Nhưng độ này thì trẻ con không đứa nào buồn ra đón Tràng nữa, chúng nó ngồi ủ rũ dưới những xó đường không buồn nhúc nhích. Trong bóng chiều nhá nhem, Tràng đi từng bước mệt mỏi, chiếc áo nâu tàng vắt sang một bên cánh tay, cái đầu trọc nhẵn chúi về đằng trước. Hình như những lo lắng, chật vật trong một ngày đè xuống cái lưng to rộng như lưng gấu của hắn. Cái đói đã tràn đến xóm này tự lúc nào. Những gia đình từ những vùng Nam Định, Thái Bình, đội chiếu lũ lượt bồng bế, dắt díu nhau lên xanh xám như những bóng ma, và nằm ngổn ngang khắp lều chợ. Người chết như ngả rạ. Không buổi sáng nào người trong làng đi chợ, đi làm đồng không gặp ba bốn cái thây nằm còng queo bên đường. Không khí vẩn lên mùi ẩm thối của rác rưởi và mùi gây của xác người. Giữa cái cảnh tối sầm lại vì đói khát ấy, một buổi chiều người trong xóm bỗng thấy Tràng về với một người đàn bà nữa. Mặt hắn có một vẻ gì phởn phơ khác thường. Hắn tủm tỉm cười nụ một mình và hai mắt thì sáng lên lấp lánh. Người đàn bà đi sau hắn chừng ba bốn bước. Thị cắp cái thúng con, đầu hơi cúi xuống, cái nón rách tàng nghiêng nghiêng che khuất đi nửa mặt. Thị có vẻ rón rén, e thẹn. Mấy đứa trẻ con thấy lạ vội chạy ra đón xem. Sợ chúng nó đùa như trước, Tràng vội vàng nghiêm nét mặt, lắc đầu ra hiệu không bằng lòng."
 ## xóa đi các dấu câu
vanban = vanban.replace("!", "")
vanban = vanban.replace(".","")
vanban = vanban.replace(",","")
vanban = vanban.replace("-","")
vanban = vanban.replace("?","")
vanban = vanban.split()#tạo tành list

## key là từ - giá trị là số lượng từ
D = {}
for i in vanban:
    D[i] = vanban.count(i)
print(D)
