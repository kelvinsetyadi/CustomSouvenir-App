from tabulate import tabulate
items = [
    {"item": "tumbler", "variant": ["coffee"], "color": ["hitam","putih","pink","hijau","abu"], "size(ml)":[380,510],"stock": 500, "custom_process": ["sablon (+Rp.3000/pcs)","sticker DTF UV (+Rp.8000/pcs)"], "harga": 35000},
    {"item": "tumbler", "variant": ["sports"], "color": ["hitam","putih","merah","biru",], "size(ml)":[600,800,1000],"stock": 500, "custom_process": ["sablon (+Rp.3000/pcs)", "sticker DTF UV (+Rp.8000/pcs)"], "harga": 50000},
    {"item": "tumbler", "variant": ["vacuum"], "color": ["hitam","putih","merah","gold","silver"], "size(ml)":[500],"stock": 500, "custom_process":["sablon (+Rp.3000/pcs)", "sticker DTF UV (+Rp.8000/pcs)"], "harga": 25000},
    {"item": "mug", "variant": ["keramik","stainless"],"color": ["hitam", "putih"],"stock": 500, "custom_process":["mug press (+Rp.5000/pcs)","sticker DTV UV (+Rp.8000/pcs)"], "harga": 10000},
    {"item": "payung", "variant": ["lipat","panjang"], "color": ["hitam","orange","merah","biru dongker"] ,"stock": 500,"custom_process": ["sablon (+Rp.4000/pcs)","DTF (+Rp.6000/pcs)"], "harga": 25000},
    {"item": "lanyard", "variant": ["leher", "gantungan kunci"], "color": ["hitam","putih"],"stock": 500, "custom_process":["DTF (+Rp.6000/pcs)","sublim (+Rp.4000/pcs)"], "harga": 5000},
    {"item": "tote bag", "variant": ["kecil","sedang","besar"], "color": ["cream","hitam","putih"],"stock": 500, "custom_process":["DTF (+Rp.6000/pcs)","sablon (+Rp.4000/pcs)"], "harga": 25000}
]

cart = []

