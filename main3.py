nim = str(input("masukan nim: "))
nama = str(input("masukan nama: "))
uts = int(input("masukan nilai uts: "))
uas = int(input("masukan nilai uas: "))
tugas = int(input("masukan nilai tugas: "))
total = (uts*0.3)+(uas*0.5)+(tugas*0.2)
if total > 100:
  print("masukin yg bener")
else:
 if total >= 60:
  print("selamat, anda lulus")
  if total >= 80:
    print("grade A")
  elif total >= 70:
    print("grade B")
  else:
  print("grade C")
 else:
  print("mampus, anda tidak lulus")
  if total >= 50:
    print("grade D")
  else:
      print("grade E")

  print("nilai anda adalah: \t" + str(total))
