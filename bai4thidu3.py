while True:
    n = int(input("Nhap n: "))
    m = int(input("Nhap m: "))

    if m == 0:
      print("khong the lay", n, "chia cho", m)
    elif n %m == 0:
      print(n, "chia het cho ", m)
    else:
      print(n, " khong chia het cho ", m)
