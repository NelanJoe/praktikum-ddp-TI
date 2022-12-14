'''
    * If
    * If <kondisi>: dimana kondisi adalah sebuah ekspresi boolean yang menghasilkan nilai True atau False
    * Jika kondisi bernilai True, maka blok kode di dalam if akan dijalankan
    * Jika kondisi bernilai False, maka blok kode di dalam if tidak akan dijalankan
'''

nama = input("Masukkan nama kamu: ")
umur = int(input("Masukkan umur kamu: ")) #:=> Parsing dari String ke Int

if (umur >= 20): # => Benar | True
    print("Boleh masuk ke bioskop")
else: # => False | Salah
    print("Gak boleh masuk")