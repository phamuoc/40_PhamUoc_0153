class Date:
    def __init__(self, day=1, month=1, year=2024):
        self.day = day
        self.month = month
        self.year = year
    def display(self):
        """In thông tin về ngày, tháng, năm."""
        print(f"{self.day}/{self.month}/{self.year}")
    def next(self):
        """Tính toán ngày tiếp theo."""
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[1] = 29
        self.day += 1  
        if self.day > days_in_month[self.month - 1]:
            self.day = 1  
            self.month += 1  
            if self.month > 12:
                self.month = 1  
                self.year += 1 
    def is_leap_year(self):
        """Kiểm tra xem năm có phải là năm nhuận hay không."""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
if __name__ == "__main__":
    date = Date(28, 2, 2024)  
    date.display() 
    date.next() 
    date.display()  
class Employee:
    def __init__(self, name, birth_date, hire_date):
        self.name = name  
        self.birth_date = birth_date 
        self.hire_date = hire_date  
    def display_info(self):
        """In thông tin của nhân viên ra màn hình."""
        print(f"Họ tên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display() 
        print("Ngày vào công ty: ", end="")
        self.hire_date.display() 
if __name__ == "__main__":
    birth_date = Date(15, 5, 1990)  
    hire_date = Date(1, 6, 2020) 
    employee = Employee("Nguyen Van A", birth_date, hire_date)
    employee.display_info()