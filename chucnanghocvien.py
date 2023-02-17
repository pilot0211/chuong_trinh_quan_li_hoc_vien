import lophoc
ketnoi = lophoc.getConnection()
data = ketnoi.cursor()
def getdata():
    data.execute("SELECT * FROM Quan_ly_hoc_vien.Hocvien")
    ketqua = data.fetchall()
    for i in ketqua:
        print(i)
   
def getdata2():
    sql = "SELECT * FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s"
    id = input("nhap :")
    data.execute(sql,(id,))
    ketqua = data.fetchall()
    for i in ketqua:
        print(i)
    ketnoi.close()
def delete_data():
    sql = "DELETE FROM Quan_ly_hoc_vien.Hocvien WHERE Id = %s"
    id = input("nhap :")
    data.execute(sql,(id,))
    ketnoi.commit()
    ketnoi.close()
def update_data():
    sql = "UPDATE Quan_ly_hoc_vien.Hocvien SET Age= %s WHERE Id = %s"
    age = input("nhap so muon thay doi: ")
    id = input("nhap :")
    data.execute(sql,(id,))
    ketnoi.commit()
    ketnoi.close()
def create():
    sql = "INSERT INTO `Hocvien`(Id,`Name`,Age,Country, English,Information)VALUES (5,'Nguyen Van E', 23, 'Da Nang', 3,4)"
    data.execute(sql,(id,))
    ketnoi.commit()
    ketnoi.close()


