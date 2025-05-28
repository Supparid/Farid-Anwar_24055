# Deklarasi Data Produk dan Layanan
data_produk = {
    "Mesin CNC Presisi": 850000000,
    "Robot Industri 6-Axis": 1200000000,
    "Conveyor Belt System": 350000000,
    "Injection Molding Machine": 680000000,
    "3D Printer Industri": 450000000,
    "PLC Controller Unit": 95000000,
    "Hydraulic Press Machine": 550000000,
    "Laser Cutting Machine": 720000000,
    "Industrial IoT Sensor Kit": 28000000,
    "Automated Packaging System": 390000000
}

layanan_tambahan = {
    "Instalasi": 15000000,
    "Pelatihan Operator": 5000000,
    "Maintenance Tahunan": 10000000,
    "Garansi Ekstensi 2 Tahun": 25000000
}

metode_pembayaran = {
    1: "Transfer Bank (BCA): 10070220063 a.n. Manufaktur Maju Jaya",
    2: "Virtual Account (DANA): 081572270095 a.n Manufaktur Maju Jaya",
    3: "Leasing Pembiayaan Industri",
    4: "Letter of Credit (L/C)"
}

print("=============== KATALOG PERALATAN INDUSTRI MANUFAKTUR ===============")
print("\nPRODUK UNGGULAN KAMI:")
print("---------------------------------------------------------------")
for produk, harga in data_produk.items():
    print(f"{produk:30} \t Rp {harga:,}")

print("\nLAYANAN TAMBAHAN:")
print("---------------------------------------------------------------")
for layanan, biaya in layanan_tambahan.items():
    print(f"{layanan:25} \t Rp {biaya:,}")

print("\n===============================================================")

# Input Data Pembeli
print("\nFORMULIR PEMESANAN")
print("---------------------------------------------------------------")
nama_perusahaan = input("Nama Perusahaan/Pabrik: ")
alamat_pabrik = input("Alamat Lengkap Pabrik: ")
no_handphone = input("Nomor Kontak (HP/WhatsApp): ")
email = input("Alamat Email: ")
nama_pic = input("Nama Penanggung Jawab: ")
jabatan_pic = input("Jabatan Penanggung Jawab: ")

# Input Pemesanan
produk_dipilih = input("\nPilih Produk yang Dipesan: ")
while produk_dipilih not in data_produk:
    print("Maaf, produk tidak tersedia dalam katalog kami.")
    print("Produk yang tersedia:")
    for produk in data_produk:
        print(f"- {produk}")
    produk_dipilih = input("\nSilakan pilih produk yang tersedia: ")

jumlah_unit = int(input("Jumlah Unit yang Dipesan: "))

# Pilih Layanan Tambahan
print("\nLAYANAN TAMBAHAN YANG TERSEDIA:")
for layanan in layanan_tambahan:
    print(f"- {layanan}")

layanan_tambahan_dipilih = []
while True:
    layanan = input("Pilih layanan tambahan (ketik 'selesai' jika sudah cukup): ")
    if layanan.lower() == 'selesai':
        break
    if layanan in layanan_tambahan:
        layanan_tambahan_dipilih.append(layanan)
    else:
        print("Layanan tidak tersedia. Silakan pilih dari daftar di atas.")

# Metode Pembayaran
print("\nMETODE PEMBAYARAN YANG TERSEDIA:")
for id, metode in metode_pembayaran.items():
    print(f"{id}. {metode}")

pilihan_pembayaran = int(input("Pilih ID Metode Pembayaran: "))

# Proses Perhitungan
subtotal_produk = data_produk[produk_dipilih] * jumlah_unit
subtotal_layanan = sum(layanan_tambahan[layanan] for layanan in layanan_tambahan_dipilih)
total_sebelum_diskon = subtotal_produk + subtotal_layanan

# Program Membership
status_membership = input("\nApakah perusahaan Anda sudah terdaftar sebagai member Asosiasi Manufaktur Indonesia? (ya/tidak): ").lower()
if status_membership == 'ya':
    diskon = total_sebelum_diskon * 0.1  # Diskon 10% untuk member
    print("Selamat! Anda mendapatkan diskon member 10%")
else:
    diskon = 0
    print("Ingin mendapatkan diskon member 10%? Daftarkan perusahaan Anda di Asosiasi Manufaktur Indonesia!")

total_akhir = total_sebelum_diskon - diskon

# Opsi Pengiriman
print("\nPILIHAN PENGIRIMAN:")
print("1. Pengiriman Standar (2-4 minggu) - Gratis")
print("2. Pengiriman Cepat (1 minggu) - Rp 5.000.000")
print("3. Pengiriman Ekspres (3 hari) - Rp 12.000.000")
opsi_pengiriman = int(input("Pilih opsi pengiriman: "))

if opsi_pengiriman == 2:
    total_akhir += 5000000
elif opsi_pengiriman == 3:
    total_akhir += 12000000

# Output Invoice
print("\n\n=============== INVOICE PEMESANAN ===============")
print(f"Perusahaan: {nama_perusahaan}")
print(f"Alamat Pabrik: {alamat_pabrik}")
print(f"Kontak: {nama_pic} ({jabatan_pic})")
print(f"Telepon: {no_handphone} | Email: {email}")
print("\nDETAIL PEMESANAN:")
print("-------------------------------------------------")
print(f"Produk: {produk_dipilih} ({jumlah_unit} unit)")
print(f"Harga Satuan: Rp {data_produk[produk_dipilih]:,}")
print(f"Subtotal Produk: Rp {subtotal_produk:,}")

if layanan_tambahan_dipilih:
    print("\nLAYANAN TAMBAHAN:")
    for layanan in layanan_tambahan_dipilih:
        print(f"- {layanan}: Rp {layanan_tambahan[layanan]:,}")
    print(f"Subtotal Layanan: Rp {subtotal_layanan:,}")

print("\nRINCIAN PEMBAYARAN:")
print("-------------------------------------------------")
print(f"Total Sebelum Diskon: Rp {total_sebelum_diskon:,}")
print(f"Diskon: Rp {diskon:,}")
print(f"Biaya Pengiriman: Rp {5000000 if opsi_pengiriman == 2 else 12000000 if opsi_pengiriman == 3 else 0:,}")
print(f"TOTAL PEMBAYARAN: Rp {total_akhir:,}")

print("\nMETODE PEMBAYARAN:")
print(metode_pembayaran[pilihan_pembayaran])

print("\nINFO PENGIRIMAN:")
if opsi_pengiriman == 1:
    print("Estimasi pengiriman: 2-4 minggu")
elif opsi_pengiriman == 2:
    print("Estimasi pengiriman: 1 minggu")
else:
    print("Estimasi pengiriman: 3 hari")

print("\nTERIMA KASIH TELAH MEMESAN DENGAN KAMI!")
print("Tim support kami akan menghubungi Anda dalam 1x24 jam untuk konfirmasi pemesanan.")
print("Untuk pertanyaan lebih lanjut, hubungi 1500-123 (Customer Service 24/7)")
print("=================================================")