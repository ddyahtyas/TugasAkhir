import csv
import os

csv_filename1 = 'darah.csv'
csv_filename2 = 'pendonoran.csv'
csv_filename3 = 'penerimaan.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI DONOR DARAH ===")
    print("[1] Stock Darah")
    print("[2] Donor Darah")
    print("[3] Transaksi Darah")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")

    if (selected_menu == "1"):
        clear_screen()
        database = []
        # Load data dari CSV
        with open(csv_filename1) as db_file:
            csv_reader = csv.reader(db_file, delimiter=';')
            for row in csv_reader:
                database.append(row)
        print("\n %10s \t %4s" %("JenisDarah","Jumlah"))
        for row in database:
            print("%6s \t %12s" %(row[0],row[1]))
        print("")
        back_to_menu()

    elif (selected_menu == "2"):
        clear_screen()
        database = []
        # Load data dari CSV
        with open(csv_filename1) as db_file:
            csv_reader = csv.reader(db_file, delimiter=';')
            for row in csv_reader:
                database.append(row)

        database2 = []
        with open(csv_filename2) as db_file:
            csv_reader = csv.reader(db_file, delimiter=';')
            for row in csv_reader:
                database2.append(row)
        id_darah = int(database2[len(database2) - 1][0]) + 1

        while True:
            print("1. Tambah Pendonor", "2. Riwayat Pendonor", "3. Selesai")
            jawab = int(input("pilih : "))
            if jawab == 1:
                with open(csv_filename2, mode='a') as db_file:
                    csv_writer = csv.writer(db_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    while True:
                        tgl_donor = input('input tgl/bln/thn : ')
                        nama_pendonor = input('Masukkan Nama: ')
                        gol_darah = input('Golongan darah (A/B/AB/O) : ')
                        jumlah_darah = int(input('Masukkan Jumlah(kantong): '))
                        pilih = input("Tambah pendonor lagi y/n ? : ")

                        csv_writer.writerow([id_darah, tgl_donor, nama_pendonor, gol_darah, jumlah_darah])
                        database2.append([id_darah, tgl_donor, nama_pendonor, gol_darah, jumlah_darah])

                        indeks = 0
                        for i in database:
                            database[indeks][1] = int(database[indeks][1])
                            if (database[indeks][0] == gol_darah):
                                database[indeks][1] = database[indeks][1] + jumlah_darah
                            indeks = indeks + 1

                        # Menulis data baru ke file CSV (tulis ulang)
                        with open(csv_filename1, mode="w") as db_file:
                            fieldnames = ['JenisDarah', 'Jumlah']
                            writer = csv.DictWriter(db_file, fieldnames=fieldnames)
                            writer.writeheader()
                            for new_data in database:
                                writer.writerow(
                                    {'JenisDarah': new_data['JenisDarah'], 'Jumlah': new_data['Jumlah']})

                        print("Barang Telah Ditambahkan\n")
                        if pilih == 'n':
                            break
                        id_darah += 1
                        os.system("clear")

            if jawab == 2:
                print("\n %2s \t %6s \t %10s \t %10s \t %10s " % ("ID", "Tanggal", "Nama", "JenisDarah", "Jumlah"))
                for row in database2:
                    print("%2s \t %11s \t %10s \t %10s \t %10s" % (row[0], row[1], row[2], row[3], row[4]))
                print("")

            else:
                break
        back_to_menu()

    elif (selected_menu == "3"):
        transaksi()
    elif (selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

def transaksi():
    clear_screen()
    database = []
    with open(csv_filename2) as db_file:
        csv_reader = csv.reader(db_file, delimiter=';')
        for row in csv_reader:
            database.append(row)
    while True:
        print("1. Tambah Penerima", "2. Riwayat Penerima", "3. Selesai")
        jawab = int(input("pilih : "))
        if jawab == 1:
            with open(csv_filename2, mode='a') as db_file:
                csv_writer = csv.writer(db_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                while True:
                    tgl_transaksi = input('input tgl/bln/thn : ')
                    nama_penerima = input('Masukkan Nama: ')
                    gol_darah = input('Golongan darah (A/B/AB/O) : ')
                    jumlah_darah = input('Masukkan Jumlah(kantong): ')
                    pilih = input("Tambah penerima lagi y/n ? : ")

                    csv_writer.writerow([tgl_transaksi,nama_penerima,gol_darah, jumlah_darah])
                    database.append([tgl_transaksi,nama_penerima,gol_darah, jumlah_darah])
                    if pilih == 'n' :
                        break
                    os.system("clear")
                    print("Transaksi Berhasil\n")

        if jawab == 2 :
            print("\n %2s \t %6s \t %10s \t %10s " % ("Tanggal", "Nama", "JenisDarah", "Jumlah"))
            for row in database:
                print("%2s \t %11s \t %10s \t %10s" % (row[0], row[1], row[2], row[3]))
            print("")

        if jawab == 3 :
            break

        else:
            print("salah input")

    show_menu()
if __name__ == "__main__":
    while True:
        show_menu()