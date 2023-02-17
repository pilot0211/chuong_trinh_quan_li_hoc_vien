import mysql.connector

def getConnection():
    khaibao = mysql.connector.connect(host='localhost',user='root', password='Pilot2002@',
                              database='Quan_ly_hoc_vien')
    return khaibao
    