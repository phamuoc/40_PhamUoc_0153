class thi_sinh:
    def __init__(self):
        self.ho_ten = ""
        self.diem_toan = 0
        self.diem_ly = 0
        self.diem_hoa = 0
    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ và tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm toán của thí sinh: "))
        self.diem_ly = float(input("Nhập điểm lý của thí sinh: "))
        self.diem_hoa = float(input("Nhập điểm hoá của thí sinh: "))
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa 
    def in_thong_tin(self):
        print("họ tên thí sinh: {}".format(self.ho_ten))
        print("Điểm toán thí sinh: {}".format(self.diem_toan))
        print("Điểm lý thí sinh: {}".format(self.diem_ly))
        print("Điểm hoá thí sinh: {}".format(self.diem_hoa))
        print("Tổng điểm 3 môn của thí sinh: {}".format(self.tinh_tong_diem()))
def lay_tong_diem(thi_sinh):
    return thi_sinh.tinh_tong_diem()
if __name__ == "__main__":
    danh_sach_thi_sinh = [] 
    so_luong = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_luong):
        ts = thi_sinh()
        print(f"Nhập thông tin cho thí sinh thứ {i+1}")
        ts.nhap_thong_tin() 
        danh_sach_thi_sinh.append(ts)
    diem_chuan = 20
    ds_thi_sinh_trung_tuyen = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]
    ds_thi_sinh_trung_tuyen.sort(key=lay_tong_diem, reverse=True)
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in ds_thi_sinh_trung_tuyen:
        ts.in_thong_tin()
        print("---------")