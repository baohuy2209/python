"""
Hãy xây dựng lớp DaGiac gồm có các thuộc tính: Số cạnh của đa giác, Mảng các số nguyên chứa kích thước các cạnh của đa giác. Các phương thức: Tính chu vi, In giá trị các cạnh của đa giác.
Xây dựng lớp TamGiac kế thừa từ lớp DaGiac, trong đó viết đè các hàm tính chu vi và xây dựng thêm phương thức tính diện tích tam giác.
Các lớp cần phải đảm bảo tính đóng gói và kế thừa.
Xây dựng một ứng dụng Java để nhập vào một dãy gồm n tam giác rồi in ra màn hình danh sách theo dạng bảng n tam giác.
In ra các cạnh của các tam giác có diện tích lớn nhất.
Tìm kiếm và in ra tam giác theo vị trí (index) nhập vào.
Xóa 1 tam giác tại vị trí nhập vào.
Sắp xếp mảng tam giác tăng dần theo diện tích.
Chương trình tính diện tích đa giác.
Hướng dẫn:

Chúng ta sẽ yêu cầu người dùng nhập vào số lượng tam giác với các thuộc tính chung ở class DaGiac và các thuộc tính riêng ở class TamGiac, hãy cùng đi theo các bước dưới đây:

Đầu tiên chúng ta sẽ tạo class DaGiac gồm các thuộc tính: soCanh, a[ ].
Trong class DaGiac xây dựng các constructor và các phương thức getter, setter. Xây dựng phương thức tính chu vi và in giá trị các cạnh của đa giác và xây dựng phương thức xuất đa giác.
Tiếp đến xây dựng class TamGiac kế thừa từ class DaGiac, trong đó viết đè thêm hàm tính chu vi và xây dựng thêm phương thức tính diện tích tam giác.
Tiếp theo sẽ tạo class LístTamGiac với các phương thức nhập tam giác, xuất tam giác, tìm kiếm tam giác theo vị trí index, xóa tam giác theo vị trí nhập vào và cuối cùng là sắp xếp tam giác theo diện tích.
Cuối cùng sẽ tạo class Main để tạo menu và gọi các phương thức đã viết để chạy chương trình.

"""