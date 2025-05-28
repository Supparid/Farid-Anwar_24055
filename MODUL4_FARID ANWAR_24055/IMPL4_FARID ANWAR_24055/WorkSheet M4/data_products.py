# Database produk
PRODUCTS = {
    "Mesin CNC": 850_000_000,
    "Robot Industri": 1_200_000_000,
    "Conveyor Belt": 350_000_000,
    "Musangking": 123_000_000_000,
    "MIe Ayam Premium": 150_000
}

# Database layanan tambahan
SERVICES = {
    "Instalasi": 15_000_000,
    "Pelatihan": 5_000_000
}

# Metode pembayaran
PAYMENT_METHODS = {
    1: "Transfer Bank",
    2: "Virtual Account"
}

def add_product(name, price):
    """
    Menambahkan produk baru ke dalam database.
    
    :param name: Nama produk
    :param price: Harga produk (int)
    """
    PRODUCTS[name] = price

def get_product_price(name):
    """
    Mengambil harga produk berdasarkan nama.

    :param name: Nama produk
    :return: Harga produk (int), 0 jika tidak ditemukan
    """
    return PRODUCTS.get(name, 0)
