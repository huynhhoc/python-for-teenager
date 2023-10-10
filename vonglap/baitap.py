#1. Nhap (input) vao hai so nguyen a va b, sau do se chon phep toan
#2.  Neu (if) nguoi dung chon +, thi se tinh tong hai so
#3.  Neu nguoi dung chon -, thi se tinh hieu a - b
#4.  Neu nguoi dung chon *, thi se tinh tich a * b

ca = input("Nhap a:")
a  = int(ca)
cb = input("Nhap b:")
b  = int(cb)
chon = input("Chon phep toan +/-/*: ")
if chon == "+":
  tong = a + b
  print ("Ket qua tong a va b la: ", tong)
if chon == "-":
  hieu = a - b
  print("Ket qua hieu a tru b la: ", hieu)
if chon == "*":
  tich = a * b
  print ("Ket qua tich a va b la: ", tich)
