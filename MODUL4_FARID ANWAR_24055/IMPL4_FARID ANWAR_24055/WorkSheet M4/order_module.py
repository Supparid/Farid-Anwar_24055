from tkinter import ttk, StringVar, IntVar
from data_products import PRODUCTS, SERVICES

class OrderForm:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Form Pemesanan")
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Variabel untuk menyimpan input
        self.company_name = StringVar()
        self.selected_product = StringVar()
        self.quantity = IntVar(value=1)

        self.create_widgets()

    def create_widgets(self):
        # Input nama perusahaan
        ttk.Label(self.frame, text="Nama Perusahaan:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        ttk.Entry(self.frame, textvariable=self.company_name).grid(row=0, column=1, padx=5, pady=5)

        # Dropdown pilihan produk
        ttk.Label(self.frame, text="Pilih Produk:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        product_combo = ttk.Combobox(
            self.frame,
            textvariable=self.selected_product,
            values=list(PRODUCTS.keys()),
            state="readonly"
        )
        product_combo.grid(row=1, column=1, padx=5, pady=5)

        # Input jumlah unit
        ttk.Label(self.frame, text="Jumlah Unit:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        ttk.Spinbox(self.frame, textvariable=self.quantity, from_=1, to=100).grid(row=2, column=1, padx=5, pady=5)
