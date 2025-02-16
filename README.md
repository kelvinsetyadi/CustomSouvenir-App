# XMAT - Toko Custom Souvenir Bandung 

XMAT merupakan toko souvenir di kota Bandung yang menyediakan layanan produk dan jasa kustomisasi souvenir. Dengan bertambahnya customer beserta banyaknya produk souvenir yang disediakan dan jasa kostumisasi yang dapat dilakukan, maka perlu adanya sistem yang dapat menyimpan daftar item, warna, variant, harga item, harga jasa kostumisasi, beserta daftar order customer. Dengan sistem pemesanan ini, admin XMAT diharapkan dapat memangkas waktu untuk pengecekan jumlah stock berdasarkan variabel-variabelnya, pengecekan harga atau update harga, serta mengetahui daftar customer yang masih belum melakukan pembayaran.

## Tampilan Menu Utama Sistem
Sistem pemesanan ini terdiri dari:
1. Daftar pilihan souvenir
3. Update stock
4. Buat custom souvenir pilihanmu
5. Daftar pesanan
6. Pembayaran
7. Exit
   
### 1. Daftar pilihan souvenir
Terdapat 3 sub-menu pada menu 1:
1. Tampilkan semua daftar list souvenir
    - Pilihan ini menampilkan dalam bentuk tabel seluruh item, variant, warna, size (khusus tumbler), jenis-jenis kostumisasi beserta harga, dan harga dari setiap item. 
3. Tampilkan berdasarkan item
    - Tabel bisa ditampilkan/filter berdasarkan nama item yang diinput, contoh jika kita memasukan item tumbler, segala jenis item tumbler akan ditampilkan pada tabel dan item selain item tumbler tidak akan di munculkan. Tetapi kita bisa memfilter lebih dari satu nama dengan menambahkan koma(,).
5. Kembali ke menu utama
    - Menu ini bertujuan untuk keluar dari menu 1 dan hendak kembali ke menu utama

### 2. Update stock
ketika memilih menu 2, akan diminta untuk input password yang bertujuan agar tidak semua dapat mengakses dan merubah daftar stock pada sistem.
Terdapat 4 sub-menu pada menu 2: 
1. Update item yang ada
    - Sistem ini memungkinkan untuk dapat mengubah value/isi dari isi table data. Data yang dapat diubah meliputi nama item, variant, warna, size (khusus untuk tumbler), jenis kostumisasi beserta harga, dan harga item
3. Tambah item baru
    - tabel data dapat ditambahkan dengan item baru. yang wajib diisi hanya nama item, stock, dan harga. 
5. Hapus item
    - Jika sudah tidak dibutuhkan, item dapat dihapus berdasarkan index kolom.
7. Kembali ke menu utama
    - Menu ini bertujuan untuk keluar dari menu 2 dan hendak kembali ke menu utama.

### 3. Buat custom souvenir pilihanmu
Terdapat 2 sub-menu pada menu 3:
1. Order souvenir sesuai list
    - Menu ini digunakan untuk kostumisasi souvenir setiap customer berdasarkan variabel-variabel yang disediakan pada tabel.
3. Kembali ke menu utama
    - Menu ini bertujuan untuk keluar dari menu 3 dan hendak kembali ke menu utama.

### 4. Daftar pesanan
Terdapat 3 sub-menu pada menu 4:
1. Tampilkan daftar order
    - Setelah kostumisasi souvenir customer menjadi order, maka pada menu ini akan ditampilkan seluruh daftar order beserta nominal harga yang harus dibayarkan oleh setiap customer.
3. Hapus data order
    - Customer memungkinkan untuk menghapus orderannya jika terdapat kondisi tertentu. Menu ini dapat menghapus datar order berdasarkan nama customer.
5. Kembali ke menu utama
    - Menu ini bertujuan untuk keluar dari menu 1 dan hendak kembali ke menu utama.

### 5. Pembayaran
Ketika menjalankan menu pembayaran, maka akan muncul daftar order customer yang belum lunas. Menu ini dimulai dari memasukan nama customer yang hendak melakukan pembayaran lalu akan muncul nominal rupiah yang harus dibayarkan. Menu ini juga akan menampilkan jumlah kekurangan uang yang dibayarkan dan mengharuskan untuk pembayaran hingga lunas.


### 6. Exit
Jika sudah selesai menggunakan sistem ini, maka user dapat melakukan exit sistem pada menu 6.
