import math
class Diem:
    def __init__(self, x=0, y=0):
        self.toa_do_x = x 
        self.toa_do_y = y  
    def hien_thi(self):
        print(f"Điểm tọa độ: ({self.toa_do_x}, {self.toa_do_y})")
class Elip(Diem):
    def __init__(self, x, y, ban_truc_lon, ban_truc_nho):
        super().__init__(x, y) 
        self.ban_truc_lon = ban_truc_lon  
        self.ban_truc_nho = ban_truc_nho 
    def dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_nho
    def hien_thi(self):
        super().hien_thi() 
        print(f"Bán trục lớn: {self.ban_truc_lon}")
        print(f"Bán trục nhỏ: {self.ban_truc_nho}")
        print(f"Diện tích elip: {self.dien_tich()}")
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh) 
        self.ban_kinh = ban_kinh 
    def dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)
    def hien_thi(self):
        super().hien_thi() 
        print(f"Bán kính: {self.ban_kinh}")
        print(f"Diện tích đường tròn: {self.dien_tich()}")
if __name__ == "__main__":
    elip = Elip(0, 0, 5, 3)
    print("Thông tin elip:")
    elip.hien_thi()
    print("\n")
    duong_tron = DuongTron(0, 0, 4)
    print("Thông tin đường tròn:")
    duong_tron.hien_thi()
    