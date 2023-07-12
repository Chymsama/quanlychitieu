#!/usr/bin/env python
# coding: utf-8

# In[1]:


list_chi = []

def addchi():
    ten =  input('Nhập mục chi tiêu :')
    m = float (input('Số tiền đã chi : '))
    date = input('Ngày chi tiêu(dd/MM) : ')
    list_chi.append({'tên':ten,'Giá trị':m,'Ngày chi':date})
    print('thêm mục chi thành công')
    
    
def delchi():
    if len(list_chi) == 0:
        print('Không có mục chi tiêu!')
    else:
        print('Danh sách các mục chi tiêu:')
        for i, chi in enumerate(list_chi):
            print(f"{i+1}. {chi['tên']} - {chi['Giá trị']} - {chi['Ngày chi']}")

        index = int(input('Nhập vào số thứ tự mục chi tiêu muốn xóa: '))
        if index <1 and index > len(list_chi) :
            print('Số thứ tự không hợp lệ. Vui lòng nhập lại')
        else:
            delchitieu = list_chi.pop(index -1 )
            print(f"Đã xoá mục chi: {delchitieu['tên']}")
            
def getall():
    if len(list_chi) == 0:
        print('Không có mục chi tiêu!')
    else:
        print('Danh sách các mục chi tiêu:')
        for i, chi in enumerate(list_chi):
            print(f"{i+1}. {chi['tên']} - {chi['Giá trị']} - {chi['Ngày chi']}")

def main():
    while True:
        print("\n----- MENU -----")
        print("1. Thêm mục chi")
        print("2. Xoá mục chi")
        print("3. Hiển thị danh sách mục chi")
        print("4. Thoát")
        choice = input("Chọn một số từ menu: ")

        if choice == "1":
            addchi()
        elif choice == "2":
            delchi()
        elif choice == "3":
            getall()
        elif choice == "4":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            
            
main()

