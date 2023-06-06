# uas-pbo
berikut ini merupakan UAS saya Rizki ramadani dengan npm G1A022054 membuat kode fasilitas pemesanan makanan menggunakan python

di dalam program terdapat 2 kelas dan beberapa method atau fungsi yang ada di dalamnya disini saya akan menjelaskan secara keseluruhan fungsi dari program masing - masing

Kelas Menu: yang pertama ada kelas menu di sini kita membuat sebuah menu untuk di tunjukkan oleh user beserta harga makanannya masing - masing agar user tidak kebinggungan untuk memilih makanan nantinya, di dalamnya ada beberapa fungsi dan konstruktor yakni :
init(self): Konstruktor ini digunakan untuk menginisialisasi objek menu. Pada bagian ini, menu_items diisi dengan daftar item makanan dan harga yang disimpan dalam bentuk kamus.

display_menu(self): Fungsi ini bertujuan untuk menampilkan daftar menu beserta harga. Setiap item dalam menu_items akan ditampilkan dengan menggunakan perulangan, dan informasi seperti ID, nama item, dan harga akan dicetak ke layar.

get_menu_price(self, item_id): Fungsi ini digunakan untuk mendapatkan harga suatu item berdasarkan ID-nya. Jika ID item ditemukan dalam menu_items, harga item akan dikembalikan. Jika tidak, fungsi ini akan mengembalikan None.

Kelas Order: yang kedua ada kelas order ini adalah kelas agar user dapat memesan makanannya dengan memilih angka satu sampai lima yang masing masing ada fungsi nya. lebih lengkapnya dapat dilihat dibawah ini.
init(self): Konstruktor ini digunakan untuk menginisialisasi objek pesanan. Pada bagian ini, menu diinisialisasi sebagai objek dari kelas Menu, dan order_items diinisialisasi sebagai sebuah daftar kosong yang akan digunakan untuk menyimpan item pesanan.

add_item(self, item_id, quantity): Fungsi ini digunakan untuk menambahkan item ke dalam pesanan. Pertama, harga item diperoleh dari objek Menu dengan memanggil fungsi get_menu_price. Jika harga ditemukan (tidak None), maka item tersebut ditambahkan ke order_items berserta kuantitas dan harga totalnya. Informasi item juga dicetak ke layar sebagai umpan balik untuk pengguna. fungsi ini akan dijalankan jika user memilih angka 1 pada keyboardnya.

remove_item(self, item_index): Fungsi ini digunakan untuk menghapus item dari pesanan berdasarkan nomor item dalam daftar pesanan. Jika nomor item valid (di antara 1 dan panjang order_items), item tersebut dihapus dari order_items dan informasi item yang dihapus dicetak ke layar sebagai umpan balik untuk pengguna. fungsi ini akan dijalankan jika user menekan angka 2 di keyboardnya.

calculate_total(self): Fungsi ini digunakan untuk menghitung total harga pesanan dengan menjumlahkan harga total dari setiap item dalam order_items. Total harga pesanan kemudian dikembalikan. ini merupakan fungsi untuk menghitung total dari semua pesanan yang di buat dan menghitung harga keseluruhan yang harus di bayar oleh user.

display_order(self): Fungsi ini digunakan untuk menampilkan isi pesanan. Jika daftar pesanan kosong, pesan "Pesanan kosong" dicetak ke layar. Jika tidak, setiap item dalam order_items akan dicetak dengan menggunakan perulangan, termasuk nomor item, nama item, kuantitas, harga per item, dan harga total. fungsi ini akan berjalan jika user menekan angka 3 pada keyboardnya.

place_order(self): Fungsi ini digunakan untuk menyelesaikan proses pemesanan. Jika daftar pesanan kosong, pesan "Pesanan kosong. Tidak dapat melakukan pemesanan" dicetak ke layar. Jika tidak, total harga pesanan dihitung dengan memanggil fungsi calculate_total. Total harga pesanan dicetak ke layar, dan pesan "Pesanan berhasil ditempatkan" dicetak sebagai konfirmasi. fungsi ini adalah fungsi terakhir dalam memesan makanan jika user memilih angka 4 pada keyboard nya maka akan muncul semua pesanan dan harga total yang harus di bayar oleh user.

Fungsi main(): Fungsi ini merupakan fungsi utama yang memulai aplikasi. Pada awalnya, objek Order dan Menu dibuat. Kemudian, fungsi display_menu dari objek Menu dipanggil untuk menampilkan daftar menu. Setelah itu, terdapat perulangan yang memunculkan menu utama dan meminta pengguna untuk memilih tindakan yang diinginkan. Pilihan pengguna diambil menggunakan input, dan kemudian dilakukan pengujian kondisi if-elif-else untuk memanggil fungsi yang sesuai dalam objek Order.

Setiap tindakan yang dilakukan oleh pengguna akan mengakibatkan pemanggilan fungsi-fungsi dalam kelas Order, seperti add_item, remove_item, display_order, dan place_order. Program akan terus berjalan dalam perulangan hingga pengguna memilih opsi "Keluar" (menu nomor 5).

Semoga penjelasan ini dapat membantu dalam memahami lebih rinci tentang program ini.
