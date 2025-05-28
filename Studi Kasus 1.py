import tkinter as tk
from tkinter import ttk, messagebox

# Data produk dan layanan
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

class AplikasiManufaktur:
    def __init__(self, root):
        self.root = root
        self.root.title("Katalog Peralatan Industri Manufaktur")
        self.root.geometry("900x700")
        
        # Variabel untuk menyimpan input
        self.nama_perusahaan = tk.StringVar()
        self.alamat_pabrik = tk.StringVar()
        self.no_handphone = tk.StringVar()
        self.email = tk.StringVar()
        self.nama_pic = tk.StringVar()
        self.jabatan_pic = tk.StringVar()
        self.produk_dipilih = tk.StringVar()
        self.jumlah_unit = tk.IntVar(value=1)
        self.layanan_tambahan = []
        self.metode_pembayaran = tk.IntVar()
        self.membership = tk.BooleanVar()
        self.pengiriman = tk.IntVar(value=1)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Notebook untuk multi-tab
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)
        
        # Tab Katalog
        tab_katalog = ttk.Frame(notebook)
        notebook.add(tab_katalog, text="Katalog Produk")
        self.create_katalog_tab(tab_katalog)
        
        # Tab Pemesanan
        tab_pemesanan = ttk.Frame(notebook)
        notebook.add(tab_pemesanan, text="Form Pemesanan")
        self.create_pemesanan_tab(tab_pemesanan)
        
        # Tab Invoice
        tab_invoice = ttk.Frame(notebook)
        notebook.add(tab_invoice, text="Invoice")
        self.create_invoice_tab(tab_invoice)
    
    def create_katalog_tab(self, parent):
        # Frame untuk produk
        frame_produk = ttk.LabelFrame(parent, text="Produk Unggulan Kami", padding=10)
        frame_produk.pack(fill='both', expand=True, padx=10, pady=5)
    
        # Treeview untuk produk + BOTH scrollbars
        columns = ('produk', 'harga')
        self.tree_produk = ttk.Treeview(frame_produk, columns=columns, show='headings')
        self.tree_produk.heading('produk', text='Nama Produk')
        self.tree_produk.heading('harga', text='Harga (Rp)')
        self.tree_produk.column('produk', width=300)
        self.tree_produk.column('harga', width=150, anchor='e')
    
        # Vertical Scrollbar
        yscroll = ttk.Scrollbar(frame_produk, orient=tk.VERTICAL, command=self.tree_produk.yview)
        self.tree_produk.configure(yscroll=yscroll.set)
    
        # Horizontal Scrollbar (NEW)
        xscroll = ttk.Scrollbar(frame_produk, orient=tk.HORIZONTAL, command=self.tree_produk.xview)
        self.tree_produk.configure(xscroll=xscroll.set)
    
        # Grid layout for scrollbars
        self.tree_produk.grid(row=0, column=0, sticky='nsew')
        yscroll.grid(row=0, column=1, sticky='ns')
        xscroll.grid(row=1, column=0, sticky='ew')
    
        # Configure grid weights
        frame_produk.grid_rowconfigure(0, weight=1)
        frame_produk.grid_columnconfigure(0, weight=1)
    
        # Insert data
        for produk, harga in data_produk.items():
            self.tree_produk.insert('', tk.END, values=(produk, f"{harga:,}"))
    
        # Repeat for layanan tambahan (similar changes)
        frame_layanan = ttk.LabelFrame(parent, text="Layanan Tambahan", padding=10)
        frame_layanan.pack(fill='both', expand=True, padx=10, pady=5)
    
        columns = ('layanan', 'biaya')
        self.tree_layanan = ttk.Treeview(frame_layanan, columns=columns, show='headings')
        self.tree_layanan.heading('layanan', text='Layanan')
        self.tree_layanan.heading('biaya', text='Biaya (Rp)')
        self.tree_layanan.column('layanan', width=300)
        self.tree_layanan.column('biaya', width=150, anchor='e')
    
        yscroll = ttk.Scrollbar(frame_layanan, orient=tk.VERTICAL, command=self.tree_layanan.yview)
        self.tree_layanan.configure(yscroll=yscroll.set)
    
        xscroll = ttk.Scrollbar(frame_layanan, orient=tk.HORIZONTAL, command=self.tree_layanan.xview)
        self.tree_layanan.configure(xscroll=xscroll.set)
    
        self.tree_layanan.grid(row=0, column=0, sticky='nsew')
        yscroll.grid(row=0, column=1, sticky='ns')
        xscroll.grid(row=1, column=0, sticky='ew')
    
        frame_layanan.grid_rowconfigure(0, weight=1)
        frame_layanan.grid_columnconfigure(0, weight=1)
    
        for layanan, biaya in layanan_tambahan.items():
            self.tree_layanan.insert('', tk.END, values=(layanan, f"{biaya:,}"))
    
    def create_pemesanan_tab(self, parent):
        # Create a main container frame with scrollbar
        container = ttk.Frame(parent)
        container.pack(fill='both', expand=True)
        
        # Create a canvas
        canvas = tk.Canvas(container)
        canvas.pack(side='left', fill='both', expand=True)
        
        # Add a scrollbar
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        
        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        
        # Create another frame inside the canvas
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        
        # Frame untuk data perusahaan
        frame_data = ttk.LabelFrame(scrollable_frame, text="Data Perusahaan", padding=10)
        frame_data.pack(fill='x', padx=10, pady=5)
        
        # Form input data perusahaan
        ttk.Label(frame_data, text="Nama Perusahaan/Pabrik:").grid(row=0, column=0, sticky='w', pady=2)
        ttk.Entry(frame_data, textvariable=self.nama_perusahaan, width=50).grid(row=0, column=1, pady=2, padx=5)
        
        ttk.Label(frame_data, text="Alamat Lengkap Pabrik:").grid(row=1, column=0, sticky='w', pady=2)
        ttk.Entry(frame_data, textvariable=self.alamat_pabrik, width=50).grid(row=1, column=1, pady=2, padx=5)
        
        ttk.Label(frame_data, text="Nomor Kontak (HP/WhatsApp):").grid(row=2, column=0, sticky='w', pady=2)
        ttk.Entry(frame_data, textvariable=self.no_handphone, width=50).grid(row=2, column=1, pady=2, padx=5)
        
        ttk.Label(frame_data, text="Alamat Email:").grid(row=3, column=0, sticky='w', pady=2)
        ttk.Entry(frame_data, textvariable=self.email, width=50).grid(row=3, column=1, pady=2, padx=5)
        
        ttk.Label(frame_data, text="Nama Penanggung Jawab:").grid(row=4, column=0, sticky='w', pady=2)
        ttk.Entry(frame_data, textvariable=self.nama_pic, width=50).grid(row=4, column=1, pady=2, padx=5)
        
        ttk.Label(frame_data, text="Jabatan Penanggung Jawab:").grid(row=5, column=0, sticky='w', pady=2)
        ttk.Entry(frame_data, textvariable=self.jabatan_pic, width=50).grid(row=5, column=1, pady=2, padx=5)
        
        # Frame untuk pemilihan produk
        frame_produk = ttk.LabelFrame(scrollable_frame, text="Pemilihan Produk", padding=10)
        frame_produk.pack(fill='x', padx=10, pady=5)
        
        ttk.Label(frame_produk, text="Pilih Produk:").grid(row=0, column=0, sticky='w', pady=2)
        produk_options = list(data_produk.keys())
        ttk.Combobox(frame_produk, textvariable=self.produk_dipilih, values=produk_options, width=47).grid(row=0, column=1, pady=2, padx=5)
        
        ttk.Label(frame_produk, text="Jumlah Unit:").grid(row=1, column=0, sticky='w', pady=2)
        ttk.Spinbox(frame_produk, textvariable=self.jumlah_unit, from_=1, to=100, width=10).grid(row=1, column=1, sticky='w', pady=2, padx=5)
        
        # Frame untuk layanan tambahan
        frame_layanan = ttk.LabelFrame(scrollable_frame, text="Layanan Tambahan", padding=10)
        frame_layanan.pack(fill='x', padx=10, pady=5)
        
        # Checkbox untuk layanan tambahan
        for i, layanan in enumerate(layanan_tambahan.keys()):
            cb = ttk.Checkbutton(frame_layanan, text=f"{layanan} (Rp {layanan_tambahan[layanan]:,})", 
                                variable=tk.BooleanVar(), 
                                command=lambda l=layanan: self.toggle_layanan(l))
            cb.grid(row=i//2, column=i%2, sticky='w', pady=2)
        
        # Frame untuk metode pembayaran
        frame_pembayaran = ttk.LabelFrame(scrollable_frame, text="Metode Pembayaran", padding=10)
        frame_pembayaran.pack(fill='x', padx=10, pady=5)
        
        # Radio button untuk metode pembayaran
        for id_metode, metode in metode_pembayaran.items():
            rb = ttk.Radiobutton(frame_pembayaran, text=metode, variable=self.metode_pembayaran, value=id_metode)
            rb.pack(anchor='w', pady=2)
        
        # Frame untuk membership dan pengiriman
        frame_opsi = ttk.LabelFrame(scrollable_frame, text="Opsi Lainnya", padding=10)
        frame_opsi.pack(fill='x', padx=10, pady=5)
        
        # Checkbox membership
        ttk.Checkbutton(frame_opsi, text="Perusahaan terdaftar sebagai member Asosiasi Manufaktur Indonesia (diskon 10%)", 
                       variable=self.membership).pack(anchor='w', pady=2)
        
        # Radio button untuk opsi pengiriman
        ttk.Label(frame_opsi, text="Pilihan Pengiriman:").pack(anchor='w', pady=5)
        ttk.Radiobutton(frame_opsi, text="Pengiriman Standar (2-4 minggu) - Gratis", 
                       variable=self.pengiriman, value=1).pack(anchor='w', pady=2)
        ttk.Radiobutton(frame_opsi, text="Pengiriman Cepat (1 minggu) - Rp 5.000.000", 
                       variable=self.pengiriman, value=2).pack(anchor='w', pady=2)
        ttk.Radiobutton(frame_opsi, text="Pengiriman Ekspres (3 hari) - Rp 12.000.000", 
                       variable=self.pengiriman, value=3).pack(anchor='w', pady=2)
        
        # Tombol Generate Invoice
        ttk.Button(scrollable_frame, text="Generate Invoice", command=self.generate_invoice).pack(pady=10)
        
        # Update scrollregion after all widgets are added
        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    
    def toggle_layanan(self, layanan):
        if layanan in self.layanan_tambahan:
            self.layanan_tambahan.remove(layanan)
        else:
            self.layanan_tambahan.append(layanan)
    
    def create_invoice_tab(self, parent):
        # Frame to hold Text + Scrollbars
        frame = ttk.Frame(parent)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
    
        # Text Widget
        self.invoice_text = tk.Text(frame, wrap=tk.WORD, height=30, width=80)
    
        # Vertical Scrollbar
        yscroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.invoice_text.yview)
        self.invoice_text.configure(yscrollcommand=yscroll.set)
    
        # Horizontal Scrollbar (NEW)
        xscroll = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.invoice_text.xview)
        self.invoice_text.configure(xscroll=xscroll.set)
    
        # Grid layout
        self.invoice_text.grid(row=0, column=0, sticky='nsew')
        yscroll.grid(row=0, column=1, sticky='ns')
        xscroll.grid(row=1, column=0, sticky='ew')
    
        # Configure grid weights
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
    
        #Button
        ttk.Button(parent, text="Cetak Invoice", command=self.cetak_invoice).pack(pady=5)
    
    def generate_invoice(self):
        # Validasi input
        if not self.produk_dipilih.get():
            messagebox.showerror("Error", "Silakan pilih produk terlebih dahulu!")
            return
        
        try:
            jumlah_unit = self.jumlah_unit.get()
            if jumlah_unit <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Jumlah unit harus bilangan bulat positif!")
            return
        
        # Hitung total
        subtotal_produk = data_produk[self.produk_dipilih.get()] * self.jumlah_unit.get()
        subtotal_layanan = sum(layanan_tambahan[layanan] for layanan in self.layanan_tambahan)
        total_sebelum_diskon = subtotal_produk + subtotal_layanan
        
        # Hitung diskon
        diskon = total_sebelum_diskon * 0.1 if self.membership.get() else 0
        total_akhir = total_sebelum_diskon - diskon
        
        # Tambah biaya pengiriman
        if self.pengiriman.get() == 2:
            total_akhir += 5000000
        elif self.pengiriman.get() == 3:
            total_akhir += 12000000
        
        # Generate invoice text
        invoice = "=============== INVOICE PEMESANAN ===============\n\n"
        invoice += f"Perusahaan: {self.nama_perusahaan.get()}\n"
        invoice += f"Alamat Pabrik: {self.alamat_pabrik.get()}\n"
        invoice += f"Kontak: {self.nama_pic.get()} ({self.jabatan_pic.get()})\n"
        invoice += f"Telepon: {self.no_handphone.get()} | Email: {self.email.get()}\n\n"
        
        invoice += "DETAIL PEMESANAN:\n"
        invoice += "-------------------------------------------------\n"
        invoice += f"Produk: {self.produk_dipilih.get()} ({self.jumlah_unit.get()} unit)\n"
        invoice += f"Harga Satuan: Rp {data_produk[self.produk_dipilih.get()]:,}\n"
        invoice += f"Subtotal Produk: Rp {subtotal_produk:,}\n\n"
        
        if self.layanan_tambahan:
            invoice += "LAYANAN TAMBAHAN:\n"
            for layanan in self.layanan_tambahan:
                invoice += f"- {layanan}: Rp {layanan_tambahan[layanan]:,}\n"
            invoice += f"Subtotal Layanan: Rp {subtotal_layanan:,}\n\n"
        
        invoice += "RINCIAN PEMBAYARAN:\n"
        invoice += "-------------------------------------------------\n"
        invoice += f"Total Sebelum Diskon: Rp {total_sebelum_diskon:,}\n"
        invoice += f"Diskon: Rp {diskon:,}\n"
        
        biaya_pengiriman = 0
        if self.pengiriman.get() == 2:
            biaya_pengiriman = 5000000
        elif self.pengiriman.get() == 3:
            biaya_pengiriman = 12000000
        
        invoice += f"Biaya Pengiriman: Rp {biaya_pengiriman:,}\n"
        invoice += f"TOTAL PEMBAYARAN: Rp {total_akhir:,}\n\n"
        
        invoice += "METODE PEMBAYARAN:\n"
        invoice += f"{metode_pembayaran[self.metode_pembayaran.get()]}\n\n"
        
        invoice += "INFO PENGIRIMAN:\n"
        if self.pengiriman.get() == 1:
            invoice += "Estimasi pengiriman: 2-4 minggu\n"
        elif self.pengiriman.get() == 2:
            invoice += "Estimasi pengiriman: 1 minggu\n"
        else:
            invoice += "Estimasi pengiriman: 3 hari\n\n"
        
        invoice += "\nTERIMA KASIH TELAH MEMESAN DENGAN KAMI!\n"
        invoice += "Tim support kami akan menghubungi Anda dalam 1x24 jam untuk konfirmasi pemesanan.\n"
        invoice += "Untuk pertanyaan lebih lanjut, hubungi 1500-123 (Customer Service 24/7)\n"
        invoice += "=================================================\n"
        
        # Tampilkan invoice
        self.invoice_text.delete(1.0, tk.END)
        self.invoice_text.insert(tk.END, invoice)
        
        # Pindah ke tab invoice
        notebook = self.root.children['!notebook']
        notebook.select(2)
    
    def cetak_invoice(self):
        # Simpan invoice ke file txt
        try:
            with open('invoice_pemesanan.txt', 'w') as f:
                f.write(self.invoice_text.get(1.0, tk.END))
            messagebox.showinfo("Sukses", "Invoice berhasil disimpan sebagai invoice_pemesanan.txt")
        except:
            messagebox.showerror("Error", "Gagal menyimpan invoice!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManufaktur(root)
    root.mainloop()