from tkinter import ttk
from data_products import PRODUCTS

class ProductCatalog:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Katalog Produk")
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        # Treeview untuk menampilkan produk
        self.tree = ttk.Treeview(self.frame, columns=('name', 'price'), show='headings')
        self.tree.heading('name', text='Nama Produk')
        self.tree.heading('price', text='Harga')

        # Scrollbar vertikal
        scrollbar = ttk.Scrollbar(self.frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Tata letak komponen
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Muat data produk
        self.load_products()

    def load_products(self):
        """Memuat data produk ke dalam treeview"""
        for product, price in PRODUCTS.items():
            self.tree.insert('', 'end', values=(product, f"Rp {price:,}"))
