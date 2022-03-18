# Huruf (STRING)

# Quote
# contoh dibawah '' yang salah
# message = 'Bobby's World'

# gunakan \ untuk mengubah command menjadi string
message = 'Bobby\'s World'
print(message)

# cara lain menggunakan """
message = """Booby"s world"""
print(message)

# len menghitung character dalam string
print(len(message))

# [] mengambil character ke dalam string
print(message[0])

# mengambil dari huruf pertama sampai kelima
print(message[0:5])
# atau
print(message[:5])

# mengambil dari huruf keenam sampai akhir
print(message[5:])

# mengubah jadi huruf kecil semua
print(message.lower())

# mengubah jadi huruf kapital semua
print(message.upper())

# menghitung jumlah huruf berapa kali ada di dalam kata
print(message.count('o'))

# cari kata di dalamnya kalau ada tunjukkan dimana lokasinya kalau ga ada -1
print(message.find('world'))

# ganti kata sebagian dari variabel
message = message.replace('world', 'universe')
print(message)

# concatenate
# cara 1
awal = "This is"
akhir = awal + " " + message
print(akhir)
# cara 2
akhir = '{} {}'.format(awal, message)
print(akhir)
# cara 3 f string untuk python 3.6 keatas
akhir = f'{awal} {message}'
print(akhir)
# kelebihan f string bisa mengunakan method dan function
akhir = f'{awal} {message.upper()}'
print(akhir)
# contoh tambah langsung di dalam f string
tambah = f'seratus tambah seribu sama dengan {100+1000}'
print(tambah)
# contoh lain n:02 berarti dua digit
for n in range(1, 11):
    sentence = f'Hitung {n:02}'
    print(sentence)
# contoh lain {:.4f} berarti 3 digit setelah coma dengan pembulatan dan f yang berarti floating
hasil = 9.87654321
sentence = f'hasil = {hasil:.4}'
print(sentence)
# untuk mengecek method apa saja yang bisa digunakan
#print(dir(message))
# untuk mencari tau apa fungsi dari method tersebut
#print(help(str))

# Angka (Integer dan float)
num=10
print(type(num))
#floor division // ambil hasil bagi pertama contoh:
print(7//2) #3
print(4//2) #2
#modulus % ambil sisa dari hasil bagi, biasanya digunakan untuk cek ganjil genap contoh:
print(7%4) #3 
#pangkat ** 
print(2**4) #2pangkat4 = 16
#*= kali jumlah, bisa juga -= , +=, /=, contoh
num = 20
num /= 4
print(num) # hasilnya 20/4 = 5.0
#abs absolut, menghilangkan minus
print(abs(-30)) #hasilnya 30
print(abs(30))  #hasilnya 30
#round pembulatan
print(round(3.49)) #hasilnya 3
print(round(3.5)) #hasilnya 4
print(round(3.634578, 4)) #dibulatkan sampai 4 angka dibelakang koma
#comparison
print(3==3) #apakah 3 sama dengan 3 
print(3!=3) #apakah 3 tidak sama dengan 3?
print(3>=2) #apakah 3 lebih besar sama dengan 2
print(3<=2) #apakah 3 lebih kecil sama dengan 2
#str(), int(), float() method untuk mengubah menjadi str, int ,float contoh
str1='100'
print(float(str1))












