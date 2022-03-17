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
#modulus % ambil sisa dari hasil bagi contoh:
print(7%4) #3
















