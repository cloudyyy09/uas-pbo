# membuat kelas baru yakni menu
class Menu:
    # membuat item yang akan di masukkan kedalam menu
    def __init__(self):
        self.menu_items = {
            1: {"name": "Nasi Goreng", "price": 15000},
            2: {"name": "Mie Ayam", "price": 12000},
            3: {"name": "Sate Ayam", "price": 10000},
            4: {"name": "Bakso", "price": 8000},
            5: {"name": "Gado-gado", "price": 15000}
        }

    # fungsi untuk Menampilkan daftar menu beserta harga.
        
    def display_menu(self):
        print("Daftar Menu:")
        for item_id, item_info in self.menu_items.items():
            print(f"{item_id}. {item_info['name']} - Rp{item_info['price']}")
    
    # fungsi untuk Mendapatkan harga suatu item berdasarkan ID-nya.
    def get_menu_price(self, item_id):
        if item_id in self.menu_items:
            return self.menu_items[item_id]['price']
        return None

# membuat kelas baru yakni order
class Order:
    def __init__(self):
        self.menu = Menu()
        self.order_items = []

    # membuat fungsi untuk menambahkan item ke dalam pesanan.
    def add_item(self, item_id, quantity):
        price = self.menu.get_menu_price(item_id)
        if price is not None:
            item_total = price * quantity
            item_info = {"name": self.menu.menu_items[item_id]['name'], "quantity": quantity, "price": price,
                         "total": item_total}
            self.order_items.append(item_info)
            print(f"{quantity} x {self.menu.menu_items[item_id]['name']} = Rp{item_total}")
            print(f"{quantity} {self.menu.menu_items[item_id]['name']} ditambahkan ke pesanan.")
        else:
            print("Item tidak tersedia.")

    # fungsi untuk menghapus item dari pesanan.
    def remove_item(self, item_index):
        if item_index >= 0 and item_index < len(self.order_items):
            item_info = self.order_items[item_index]
            del self.order_items[item_index]
            print(f"{item_info['quantity']} x {item_info['name']} = Rp{item_info['total']}")
            print(f"{item_info['quantity']} {item_info['name']} dihapus dari pesanan.")
        else:
            print("Item tidak ditemukan dalam pesanan.")

    # fungsi untuk menghitung total harga pesanan.
    def calculate_total(self):
        total = 0
        for item_info in self.order_items:
            total += item_info['total']
        return total

    # fungsi untuk menampilkan isi pesanan.
    def display_order(self):
        if len(self.order_items) == 0:
            print("Pesanan kosong.")
        else:
            print("Pesanan:")
            for index, item_info in enumerate(self.order_items):
                print(f"{index+1}. {item_info['name']} - {item_info['quantity']} x {item_info['price']} = Rp{item_info['total']}")

    # fungsi untuk menyelesaikan dan melakukan pemesanan.
    def place_order(self):
        if len(self.order_items) == 0:
            print("Pesanan kosong. Tidak dapat melakukan pemesanan.")
        else:
            total = self.calculate_total()
            print(f"Total harga: Rp{total}")
            print("Pesanan berhasil ditempatkan.")
            print("\nTerima kasih telah menggunakan Fasilitas Pemesanan Makanan!")

# fungsi utama untuk memanggil kelas order dan memunculkan menu
def main():
    order = Order()
    order.menu.display_menu()

# perulangan untuk menampilkan menu utama agar jika pengguna ingin menambah atau menghapus tidak kebingungan
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Item ke Pesanan")
        print("2. Hapus Item dari Pesanan")
        print("3. Lihat Pesanan")
        print("4. Selesai dan Pesan")
        print("5. Keluar")

        choice = input("Silakan pilih tindakan (1-5): ")

        print("==============================")
        
# kondisi jika memilih salah satu menu. 
        if choice == '1':
            item_id = int(input("Masukkan ID item yang ingin ditambahkan: "))
            quantity = int(input("Masukkan jumlah item yang ingin ditambahkan: "))
            order.add_item(item_id, quantity)
        elif choice == '2':
            order.display_order()
            item_index = int(input("Masukkan nomor item yang ingin dihapus: ")) - 1
            order.remove_item(item_index)
        elif choice == '3':
            order.display_order()
        elif choice == '4':
            order.place_order()
            break
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

        print("==============================")

if __name__ == "__main__":
    main()