def show_list_souvenir():
    table_data = []
    for index, item in enumerate(items, start=1):
        size_info = item.get("size(ml)", "-")
        size_str = ", ".join(map(str, size_info)) if isinstance(size_info, list) else str(size_info)
        variant_str = ", ".join(item.get("variant", ["-"])) if isinstance(item.get("variant", []), list) else item.get("variant", "-")
        color_str = ", ".join(item.get("color", ["-"]))

        row = [
            index,
            item.get("item", "-"),
            variant_str,
            color_str,
            size_str,
            item.get("stock", "-"),
            ", ".join(item.get("custom_process", ["-"])),
            f"Rp.{item.get('harga', 0):,}"
        ]
        table_data.append(row)

    headers = ["Index", "Item", "Variant", "Color", "Size (ml)", "Stock (Pcs)", "Custom Process", "Harga (Rp)"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

# ==================================================================================================================================    

def called_list_number():
    nama_item = input("\nMasukkan nama item yang ingin ditampilkan (pisahkan dengan koma jika lebih dari satu): ").strip().lower()
    if not nama_item:
        print("Nama item tidak boleh kosong.")
        return

    nama_item_list = [item.strip() for item in nama_item.split(",")]
    table_data = []

    for item in items:
        if item["item"].lower() in nama_item_list:
            size_info = item.get("size(ml)", "-")
            size_str = ", ".join(map(str, size_info)) if isinstance(size_info, list) else str(size_info)
            variant_str = ", ".join(item.get("variant", ["-"])) if isinstance(item.get("variant", []), list) else item.get("variant", "-")
            color_str = ", ".join(item.get("color", ["-"]))

            row = [
                item.get("item", "-"),
                variant_str,
                color_str,
                size_str,
                item.get("stock", "-"),
                ", ".join(item.get("custom_process", ["-"])),
                f"Rp.{item.get('harga', 0):,}"
            ]
            table_data.append(row)

    if table_data:
        headers = ["Item", "Variant", "Color", "Size (ml)", "Stock (Pcs)", "Custom Process", "Harga (Rp)"]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    else:
        print("Item yang dicari tidak ditemukan.")

# ==================================================================================================================================

def validate_admin():
    """Validasi admin dengan password biasa"""
    user_role = input("Apakah Anda admin? (y/n): ").strip().lower()
    if user_role == "y":
        password = input("Masukkan password admin: ")
        if password == "purwadhika":
            print("Login berhasil. Anda dapat mengubah items.")
            return True
        else:
            print("Password salah. Akses ditolak.")
            return False
    else:
        print("Selain admin dilarang mengubah items.")
        return False

# ==================================================================================================================================

def update_items():
    if not validate_admin():
        return

    while True:
        print("\n1. Update item yang ada\n2. Tambah item baru\n3. Hapus item\n4. Kembali ke menu utama")
        pilihan = input("Pilih sub-menu (1/2/3/4): ")
        if pilihan == "1":
            show_list_souvenir()
            try:
                index = int(input("\nMasukkan index item yang ingin diupdate: ")) - 1
                if index < 0 or index >= len(items):
                    print("Index tidak valid. Silakan coba lagi.")
                    continue
                item = items[index]
                print("\nMasukkan data baru untuk item ini (kosongkan jika tidak ingin mengubah):")
                new_item = input("Item (wajib, hanya huruf): ") if input("\nUpdate item? (y/n): ") == "y" else item.get("item")
                while new_item and not new_item.isalpha():
                    print("Input item tidak valid. Harus berupa huruf saja.")
                    new_item = input("Item (wajib, hanya huruf): ")
                new_variant = input("Variant (pisahkan dengan koma jika lebih dari satu): ").split(",") if input("\nUpdate variant? (y/n): ") == "y" else item.get("variant")
                new_color = input("Color (pisahkan dengan koma jika lebih dari satu): ").split(",") if input("\nUpdate color? (y/n): ") == "y" else item.get("color")
                new_size = input("Size (ml, pisahkan dengan koma jika lebih dari satu): ").split(",") if input("\nUpdate size? (y/n): ") == "y" else item.get("size(ml)","-")
                while True:
                    try:
                        new_stock = int(input("\nStock (wajib): "))
                        break
                    except ValueError:
                        print("Stock harus berupa angka. Masukkan ulang stock.")
                while True:
                    try:
                        new_price = int(input("\nHarga (wajib): "))
                        break
                    except ValueError:
                        print("Harga harus berupa angka. Masukkan ulang harga.")
                new_custom_process = input("\nCustom Process (pisahkan dengan koma jika lebih dari satu): ").split(",") if input("\nUpdate custom process? (y/n): ") == "y" else item.get("custom_process")
                
                item.update({
                    "item": new_item if new_item else item["item"],
                    "variant": new_variant if new_variant else item.get("variant"),
                    "color": new_color,
                    "size(ml)": new_size,
                    "stock": new_stock,
                    "custom_process": new_custom_process,
                    "harga": new_price
                })
                print("Data item berhasil diperbarui!")
                show_list_souvenir()
            except ValueError:
                print("Input tidak valid. Masukkan angka yang benar.")

        elif pilihan == "2":
            print("\nTambah item baru:")
            while True:
                item_name = input("Masukkan nama item: ").strip()
                if not item_name:
                    print("Item tidak boleh kosong, silakan masukkan nama item.")
                    continue
                if item_name.isdigit():
                    print("Item hanya boleh huruf, silakan coba lagi.")
                    continue
                break
            
            while True:
               variant_name = input("\nMasukkan variant (kosong jika tidak ada): ").strip() 
               for item in items:
                if variant_name in item.get("variant", []):
                        print("Variant sudah ada dalam daftar! Kembali ke menu utama.")
                        return
               if variant_name.isdigit():
                    print("Variant hanya boleh huruf, silakan coba lagi.")
                    continue
               break 

            while True:
                color_input = input("\nMasukkan color (pisahkan dengan koma, kosong jika tidak ada): ").strip()
                if not color_input:
                    color_list = []
                    break
                color_list = [color.strip() for color in color_input.split(",")]
                if any(any(char.isdigit() for char in color) for color in color_list):
                    print("Color hanya boleh huruf, silakan coba lagi.")
                else:
                    break

            while True:
                size_input = input("\nMasukkan size (ml) (pisahkan dengan koma, kosong jika tidak ada): ").strip()
                size_data = []
                if size_input:
                    if not size_input.replace(",", "").replace(" ", "").isdigit():
                        print("Size hanya boleh angka, silahkan coba lagi")
                    else:
                        size_data = list(map(int, size_input.split(","))) if "," in size_input else [int(size_input)]
                        print(size_data)
                        break
                else: 
                    break

            while True:
                try:
                    stock_input = int(input("\nMasukkan stock: "))
                    break
                except ValueError:
                    print("Stock hanya boleh angka, silahkan coba lagi.")

            custom_process_input = input("\nMasukkan custom process (pisahkan dengan koma, kosong jika tidak ada): ").strip()
            custom_process_list = [process.strip() for process in custom_process_input.split(",")] if custom_process_input else []

            while True:
                try:
                    price_input = int(input("\nMasukkan harga: "))
                    break
                except ValueError:
                    print("Harga tidak boleh kosong, silakan coba lagi.")

            # Tambahkan item baru ke daftar items
            new_item = {
                "item": item_name,
                "variant": variant_name if variant_name else "-",
                "color": color_list,
                "size(ml)": size_data if size_data else "-",
                "stock": stock_input,
                "custom_process": custom_process_list,
                "harga": price_input
            }
            items.append(new_item)
            print("\nItem baru berhasil ditambahkan.")
            show_list_souvenir()

        elif pilihan == "3":
            print("\nHapus item:")
            if not validate_admin():
                return

            while True:
                show_list_souvenir()
                try:
                    index = int(input("Masukkan index item yang ingin dihapus (0 untuk kembali): ")) - 1
                    if index == -1:
                        break
                    if 0 <= index < len(items):
                        hapus_item = items.pop(index)
                        print(f"Item {hapus_item['item']} variant {hapus_item['variant']} berhasil dihapus.")
                        show_list_souvenir()
                        break
                    else:
                        print("Index tidak valid. Silakan coba lagi.")
                except ValueError:
                    print("Input harus berupa angka. Silakan coba lagi.")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# ==================================================================================================================================

def create_order():
    current_cart = []

    print("\n=== Order souvenir sesuai list ===")
    show_list_souvenir()
    
    customer_name = input("\nMasukkan nama customer: ")
    while not customer_name.isalpha():
        print("Nama harus berupa huruf!")
        customer_name = input("Masukkan nama customer: ")
    
    current_cart.append(customer_name)

    index = 0
    while True:
        try:
            index = int(input("\nMasukan index: "))
            if index < len(items) + 1 and index > 0:
                current_cart.append(items[index -1]["item"])
                break
            else:
                print("Index tidak valid, silahkan ")
        except ValueError:
            print("Index hanya berupa angka")

    list_variant = items[index -1]["variant"]
    print(f"\n Variant yang tersedia {', '.join(list_variant)}")
    while True:
        variant = input("Masukan variant: ").lower()
        if variant in list_variant:
            current_cart.append(variant)
            break
        else:
            print("Variant tidak tersedia")

    list_color = items[index -1]["color"]
    print(f"\nWarna yang tersedia {', '.join(list_color)}")
    while True:
        colors = input("Masukan warna (Pilihan warna lebih dari satu menggunakan koma(,)): ").replace(" ","").lower().split(",")
        is_input_valid = True
        for color in colors:
            if color in list_color:
                continue
            else:
                is_input_valid = False
                print("Input tidak valid")
                break
    
        if is_input_valid:
            box_warna = ""
            for color in colors:
                box_warna += color + ","
            current_cart.append(box_warna)
            break

    if "size(ml)" in items[index -1]:
        list_size = items[index -1]["size(ml)"]
        print(f"\nsize tumbler yang tersedia {list_size}")

        while True:
            try:
                size = int(input("Masukan size: "))
                if size in list_size:
                    current_cart.append(size)
                    break
                else:
                    print("size tidak tersedia")
            except ValueError:
                print("Size harus berupa angka, silahkan coba lagi")

    else:
        current_cart.append("-")

    list_stock = items[index -1]["stock"]
    print(f"\nStock tersedia {list_stock}")

    order = 0

    while True:
        try:
            order = int(input("Masukan jumlah pesanan: "))

            if order <= list_stock:
                current_cart.append(order)
                break
            else: 
                print(f"Stock hanya ada {list_stock}, silahkan input ulang")
        except ValueError:
            print("Jumlah pesanan harus berupa angka, silahkan coba lagi")

    list_custom_order = items[index -1]["custom_process"]
    print("\n0. Polosan")
    all_custom = ""
    counter = 1
    for custom in list_custom_order:
        print(f"{counter}. {custom}")
        counter += 1
        all_custom += custom
    if counter > 2:
        print(f"{counter}. {all_custom}")

    price = items[index -1]["harga"]
    current_cart.append(f"Rp.{price:,}")

    while True:
        custom_orders = int(input("pilih custom process: "))
        if custom_orders == 0:
            current_cart.append("polos")
            current_cart.append(price*order)
            break
        elif custom_orders == counter:
            custom_price = 0
            for custom in list_custom_order:
                custom_price += int(custom.split("(+Rp.")[1].split("/pcs)")[0])   
            current_cart.append(list_custom_order)
            current_cart.append((price + custom_price)*order)
            break

        elif custom_orders > counter + 1:
            print("Input tidak valid")

        else:
            custom_price = int(list_custom_order[custom_orders - 1].split("(+Rp.")[1].split("/pcs)")[0])
            current_cart.append(list_custom_order[custom_orders - 1])
            current_cart.append((price + custom_price)*order)
            break
    cart.append(current_cart)
    show_cart()

# ==================================================================================================================================

def show_cart():
    print("\n=== Daftar Pesanan ===")
    headers = ["Customer", "Item", "Variant", "Color", "Size", "Quantity", "Item Price", "Custom Process","Total Price"]
    table_data = []
    for item in cart:
        row = [item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],f"Rp.{item[8]:,}"]
        table_data.append(row)
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

