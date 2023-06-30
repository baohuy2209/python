"""
Mỗi tài khoản chứa các thông tin:

Bài viết này được đăng tại [free tuts .net]

Số tài khoản ( Kiểu long)
Tên tài khoản (kiểu chuỗi)
Số tiền trong tài khoản (kiểu double)
ADVERTISEMENT
Thiết kế lớp Account để lưu trữ các thông tin, lớp bao gồm các phương thức sau:

Constructor: Có 2 constructor ( mặc định và đầy đủ tham số)
Các phương thức get, set cho từng thuộc tính
Phương thức toString để trả về chuỗi chứa toàn bộ thông tin tài khoản, yêu cầu định dạng tiền tệ.
Thêm các thông tin sau vào lớp Account:

Hằng số lãi suất có giá trị khởi tạo 0.035
Constructor có 2 đối số: số tài khoản, tên tài khoản. Constructor này sẽ khởi tạo số tiền mặc định là 50
Phương thức nạp tiền vào tài khoản: Lấy số tiền hiện tại trong tài khoản + số tiền nạp vào
Phương thức rút tiền: Lấy số tiền hiện tại trong tài khoản – (số tiền muốn rút+phí rúttiền)
Phương thức đáo hạn: Mỗi lần đến kỳ đáo hạn thì số tiền trong tài khoản = số tiền trong tài khoản + số tiền trong tài khoản * LAISUAT
Phương thức chuyển khoản từ tài khoản này sang tài khoản khác
Chú ý: Mỗi thao tác phải kiểm tra số tiền nạp, rút, chuyển có hợp lệ hay không? (VD: tiền nhập vào <0, tiền rút nhiều hơn tiền trong tài khoản thì thông báo không hợp lệ và yêu cầu nhập lại)







Chúng ta sẽ lần lượt thực hiện theo các yêu cầu của bài toán:

Đầu tiên chúng ta sẽ tạo class Account với các thuộc tính soTK, tenTK, soTienTrongTK.
Tạo các constructor mặc định và constructor có tham số.
Tạo các phương thức getter và setter.
khởi tạo phương thức toString để hiển thị kết quả dưới dạng chuỗi.
Khởi tạo phương thức nạp tiền với điều kiện số tiền phải lớn hơn hoặc bằng 0.
Khởi tạo phương thức rút tiền với điều kiện số tiền rút phải bé hơn hoặc bằng số tiền có trong tài khoản + phí.
Khởi tạo phương thức đáo hạn.
Khởi tạo phương thức in kết quả theo Format.
Tiếp đến chúng ta sẽ tạo class Main với các Menu theo yêu cầu của đề bài và gọi các phương thức đã tạo ở class Account.
"""