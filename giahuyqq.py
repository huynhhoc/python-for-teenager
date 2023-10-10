n = int(input("Nhap n: "))
m = int(input("Nhap m: "))
if m == 0:
  print(" khong the lay", n, "chia cho", m)
elif n %m == 0:
  l = n//m
  b = n%m
  print(n, "chia het cho", m)
  print("Thuong la:", l)
else:
  l = n//m
  b = n%m
  print(n, "khong chia het cho", m)
  print("So du la:", b)
  print("Thuong la:", l)
