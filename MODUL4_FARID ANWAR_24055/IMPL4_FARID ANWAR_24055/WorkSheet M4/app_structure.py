import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Manufaktur")
        self.root.geometry("900x700")

        # Buat notebook (tab container)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Buat frame untuk masing-masing tab
        self.setup_tabs()

    def setup_tabs(self):
        """Inisialisasi semua tab"""

        # Tab Katalog
        self.tab_katalog = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_katalog, text="Katalog")

        # Tab Pemesanan
        self.tab_pemesanan = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_pemesanan, text="Pemesanan")

        # Tab Invoice
        self.tab_invoice = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_invoice, text="Invoice")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
