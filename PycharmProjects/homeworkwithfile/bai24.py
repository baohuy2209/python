"""
Mô tả: class Account có 3 biến private: id, name, balance.

Một hàm khởi tạo Account 3 thuộc tính id, name, balance.

credit(amount: int): Nạp tiền vào tài khoản, tài khoản sẽ được cộng lên một khoản amount. Kiểm tra tham số đầu vào phải là số dương.

debit(amount: int): Thanh toán tiền, tài khoản sẽ được trừ một số lượng tiền amount. Nếu số tiền thanh toán lớn hơn số tiền trong tài khoản thì thông báo thanh toán không thành công.

tranferTo(account: Account), chuyển tiền từ tài khoản này cho tài khoản khác. Ví dụ Account A có balance = 50, B có balance = 10. A.tranferTo(B, 10). A (balance = 40), B (balance = 20). Chú ý kiểm tra nếu chuyển số tiền nhiều hơn tài khoản hiện Acó thông báo lỗi chuyển tiền không thành
"""

class Account:
    def __init__(self, id:int, name:str, balance:int):
        self.id = id
        self.name = name
        self.balance = balance


    def credit(self):


    def debit(self):


    def tranferto(self):


