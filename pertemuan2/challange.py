#variable allNumber
allNumber = [] #type List

# Buatlah perulangan dengan menggunakan range(1 ~ 100)
for index in range(1, 101):
	# Buatlah kondisi dimana jika index % 2 == 0 : Bilangan Genap: 2, 4, 6, 8, dst
	if index % 2 == 0:
			# Tambahkan nilai index ke list allNumber dengan fungsi append
			allNumber.append(index)

# Tampilkan value/nilai di dalam variable allNumber
print(allNumber)