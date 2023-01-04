'''
    * Import module mysql connector
    * aliaskan menjadi database
'''
import mysql.connector as database

'''
    * Configurasi database
    * - Host : "localhost" / "127.0.0.1"
    * - user : "root" 
    * - pw : "" 
'''
db = database.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="",
    database="dbpython"
)

if db.is_connected():
    print("Berhasil connect ke database")

'''
    * Variable cursor
'''
cursor = db.cursor()
'''
    * Query SQL untuk mendapatkan data dari tabel mahasiswa
'''
querySql = "SELECT * FROM mahasiswa"

'''
    * Menjalankan query SQL
'''
cursor.execute(querySql)

'''
    * Panggil fungsi fetchall :=> Mendapatkan semua data yang ada di tabel mahasiswa
'''
students = cursor.fetchall()

'''
    * looping sederhana dari variable students
'''
for student in students:
    print(student)