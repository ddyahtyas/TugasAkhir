import csv
import os

csv_filename = 'contacts.csv'

'''Fungsi ini akan kita gunakan untuk membersihkan layar. Fungsi ini sebenarnya akan menjalankan perintah cls 
(jika di Windows) dan clear (jika di Linux dan Unix).'''
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI BUKU TELEPON ===")
    print("[1] Lihat Daftar Kotak")
    print("[2] Buat Kontak Baru")
    print("[3] Edit Kontak")
    print("[4] Hapus Kontak")
    print("[5] Cari Kontak")
    print("[6] Mengurutkan Kontak")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")

    if (selected_menu == "1"):
        show_contact()
    elif (selected_menu == "2"):
        create_contact()
    elif (selected_menu == "3"):
        edit_contact()
    elif (selected_menu == "4"):
        delete_contact()
    elif (selected_menu == "5"):
        search_concat()
    elif (selected_menu == "6"):
        sorting_contact()
    elif (selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

def show_contact():
    clear_screen()
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    if (len(contacts) > 0):
        #pop untuk menghapus
        labels = contacts.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t\t {labels[2]}")
        print("-" * 34)
        for data in contacts:
            print(f'{data[0]} \t {data[1]} \t\t\t {data[2]}')
    else:
        print("Tidak ada data!")
    back_to_menu()


def create_contact():
    clear_screen()
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    no = int(contacts[len(contacts) - 1][0]) + 1
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NO', 'NAMA', 'TELEPON']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        #no = input("No urut: ")
        nama = input("Nama lengkap: ")
        telepon = input("No. Telepon: ")

        writer.writerow({'NO': no, 'NAMA': nama, 'TELEPON': telepon})
        no += 1

    back_to_menu()


def search_concat():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    no = input("Cari berdasrakan nomer urut> ")

    data_found = []

    # mencari contact
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            data_found = contacts[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Nama: {data_found['NAMA']}")
        print(f"Telepon: {data_found['TELEPON']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()


def edit_contact():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NAMA \t\t TELEPON")
    print("-" * 32)

    for data in contacts:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['TELEPON']}")

    print("-----------------------")
    no = input("Pilih nomer kontak> ")
    nama = input("nama baru: ")
    telepon = input("nomer telepon baru: ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            contacts[indeks]['NAMA'] = nama
            contacts[indeks]['TELEPON'] = telepon
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'TELEPON']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON']})

    back_to_menu()


def delete_contact():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NAMA \t\t TELEPON")
    print("-" * 32)

    for data in contacts:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['TELEPON']}")

    print("-----------------------")
    no = input("Hapus nomer> ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'TELEPON']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['TELEPON']})

    print("Data sudah terhapus")
    back_to_menu()

def sorting_contact():
    clear_screen()
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)
    label = contacts.pop(0)

    for i in range(len(contacts)):
        contacts[i][1] = str(contacts[i][1])

    max = len(contacts) - 1
    for x in range(max, 0, -1):
        for y in range(x):
            if contacts[y][1] > contacts[y + 1][1]:
                temp = contacts[y + 1]
                contacts[y + 1] = contacts[y]
                contacts[y] = temp

    print("%10s \t %10s" % ("nama ", "kontak"))
    for row in contacts:
        print("%10s \t %10s" % (row[1], row[2]))
    back_to_menu()

while True:
    show_menu()
