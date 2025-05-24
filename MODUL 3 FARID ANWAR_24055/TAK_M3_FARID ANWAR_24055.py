# Dictionary jenis waste
jenis_waste = {
    1: "Overproduction",
    2: "Waiting",
    3: "Transport",
    4: "Extra Processing",
    5: "Inventory",
    6: "Motion",
    7: "Defects"
}

#Fungsi klasifikasi menggunakan if-elif-else
def klasifikasi_waste(aktivitas):
    aktivitas = aktivitas.lower()

    if "berlebih" in aktivitas or "produksi berlebih" in aktivitas:
        return jenis_waste[1]  # Overproduction
    elif "menunggu" in aktivitas or "tertunda" in aktivitas:
        return jenis_waste[2]  # Waiting
    elif "pindah" in aktivitas or "transport" in aktivitas or "pengiriman" in aktivitas:
        return jenis_waste[3]  # Transport
    elif "proses tambahan" in aktivitas or "ulang" in aktivitas or "rework" in aktivitas:
        return jenis_waste[4]  # Extra Processing
    elif "persediaan" in aktivitas or "stok" in aktivitas:
        return jenis_waste[5]  # Inventory
    elif "gerakan" in aktivitas or "bergerak" in aktivitas:
        return jenis_waste[6]  # Motion
    elif "cacat" in aktivitas or "kesalahan" in aktivitas or "rusak" in aktivitas:
        return jenis_waste[7]  # Defects
    else:
        return "Lainnya"

 #Input aktivitas dari pengguna
jumlah = int(input("Masukkan jumlah aktivitas: "))
aktivitas_list = []

for i in range(jumlah):
    aktivitas = input(f"Masukkan aktivitas ke-{i+1}: ")
    aktivitas_list.append(aktivitas)

#Analisis dan tampilkan hasil
print("\nHasil Klasifikasi Waste:")
for aktivitas in aktivitas_list:
    hasil = klasifikasi_waste(aktivitas)
    print(f"- '{aktivitas}' diklasifikasikan sebagai: {hasil}")

