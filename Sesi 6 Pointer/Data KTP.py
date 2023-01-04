def menu():
    import os
    os.system("CLS")
    print("Daftar Menu:")
    print("[1] Menambah data")
    print("[2] Mencari data sesuai kelahiran tertentu")
    print("[3] Menampilkan data berdasarkan gender")
    print("[4] Mengedit data")
    print("[5] Keluar dari program")
    pil = input("\nPilih Menu >>> ")
    pilihmenu(pil)


def pilihmenu(p):
    if p == '1':
        tambahdataktp()
    elif p == '2':
        mencaridataktp()
    elif p == '3':
        lihatdataktp()
    elif p == '4':
        editdataktp()
    else:
        print("Program berhenti")


def tambahdataktp():
    print("Masukan data\n")
    n = input("Nama: ")
    tgl = input("Tanggal lahir: ")
    bln = input("Bulan lahir: ")
    th = input("Tahun lahir: ")
    k = input("Jenis kelamin 'L'/'P': ")
    nik = input("NIK: ")
    f = open("Data/dataktp.txt", "a")
    f.writelines(n + "," + tgl + "," + bln + "," + th + "," + k + "," + nik + "\n")
    print("\ntekan [Enter] untuk melanjutkan...")
    f.close()
    input()
    menu()


def mencaridataktp():
    global pecah
    print("Sesuaikan tanggal, bulan, dan tahun data yang ingin anda cari")
    data1 = input("Tanggal: ")
    data2 = input("Bulan: ")
    data3 = input("Tahun: ")
    #    data = input("Masukan nama yang ingin anda cari: ")
    f = open("Data/dataktp.txt", "r")
    dataktp = []
    isi = f.readlines()
    if len(isi) == 0:
        print("daftar nama belum ada")
    else:
        for x in isi:
            pecah = x.split(",")
        if data1 == pecah[1] and data2 == pecah[2] and data3 == pecah[3]:
            dataktp = pecah[1] + pecah[2] + pecah[3]
    if dataktp:
        print("No\tNama\tTanggal\t\tBulan\tTahun\tJenis Kelamin\tNIk")
        print("----------------------------------------------------------------")
        print("\t" + pecah[0] + "\t" + pecah[1] + "\t\t\t" + pecah[2] + "\t\t" + pecah[3] + "\t" + pecah[4]
              + "\t\t\t\t" + pecah[5], end="")
    else:
        print("data tidak ditemukan")
    print("\ntekan [Enter] untuk melanjutkan...")
    f.close()
    input()
    menu()


def lihatdataktp():
    f = open("Data/dataktp.txt")
    isi = f.readlines()
    isi.sort()
    if len(isi) == 0:
        print("data masih kosong")
    else:
        print("No\tNama\tTanggal\t\tBulan\tTahun\tJenis Kelamin\tNIk")
        i = 1
        for x in isi:
            pecah = x.split(",")
            print(str(i), end="")
            print("\t" + pecah[0] + "\t" + pecah[1] + "\t\t\t" + pecah[2] + "\t\t" + pecah[3] + "\t" + pecah[
                4] + "\t\t\t\t" + pecah[5], end="")
            i += 1
    print("\ntekan [Enter] untuk melanjutkan...")
    f.close()
    input()
    menu()


def editdataktp():
    global xg
    nx = input("Masukan nama data yang ingin di update: ")
    print("Masukan data baru")
    nb = input("Nama baru: ")
    tglb = input("Tanggal lahir baru: ")
    blnb = input("Bulan lahir baru: ")
    thb = input("Tahun lahir baru: ")
    kb = input("Jenis kelamin baru: ")
    nikb = input("NIK baru: ")

    f = open("Data/dataktp.txt")
    isi = f.readlines()
    idx = 0
    for x in isi:
        xp = x.split(",")
        if xp[0] == nx:
            xp[0] = nb
            xp[1] = tglb
            xp[2] = blnb
            xp[3] = thb
            xp[4] = kb
            xp[5] = nikb + "\n"
            xg = ",".join(xp)
            isi[idx] = xg
        idx += 1
    f = open("Data/dataktp.txt", "w")
    f.writelines(xg)
    print("\ntekan [Enter] untuk melanjutkan...")
    print("Data berhasil diupdate")
    f.close()
    input()
    menu()


menu()
