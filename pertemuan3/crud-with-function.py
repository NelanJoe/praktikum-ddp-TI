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
    * Fungsi Store :=> Untuk menambahkan data
'''

def store(fruitName):
    fruits.append(fruitName)


'''
    * UPDATE
'''

def update(position, fruitName):
    fruits[position] = fruitName


'''
    * DELETE
'''
def destroy(position):
    del fruits[position]


'''
    * READ
'''
def index():
    for fruit in fruits:
        print(fruit)


# Menampikan semua data
print("Menampilkan semua data dalam varaibel list fruits")
index()
print()

# Menambahkan data baru / entri baru
print("Menambahkan data baru")
store("Anggur")
index()

# Challange
# Panggil fungsi Update, Delete

# Mengubah data fruit / entri fruit
print("Mengubah data fruit")
update(1, "Melon")
index()
print()

# Menghapus data fruit / entri fruit
print("menghapus data fruit")
destroy(0)
index()
print()