# ==================================================================================================================================

def delete_cart():
    show_cart()
    delete_index = []
    while True:
        delete_order_name = input("\nPilih nama customer yang hendak dihapus ordernya: ")
        for idx,customer in enumerate(cart):
            if customer[0] == delete_order_name:
                delete_index.append(idx)
        if len(delete_index) == 0:
            print("User tidak ada")
            break
        for index in delete_index:
            cart.pop(index)
        break

# ==================================================================================================================================

def payment():
    show_cart()
    total = 0
    delete_index = []

    while True:
        cutomer_payment_name = input("\nPilih nama customer yang hendak melakukan pembayaran: ")
        for idx,customer in enumerate(cart):
            if customer[0] == cutomer_payment_name:
                total += customer[-1]
                delete_index.append(idx)
        if total == 0:
            print("User tidak ada")
            return
        else:
            print(f"Total harga yang harus dibayar Rp.{total:,}")
            break

    while True:
        try:
            uang_diberikan = int(input("\nMasukkan nominal uang yang diberikan: "))
            break
        except ValueError:
            print("Nominal harus berupa angka, silahkan coba lagi")

    while True:
        sisa_uang = total - uang_diberikan
        if uang_diberikan > total:
            print(f"Kembalian: Rp.{uang_diberikan - total:,}")
            print("\nTerima kasih telah berbelanja di Xmat!")
            for index in delete_index:
                cart.pop(index)
            break
        elif uang_diberikan < total:
            print(f"Uang kurang: Rp.{total - uang_diberikan:,}")
            try:
                uang_tambahan = int(input("\nMasukan sisa nominal yang kurang: "))
                total = sisa_uang
                uang_diberikan = uang_tambahan
            except ValueError:
                print("Nominal harus berupa angka, silahkan coba lagi")
        else:
            print("\nPembayaran pas. Terima kasih!")
            for index in delete_index:
                cart.pop(index)
            break

