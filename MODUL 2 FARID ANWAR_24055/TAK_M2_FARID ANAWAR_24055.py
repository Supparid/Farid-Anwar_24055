#fungsi 
def hitung_kecepatan_produksi(jumlah_unit, waktu_produksi, satuan_waktu):
    if jumlah_unit <= 0:
        print("Error: Jumlah unit harus lebih besar dari 0.")
    elif waktu_produksi <= 0:
        print("Error: Waktu produksi harus lebih besar dari 0.")
    else:
        kecepatan = jumlah_unit / waktu_produksi
        
        if satuan_waktu == "detik":
            print(f"Kecepatan produksi: {kecepatan:.2f} unit per detik.")
        elif satuan_waktu == "menit":
            print(f"Kecepatan produksi: {kecepatan:.2f} unit per menit.")
        elif satuan_waktu == "jam":
            print(f"Kecepatan produksi: {kecepatan:.2f} unit per jam.")
        else:
            print("Error: Satuan waktu tidak salah. Gunakan 'detik', 'menit', atau 'jam'.")

#Baigan untuk memasukan jumlah produksi dan waktu produksi nya
try:
    jumlah_unit = float(input("Masukkan jumlah unit yang diproduksi: "))
    waktu_produksi = float(input("Masukkan waktu produksi: "))
    satuan_waktu = input("Masukkan satuan waktu (detik/menit/jam): ").lower()

    hitung_kecepatan_produksi(jumlah_unit, waktu_produksi, satuan_waktu)

except ValueError:
    print("Error: Masukkan angka yang valid untuk jumlah unit dan waktu.")

