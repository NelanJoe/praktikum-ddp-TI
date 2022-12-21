# Panggil modul / paket matematika
from Matematika import * #:=> import semua function yang ada di modul matematika
# import matematika
from datetime import *


today = date.today()
print(f"Tanggal hari ini {today.month} / {today.year}")

print("Waktu hari ini", datetime.now())

pertambahan(10, 5)
pengurangan(10, 5)
perkalian(10, 5)
pembagian(100, 2)