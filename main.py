from chucnanghocvien import *
while(True):
    print("---------------------------")
    print("1.tao danh sach")
    print("2.in danh sach")
    print("3.xoa giay trong danh sach")
    print("4.update giay trong danh sach")
    print("5.exit")
    print("---------------------------")
    h = int(input("moi ban chon:"))
    match(h):
        case 1:
            create()
        case 2:
            getdata()
        case 3:
            delete_data()
        case 4:
            update_data()
        
