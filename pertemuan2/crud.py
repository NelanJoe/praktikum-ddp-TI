'''
    * CRUD 
        - Create : Buat entri / nilai baru 
        - Read   : Membaca entri / nilai  
        - Update : Memperbaharui entri / nilai  
        - Delete : Menghapus entri / nilai  
'''

# Variabel fruits / buah - buahan
fruits = ["Mangga", "Apel"]


'''
    * CREATE
'''

fruits.append("Anggur")
fruits.append("Cempedak")


'''
    * UPDATE
'''

fruits[0] = "Pisang"


'''
    * DELETE
'''

del fruits[1]


'''
    * READ
'''
print(fruits)