"""
Viết lớp ThucPham mô tả một hàng hóa là hàng thực phẩm trong kho của một siêu thị, có các thuộc tính:

Mã hàng (không cho phép sửa, không được để rỗng).
Tên hàng (không được để rỗng), đơn giá (>0).
Ngày sản xuất và ngày hết hạn (ngày không được để rỗng, ngày hết hạn phải sau ngày sản xuất).
Ràng buộc chặt chẽ các ràng buộc trên các trường dữ liệu. Nếu dữ liệu không hợp lệ thì gán giá trị mặc định cho phép tương ứng của trường đó.

Bài viết này được đăng tại [free tuts .net]

Tạo 1 constructor có đầy đủ tham số, 1 constructor có tham số là mã hàng.
Viết các phương thức setters/getters.
Viết phương thức kiểm tra một hàng thực phẩm đã hết hạn chưa?
Phương thức toString, trả về chuỗi chứa thông tin của hàng thực phẩm. Trong đó: Định dạng đơn giá có phân cách hàng nghìn. Định dạng kiểu ngày là dd/MM/yyyy.
ADVERTISEMENT





Viết hàm Main để thực hiện các yêu cầu trên.

Chương trình kiểm tra thực phẩm.
Hướng dẫn:

Chúng ta sẽ thực hiện lần lượt các yêu cầu của đề bài:

Đầu tiền chúng ta sẽ thực hiện tạo class ThucPham với các thuộc tính maHang, tenHang, donGia, nSX, hSD. Với các thuôc tính này chúng ta sẽ phải gán điều kiện như đề bài đã yêu cầu
Trong class ThucPham chúng ta sẽ khởi tạo các constructor mặc đinh và constructor có tham số.
Khởi tạo các phương thức getter và setter.
Khởi tạo các phương thức kiểm tra ngày tháng năm. Cụ thể chúng ta sẽ kiểm tra ngày tháng năm nhập vào có hợp lệ hay không.
Khởi tạo phương thức kiểm tra sản phẩm còn hạn sử dụng hay không dựa vào này sản xuất, hạn sử dụng và ngày hiện tại.
khởi tạo phương thức toString để hiển thị kết quả dưới dạng chuỗi.
Tiếp đến sẽ tạo class Main để gọi các phương thức được khởi tạo ở class ThucPham.
"""