# ==================================================================================================================================

import sys
def exit_program():
    print("Terima kasih telah berbelanja di Xmat, sampai jumpa kembali")
    sys.exit()

# ==================================================================================================================================

while True:
    title = "XMAT - Toko Custom Souvenir Bandung"
    border = "+" + "=" * (len(title) + 2) + "+"
    print(f"\n{border}")
    print(f"| {title} |")
    print(border)
    
    
    while True:
        print("\nList Menu:")
        print("1. Daftar Pilihan Souvenir")
        print("2. Update Stock")
        print("3. Buat Custom Souvenir Pilihanmu")
        print("4. Daftar Pesanan")
        print("5. Pembayaran")
        print("6. Exit")
        
        choice = input("\nPilih menu: ")
        try:
            if choice == "1":
                print("\n1. Tampilkan semua daftar list souvenir")
                print("2. Tampilkan berdasarkan item ")
                print("3. Kembali ke menu utama")
                sub_choice = input("Pilih sub-menu (1/2/3): ")
                if sub_choice == "1":
                    show_list_souvenir()
                elif sub_choice == "2":
                    called_list_number()
                elif sub_choice == "3":
                    break
                else:
                    print("\nPilihan tidak valid!")  
            elif choice == "2":
                update_items()
            elif choice == "3":
                print("1. Order souvenir sesuai list")
                print("2. Kembali ke menu utama")
                sub_choice = input("Pilih sub-menu (1/2): ")
                if sub_choice == "1":
                    create_order()
                elif sub_choice == "2":
                    break
                else:
                    print("\nPilihan tidak valid!")      
            elif choice == "4":
                while True:
                    print("\n1. Tampilkan daftar order")
                    print("2. Hapus data order")
                    print("3. Kembali ke menu utama")
                    sub_choice = input("Pilih sub-menu (1/2/3): ")
                    if sub_choice == "1":
                        show_cart()
                    elif sub_choice == "2":
                        delete_cart()
                    elif sub_choice == "3":
                        break
                    else:
                        print("\nPilihan tidak valid!")
            elif choice == "5":
                payment()
            elif choice == "6":
                exit_program()
                break
            else:
                print("Menu tidak valid.")
                break
        except ValueError:
            print("Menu tidak valid.")
    
