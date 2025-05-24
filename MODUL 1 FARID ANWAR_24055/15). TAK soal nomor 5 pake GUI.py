import tkinter as tk
from tkinter import messagebox

# Fungsi hitung diskon di nomor 14
def hitung_diskon():
    try:
        harga = float(entry_harga.get())
        
        if harga >= 500000:
            diskon = 0.2
        elif harga >= 300000:
            diskon = 0.15
        elif harga >= 100000:
            diskon = 0.1
        else:
            diskon = 0

        potongan = harga * diskon
        total = harga - potongan

        # hasil output
        label_diskon.config(text=f"Diskon: {diskon * 100:.0f}%")
        label_potongan.config(text=f"Potongan: Rp{potongan:,.0f}")
        label_total.config(text=f"Total Bayar: Rp{total:,.0f}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# GUI setup
window = tk.Tk()
window.title("Hitung Diskon Harga Barang")

# Input harga
tk.Label(window, text="Masukkan Harga Barang (Rp):").pack(pady=5)
entry_harga = tk.Entry(window)
entry_harga.pack(pady=5)

# Tombol hitung
tk.Button(window, text="Hitung Diskon", command=hitung_diskon).pack(pady=10)

# Label hasil
label_diskon = tk.Label(window, text="Diskon: ")
label_diskon.pack()

label_potongan = tk.Label(window, text="Potongan: ")
label_potongan.pack()

label_total = tk.Label(window, text="Total Bayar: ")
import tkinter as tk
from tkinter import messagebox

# Fungsi hitung diskon
def hitung_diskon():
    try:
        harga = float(entry_harga.get())
        
        if harga >= 500000:
            diskon = 0.2
        elif harga >= 300000:
            diskon = 0.15
        elif harga >= 100000:
            diskon = 0.1
        else:
            diskon = 0

        potongan = harga * diskon
        total = harga - potongan

        # Tampilkan hasil
        label_diskon.config(text=f"Diskon: {diskon * 100:.0f}%")
        label_potongan.config(text=f"Potongan: Rp{potongan:,.0f}")
        label_total.config(text=f"Total Bayar: Rp{total:,.0f}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# GUI setup
window = tk.Tk()
window.title("Hitung Diskon Harga Barang")

# Input harga
tk.Label(window, text="Masukkan Harga Barang (Rp):").pack(pady=5)
entry_harga = tk.Entry(window)
entry_harga.pack(pady=5)

# Tombol hitung
tk.Button(window, text="Hitung Diskon", command=hitung_diskon).pack(pady=10)

# Label hasil
label_diskon = tk.Label(window, text="Diskon: ")
label_diskon.pack()

label_potongan = tk.Label(window, text="Potongan: ")
label_potongan.pack()

label_total = tk.Label(window, text="Total Bayar: ")
label_total.pack()

#  GUI
window.mainloop()

