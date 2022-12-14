day = input("Masukkan nama hari: ")

match day:
    case "Senin":
        print("Bekerjaa....")
    case "Selasa":
        print("Turu....")
    case "Rabu":
        print("Liburan....")
    case _: # False | Salah
        print("Inputan yang kamu masukkan salah")
