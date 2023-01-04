def tahun_kabisat():
    t = int(input("Masukan tahun: "))

    if (t % 4 == 0 and t % 100 != 0) or t % 400 == 0:
        print("Adalah tahun kabisat")
    else:
        print("Bukan tahun kabisat")


def donor_darah():
    umur = int(input("Inputkan umur anda: "))
    bb = int(input("Berat badan: "))

    if umur >= 18 and bb >= 50:
        print("Anda diizinkan untuk mendonorkan darah")
    else:
        print("Anda belum memenuhi syarat")


if __name__ == "__main__":
    donor_darah()
    tahun_kabisat()
