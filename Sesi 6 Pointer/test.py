def menu():
    import os
    os.system("CLS")
    print("\xB1\xB1 PROGRAM OPERASI DATA KTP \xB1\xB1\n")
    print("Daftar Menu:")
    print("\n[1] Lihat daftar data KTP")
    print("[2] Buat data baru untuk KTP")
    print("[3] Cari data KTP")
    print("[4] Edit data KTP")
    print("[5] Hapus data KTP")
    print("[6] Keluar dari Program")
    pil = input("Pilih Menu >> ")
    pilihmenu(pil)


# --------------------------------------------------------------------------
def pilihmenu(p):
    if p == "1":
        lihatdataktp()
    elif p == "2":
        tambahdataktp()
    elif p == "3":
        caridataktp()
    elif p == "4":
        updatedataktp()
    elif p == "5":
        hapusdataktp()
    else:
        print("\nakan keluar.")


# --------------------------------------------------------------------------
def lihatdataktp():
    print("\n==Anda berada pada menu data KTP==\n")

    f = open("Data/dataktp.txt")
    isi = f.readlines()
    isi.sort()
    if len(isi) == 0:
        print("Data masih kosong")
    else:
        print("No\tNama \tNIK \t\t Jenis Kelamin \t\tAlamat")
        i = 1
        for x in isi:
            pecah = x.split(",")
            print(str(i), end="")
            print("\t" + pecah[0] + "\t" + pecah[1] + "\t\t" + pecah[2] + "\t\t" + pecah[3], end="")
            i += 1
    print("\ntekan [enter]  untuk kembali ke menu")
    f.close()
    input()
    menu()


# --------------------------------------------------------------------------
def tambahdataktp():
    print("\nAnda berada pada menu menambah data")
    print("Masukkan data baru anda.\n")
    n = input("Nama :")
    k = input("NIK :")
    j = input("Jenis Kelamin : ")
    a = input("Alamat :")
    f = open("Data/dataktp.txt", "a")
    f.writelines([n + "," + k + "," + j + "," + a + "\n"])
    print("\ntekan [enter] untuk melanjutkan...")
    f.close()
    input()
    menu()


# --------------------------------------------------------------------------
def caridataktp():
    print("===Anda berada pada  menu mencari data===")
    data = input("\nMasukkan nama yang ingin dicari: ")
    f = open("Data/dataktp.txt", "r")
    dataktp = []
    isi = f.readlines()
    if len(isi) == 0:
        print("Daftar nama belum ada")
    else:
        for x in isi:
            pecah = x.split(",")
        if data == pecah[0]:
            dataktp = pecah
    if dataktp:
        print("No\tNama \t\t\tNIK \t\t Jenis Kelamin \t\tAlamat")
        print("------------------------------")
        print("\t" + pecah[0] + "\t" + pecah[1] + "\t\t" + pecah[2] + "\t\t" + pecah[3], end="")
    else:
        print("Data tidak dditemukan.")
    print("\ntekan [enter] untuk  kembali kemenu...")
    f.close()
    input()
    menu()


# --------------------------------------------------------------------------
def updatedataktp():
    print("\n===Anda berada  pada  menu uodate data===")
    nx = input("\nMasukkan nama data yang ingin di update.")
    print("Masukkann data baru")
    nb = input("Masukkan nama baru :")
    kb = input("Masukkan NIK KTP baru :")
    jb = input("Masukkan Jenis Kelamin baru :")
    ab = input("Masukkan alamat baru :")

    f = open("Data/dataktp.txt")
    isi = f.readlines()
    idx = 0
    for x in isi:
        xp = x.split(",")
        if xp[0] == nx:
            xp[0] = nb
            xp[1] = kb
            xp[2] = jb
            xp[3] = ab + "\n"
            xg = ",".join(xp)
            isi[idx] = xg
        idx += 1
    f = open("Data/dataktp.txt", "w")
    f.writelines(xg)
    print("Tekan [enter] untuk melanjutkan update Data")
    print("Data telah berhasil diupdate")
    f.close()
    input()
    menu()


# --------------------------------------------------------------------------
def hapusdataktp():
    f = open("Data/dataktp.txt")
    isi = f.readlines()
    isi.sort()
    if len(isi) == 0:
        print("Data masih kosong")
    else:
        print("No\tNama \t\t\tNIK \t\t Jenis Kelamin \t\tAlamat")
        i = 1
        for x in isi:
            pecah = x.split(",")
            print(str(i), end="")
            print("\t" + pecah[0] + "\t" + pecah[1] + "\t\t" + pecah[2] + "\t\t" + pecah[3], end="")
            i += 1

    pil = int(input("Masukkan nomor data yang ingin dihapus"))
    y = pil - 1
    del isi[y]
    f.close()
    f = open("Data/dataktp.txt", "w")
    f.writelines(isi)
    print("Tekan [enter] untuk melanjutkan penghapusan")
    print("Data telah berhasil dihapus")
    f.close()
    input()
    menu()


menu()