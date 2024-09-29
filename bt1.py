class hinhchunhat:
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0
    def nhap_kich_thuoc(self): 
        self.chieu_dai =  float(input("Nhập chiều dài hình chữ nhật: "))
        self.chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))       
    def chu_vi(self):
            chu_vi = (self.chieu_dai + self.chieu_rong) * 2
            print("chu vi hình chữ nhật bằng {} ".format(chu_vi))           
    def dien_tich(self): 
        dien_tich = self.chieu_dai * self.chieu_rong
        print("diện tích hình chữ nhật bằng {} ".format(dien_tich))        
    def in_thong_tin(self): 
        print(f"Chiều dài: {self.chieu_dai}")
        print(f"Chiều rộng: {self.chieu_rong}")
        self.chu_vi()   
        self.dien_tich() 
if __name__ == "__main__":
    hcn = hinhchunhat()  
    hcn.nhap_kich_thuoc()  
    hcn.in_thong_tin()  