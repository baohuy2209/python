"""
Viết chương trình quản lý việc tuyển sinh viên sau khi tốt nghiệp đại học.

Có 2 loại sinh viên bao gồm sinh viên tốt nghiệp loại khá giỏi (GoodStudent) và sinh viên tốt nghiệp loại trung bình (NormalStudent).

Cả 2 loại sinh viên trên đều phải cung cấp các thông tin sau khi nộp hồ sơ xin việc:
Họ tên (fullName), Ngày tháng năm sinh (doB), Giới tính (sex), Số điện thoại (phoneNumber), Tên trường đã học (universityName), Xếp loại tốt nghiệp (gradeLevel).

Riêng sinh viên loại khá giỏi phải có thêm thông tin:
điểm trung bình học tập (gpa) theo thang điểm 10, tên của loại học bổng (hoặc giải thưởng) cao nhất đã từng giành được (bestRewardName).

Riêng sinh viên loại trung bình thì phải có thêm các thông tin:
điểm TOEIC (englishScore), điểm thi đầu vào chuyên môn do công ty tổ chức thi (entryTestScore) theo thang điểm 10.

Yêu cầu 1:
Thí sinh hãy thiết kế và viết code thể hiện các class của các sinh viên và lớp học của chương trình làm sao để tuân thủ theo mô hình OOP đã học, áp dụng 4 tính chất : bao đóng (encapsulation) , kế thừa (inheritance) , đa hình (polymorphism) , trừu tượng (abstraction).
Lưu ý: Bất kì một sinh viên nào cũng cần có một phương thức có tên là ShowMyInfor để hiển thị thông tin của sinh viên đó ra màn hình cosole, yêu cầu này là bắt buộc với các thành viên xây dựng code cho chương trình này. Bạn hãy lưu ý khi thiết kế code để thỏa mãn yêu cầu này.
Yêu Cầu 2 : Kiểm tra ràng buộc dữ liệu cho chương trình. Dữ liệu của các file input phải tuân thủ theo ràng buộc sau:
– Họ tên sinh viên có chiều dài tối đa là 50 ký tự và tổi thiểu là 10 ký tự. Học viên cần tạo Exception tương ứng có tên là InvalidFullNameException (1 điểm).
– Chương trình phải bắt được lỗi sai định dạng ngày tháng năm đối với trường doB. doB phải theo định dạng dd/MM/YYYY. Học viên cần tạo Exception tương ứng có tên là InvalidDOBException (1 điểm).
– Số điện thoại: phải là chuỗi số có chiều dài 10 ký tự và phải bắt đầu bằng một trong các chuỗi số: 090, 098, 091, 031, 035 hoặc 038. Học viên cần tạo Exception tương ứng có tên là InvalidPhoneNumberException (1 điểm).
– Ngoài ra nếu có bất cứ một exception nào khác trong quá trình thực thi chương trình, thí sinh hãy thông báo ra màn hình nội dung “Input files have unknow errors !!!”  (0.5 điểm).
Yêu cầu 3: Chương trình cần có chức năng lựa chọn ứng viên trúng tuyển vào công ty theo nguyên tắc sau:
Người dùng sẽ nhập vào số lượng sinh viên cần tuyển dụng (tối thiểu là 11, tối đa là 15).
Chương trình sẽ tự động chọn ra ứng viên phù hợp cho công ty theo các bước như sau:
Nếu số lượng ứng viên là sinh viên khá giỏi có nhiều hơn số lượng cần tuyển thì xét ưu tiên theo điểm GPA. Nếu xuất hiện ứng viên khá giỏi có cùng điểm GPA thì xét ưu tiên theo họ tên. Vd: nếu họ tên là Nguyễn Văn A và Nguyễn Văn B thì ứng viên Nguyễn Văn A được chọn. (Giả sử không bao giờ có sinh viên có trùng họ tên nhau).
Nếu số lượng ứng viên là sinh viên khá giỏi ít hơn hoặc bằng số lượng cần tuyển thì nhận hết sinh viên khá giỏi.
Sau khi tuyển hết ứng viên khá giỏi, nếu vẫn chưa đủ số lượng cần tuyển, chương trình sẽ lấy ứng viên trung bình. Các ứng viên trung bình được xét ưu tiên theo điểm thi đầu vào, nếu điểm thi đầu vào bằng nhau thì xét đến điểm TOEIC. Nếu xuất hiện ứng viên trung bình có cùng điểm TOEIC thì xét ưu tiên theo họ tên.
Yêu cầu 4: Chương trình có thể hiển thị được thông tin họ tên và số điện thoại của tất cả các sinh viên đã nhập vào hệ thống (yêu cầu dùng collection sort để sắp xếp giảm dần theo fullName và tăng dần theo phoneNumber đối với sinh viên trước khi hiển thị).
"""

import datetime


class Student:
    def __init__(self, fullname: str, birthday, sex: str, phone: int, universityname: str, gradelevel: str):
        self.fullname = fullname
        self.birthday = birthday
        self.sex = sex
        self.phone = phone
        self.universityname = universityname
        self.gradelevel = gradelevel


class Goodstudent(Student):
    def __init__(self, fullname: str, birthday, sex: str, phone: int, universityname: str, gradelevel: str, gpa: int, bestrewardname:str):
        Student .__init__(self, fullname, birthday, sex, phone, universityname, gradelevel)
        self.gpa = gpa
        self.bestrewardname = bestrewardname


class Normalstudent(Student):
    def __init__(self, fullname: str, birthday, sex: str, phone: int, universityname: str, gradelevel: str, engscore: float, entrytestscore:float):
        Student .__init__(self, fullname, birthday, sex, phone, universityname, gradelevel)
        self.engscore = engscore
        self.entrytestscore = entrytestscore


def inputfullname():



def inputphone():




listnorstd = []

listgoodstd = []


class Management():
    def insert(self):


    def show(self):



    def remove(self):


    def recruit(self):


    def edit(self):



if __name__ == "__main__":
    print("List operation with list household : ")
    print("1. Inserting student .")
    print("2. Showing information of student .")
    print("3. Removing out list .")
    print("4. Editing information .")
    print("5. Searching by gpa ")
    print("6. Write in file .")
    print("7. Read a file ")
    print("8. Recruit and show list of students which passed .")
    print("9. Exit loop .")