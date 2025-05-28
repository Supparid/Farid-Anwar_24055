import tkinter as tk
from app_structure import MainApp
from catalog_module import ProductCatalog
from order_module import OrderForm
from invoice_module import InvoiceGenerator

class ManufacturingApp(MainApp):
    def __init__(self, root):
        super().__init__(root)
        self.setup_modules()

    def setup_modules(self):
        # Inisialisasi semua modul
        ProductCatalog(self.tab_katalog)
        OrderForm(self.tab_pemesanan)
        InvoiceGenerator(self.tab_invoice)

if __name__ == "__main__":
    root = tk.Tk()
    app = ManufacturingApp(root)
    root.mainloop()
