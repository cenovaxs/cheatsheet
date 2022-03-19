# Huruf (STRING)

#type()
message = 'string'
print(type(message))

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

#List and Tuples
matpel = ['sejarah','mat', 'fis','agama']
print(len(matpel)) #melihat jumlah item dalam list
print(matpel[0]) #melihat hanya isi item pertama
print(matpel[-1]) #melihat hanya isi item terakhir
print(matpel[0:2]) #melihat isi pertama sampai kedua
print(matpel[:2]) #sama kyk diatas
print(matpel[2:]) #melihat isi ketiga sampai akhir
print(matpel[::-1]) #melihat isi reverse
print(matpel[-1:0:-1]) #dari belakang ke nomor 2

#append tambah dibelakang
matpel.append('seni') 
print(matpel)
#tambah di posisi awal, bisa juga diatur posisi sesuai dengan keinginan
matpel.insert(0,'seni')

matpel2=['seni', 'olahraga'] #apabila mau menggabungkan list tidak bisa menggunakan append
matpel.append(matpel2) #karena akan menambahkan list di dalam list
print(matpel)

#extend menggabungkan dua list
matpel = ['sejarah','mat', 'fis','agama'] #gunakan extend untuk menggabungkan dua list
matpel.extend(matpel2)
print(matpel)

#membuang list
matpel.remove(matpel[0])
print(matpel)
#atau
matpel.remove('mat')
print(matpel)
#pop membuang yang paling belakang dan return value
popped = matpel.pop()
popped2 = matpel.pop()
print(matpel)
print(popped) #olahraga
print(popped2) #seni

#reverse sebutkan isi list dari belakang
matpel = ['sejarah','mat', 'fis','agama', 'bahasa']
matpel.reverse()
print(matpel)

#sort atur sesuai aplhabetical
matpel.sort()
print(matpel)
#bisa juga digunakan untuk mengurutkan angka dari kecil ke besar
listangka = [6,24,52,100,2,5,20,80] 
listangka.sort()
print(listangka)
#kalau mau terbalik bisa dengan:
listangka.sort(reverse=True)
print(listangka)

#sorted kyk sort tapi return value, ini kepakai kalau ga mau ganti originalnya
sorted_matpel = sorted(matpel)
print(sorted_matpel)

#min value minimum yang paling rendah
print(min(matpel))
#max value paling tinggi
print(max(matpel))
#sum jumlah
print(sum(listangka))

#index cari urutan 
print(matpel.index('fis')) #2 karena fis ada diurutan ke tiga

#cek apakah ada di dalam list
print('fis' in matpel) #True

#enumerate
for ea in enumerate(matpel):
    print(ea) #hasil masih dalam bentuk list
#yang rapih
for no, ea in enumerate(matpel):
    print(no, ea)
#kalau mau mulai dari 1 bukan 0
for no, ea in enumerate(matpel, start=1):
    print(no, ea)

#join jadi satu string
matpel_join = ' - '.join(matpel) #bisa pake koma, atau apapun kalau mau yang lain tinggal ganti aja
print(matpel_join)
#split ubah string jadi list
matpel3 = matpel_join.split(" - ")
print(matpel3)

#tuple () kyk list tapi immutable gabs diganti

#set {} kyk list tapi gak ada order (unordered list) dan gak bisa doble ini cocok buat ngeeliminasi yang doble2

# list() convert menjadi list 
atuple =(1,2,3,4,5)
alist = list(atuple)
print(type(alist)) #jadi list
# set() convert menjadi set
aset = set(atuple)
print(type(aset))
# tuple() convert menjadi tuple
btuble = tuple(aset)
print(type(btuble))

#union ini khusus untuk set aja mengabungkan 2 set
seta = set(matpel)
print(seta)
setb = {'agama', 'sejarah','mat','geo','bio'}
print(setb)
print(seta.union(matpel2))

#intersection mengambil hanya yang sama dalam 2 set
print(seta.intersection(setb))

#difference mengambil hanya yang berbeda dalam 2 set
print(seta.difference(setb))



