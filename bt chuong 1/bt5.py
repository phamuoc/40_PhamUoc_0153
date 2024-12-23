class Stack:
    def __init__(self, dung_luong_ngan_xep):
        self.dung_luong_ngan_xep = dung_luong_ngan_xep 
        self.stack = [] 
        self.top = -1  
    def isFull(self):
        return self.top == self.dung_luong_ngan_xep - 1
    def isEmpty(self): 
        return self.top == -1
    def push(self, value):  
        if self.isFull():
            raise IndexError("Stack đã đầy, không thể thêm phần tử mới.")
        self.stack.append(value)  
        self.top = self.top + 1 
    def pop(self): 
        if self.isEmpty():
            raise IndexError("Ngăn xếp trống, không thể lấy phần tử ra.")
        value = self.stack.pop() 
        self.top = self.top - 1  
        return value
    def count(self):  
        return self.top + 1 if not self.isEmpty() else 0
    def __del__(self):  
        self.stack.clear()  
        print("Ngăn xếp đã được xoá/huỷ")
if __name__ == "__main__":
    stack_dung_luong_ngan_xep = 5
    stack = Stack(stack_dung_luong_ngan_xep)
    try:
        stack.push(1.5)
        stack.push(2.5)
        stack.push(3.5)
        stack.push(4.5)
        stack.push(5.5)
    except IndexError as e:
        print(e)
    try:
        top_element = stack.pop()
        print("Phần tử lấy ra từ ngăn xếp:", top_element)
    except Exception as e:
        print(e)
    print("Số phần tử hiện có trong ngăn xếp:", stack.count())