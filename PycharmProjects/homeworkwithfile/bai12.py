"""
Xây dựng chương trình quản lý kết quả học tập của sinh viên tại một trường đại học. Có 2 loại sinh viên là sinh viên chính quy và sinh viên tại chức với các thông tin giống nhau: mã sinh viên, họ tên, ngày tháng năm sinh, năm vào học, điểm đầu vào và danh sách kết quả học tập. Sinh viên tại chức có thêm thông tin nơi liên kết đào tạo(Đồng Nai, Cà Mau, …). Khoa gồm có các thông tin: tên khoa và danh sách sinh viên đang theo học. Kết quả học tập gồm có tên học kỳ, điểm trung bình học kỳ đó.

Hiện thực các yêu cầu sau:
Vẽ class diagram cho phát biểu bài toán trên OOP:

Hiện thực các lớp cần thiết cho bài toán trên
Phương thức khởi tạo (constructor) cho các lớp: constructor chuẩn, constructor
có tham số, constructor sao chép
Phương thức input và output để cho phép người dùng nhập thông tin cho các
loại sinh viên
Phương thức xác định sinh viên có phải là chính quy hay không?
Xử lý Exception khi người dùng nhập sai dữ liệu
Phương thức lấy điểm trung bình các môn học của sinh viên dựa vào học kỳ
cho trước
Phương thức xác định tổng số sinh viên chính quy của khoa?
Tìm ra sinh viên có điểm đầu vào cao nhất ở mỗi khoa
Ở mỗi khoa, lấy ra danh sách các sinh viên tại chức tại nơi liên kết đào tạo cho
trước
Ở mỗi khoa, lấy ra danh sách sinh viên có điểm trung bình ở học kỳ gần nhất
(là học kỳ cuối cùng trong danh sách kết quả học tập của sinh viên) từ 8.0 trở
lên
Ở mỗi khoa, tìm ra sinh viên có điểm trung bình học kỳ cao nhất (ở bất kỳ học
kỳ nào)
Ở mỗi khoa, sắp xếp danh sách sinh viên tăng dần theo loại và giảm dần theo
năm vào học (sử dụng interface Comparable hoặc Comparator)
Ở mỗi khoa, thống kê số lượng sinh viên theo năm vào học. Ví dụ 2020: 100,
2019: 90, 2018: 120.
"""