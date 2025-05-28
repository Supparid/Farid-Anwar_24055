from tkinter import ttk, END
from tkinter.scrolledtext import ScrolledText

class InvoiceGenerator:
    def __init__(self, parent_frame):
        self.frame = ttk.LabelFrame(parent_frame, text="Invoice")
        self.frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        # Area teks untuk invoice
        self.invoice_text = ScrolledText(self.frame, wrap='word', height=20)
        self.invoice_text.pack(fill='both', expand=True, padx=5, pady=5)

        # Tombol contoh invoice
        ttk.Button(
            self.frame,
            text="Generate Contoh",
            command=self.sample_invoice
        ).pack(pady=5)

    def sample_invoice(self):
        """Contoh invoice untuk testing"""
        sample = (
            "========== INVOICE SAMPLE ==========\n"
            "Nama Perusahaan : Contoh Perusahaan\n"
            "Produk          : Mesin CNC (2 unit)\n"
            "Total           : Rp 1.700.000.000\n"
            "===================================="
        )
        self.invoice_text.delete(1.0, END)
        self.invoice_text.insert(END, sample)
