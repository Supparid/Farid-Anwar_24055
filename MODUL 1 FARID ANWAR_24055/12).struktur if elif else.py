nilai = float(input("masukan nilai siswa(0-100)"))

if nilai <0 or nilai >100:
    print("nilai tidak valid! harus antara 0-100")
elif nilai >= 75:
    print("selamat anda LULUS! dengan nilai baik")
elif nilai >= 60:
    print("selamat anda LULUS! dengan nilai cukup")
else:
    print("Mohon maaf anda tidak Lulus")