#input variable
harga = float(input("Masukkan harga barang (Rp): "))

# proses 
if harga >= 500000:
    diskon = 0.2 
elif harga >= 300000:
    diskon = 0.15 
elif harga >= 100000:
    diskon = 0.1  
else:
    diskon = 0  

# perhitangan
potongan = harga * diskon
total = harga - potongan
# hasil outpot
print(f"Harga awal     : Rp{harga:,.0f}")
print(f"Diskon         : {diskon * 100:.0f}%")
print(f"Potongan harga : Rp{potongan:,.0f}")
print(f"Total bayar    : Rp{total:,.0f}")