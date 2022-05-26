# Huruf (STRING)
from multiprocessing import Condition
import module
import module as mm
from module import find as fi
import sys
import random
import math
import datetime
import calendar
import os
from module import find
print("\nHuruf (STRING)\n")

# type() mengecek type variabel
# kalau mau import lebih dari satu bisa pake coma contoh:

message = 'string'
print(type(message))
# Id() mengecek lokasi dalam memory
print(id(message))

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
print("\nconcatenate\n")
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
# print(dir(message))
# untuk mencari tau apa fungsi dari method tersebut
# print(help(str))

# Angka (Integer dan float)
print("\nAngka (integer dan float)\n")
"""
List dibawah adalah prioritas logical python 

()	                                            Parentheses
**	                                            Exponent
+x, -x, ~x	                                    Unary plus, Unary minus, Bitwise NOT
*, /, //, %	                                    Multiplication, Division, Floor division, Modulus
+, -	                                        Addition, Subtraction
<<, >>	                                        Bitwise shift operators
&	                                            Bitwise AND
^	                                            Bitwise XOR
|	                                            Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators
not	                                            Logical NOT
and	                                            Logical AND
or	                                            Logical OR
"""

num = 10
print(type(num))
# floor division // ambil hasil bagi pertama contoh:
print(7//2)  # 3
print(4//2)  # 2
# modulus % ambil sisa dari hasil bagi, biasanya digunakan untuk cek ganjil genap contoh:
print(7 % 4)  # 3
# pangkat **
print(2**4)  # 2pangkat4 = 16
# *= kali jumlah, bisa juga -= , +=, /=, contoh
num = 20
num /= 4
print(num)  # hasilnya 20/4 = 5.0
# abs absolut, menghilangkan minus
print(abs(-30))  # hasilnya 30
print(abs(30))  # hasilnya 30
# round pembulatan
print(round(3.49))  # hasilnya 3
print(round(3.5))  # hasilnya 4
print(round(3.634578, 4))  # dibulatkan sampai 4 angka dibelakang koma
# comparison
print(3 == 3)  # apakah 3 sama dengan 3
print(3 != 3)  # apakah 3 tidak sama dengan 3?
print(3 >= 2)  # apakah 3 lebih besar sama dengan 2
print(3 <= 2)  # apakah 3 lebih kecil sama dengan 2
# str(), int(), float() method untuk mengubah menjadi str, int ,float contoh
str1 = '100'
print(float(str1))

#List and Tuples
print("\nList and Tuples\n")
matpel = ['sejarah', 'mat', 'fis', 'agama']
print(len(matpel))  # melihat jumlah item dalam list
#List Slicing
print("\nList Slicing\n")

# rumusnya list[star:stop:step]
print(matpel[1:5])
# bisa juga negatif
print(matpel[-5:-1])
print(matpel[0])  # melihat hanya isi item pertama
print(matpel[-1])  # melihat hanya isi item terakhir
print(matpel[0:2])  # melihat isi pertama sampai kedua
print(matpel[:2])  # sama kyk diatas
print(matpel[2:])  # melihat isi ketiga sampai akhir
print(matpel[::-1])  # melihat isi reverse
print(matpel[-1:0:-1])  # mulai dari belakang ke nomor 2
print(matpel[-1::-2])  # mulai dari belakang skip satu
print(matpel[::-1]) # reverse list

# bisa juga slice String
print("\nString Slicing\n")
string_slicing = "Lorem Ipsum"
print(string_slicing[6:]) # hasilnya Ipsum 

# append tambah dibelakang
print("\nappend\n")
matpel.append('seni')
print(matpel)
# tambah di posisi awal, bisa juga diatur posisi sesuai dengan keinginan
matpel.insert(0, 'seni')

# apabila mau menggabungkan list tidak bisa menggunakan append
matpel2 = ['seni', 'olahraga']
matpel.append(matpel2)  # karena akan menambahkan list di dalam list
print(matpel)

# extend menggabungkan dua list
# gunakan extend untuk menggabungkan dua list
print("\nextend\n")
matpel = ['sejarah', 'mat', 'fis', 'agama']
matpel.extend(matpel2)
print(matpel)

# membuang list
print("\nremove\n")
matpel.remove(matpel[0])
print(matpel)
# atau
matpel.remove('mat')
print(matpel)
# pop membuang yang paling belakang dan return value
popped = matpel.pop()
popped2 = matpel.pop()
print(matpel)
print(popped)  # olahraga
print(popped2)  # seni

# reverse sebutkan isi list dari belakang
print("\nreverse\n")
matpel = ['sejarah', 'mat', 'fis', 'agama', 'bahasa']
matpel.reverse()
print(matpel)

# sort atur sesuai aplhabetical
print("\nsort\n")
matpel.sort()
print(matpel)
# bisa juga digunakan untuk mengurutkan angka dari kecil ke besar
listangka = [6, 24, 52, 100, 2, 5, 20, 80]
listangka.sort()
print(listangka)
# kalau mau terbalik bisa dengan:
listangka.sort(reverse=True)
print(listangka)

# sorted kyk sort tapi return value, ini kepakai kalau ga mau ganti originalnya
sorted_matpel = sorted(matpel)
print(sorted_matpel)

# min value minimum yang paling rendah
print(min(matpel))
# max value paling tinggi
print(max(matpel))
# sum jumlah
print(sum(listangka))

# index cari no urutan
print(matpel.index('fis'))  # 2 karena fis ada diurutan ke tiga

# cek apakah ada di dalam list
print('fis' in matpel)  # True

# enumerate
print('\nenumerate/kasih nomor\n')

for ea in enumerate(matpel):
    print(ea)  # hasil masih dalam bentuk list
# yang rapih
for no, ea in enumerate(matpel):
    print(no, ea)
# kalau mau mulai dari 1 bukan 0
for no, ea in enumerate(matpel, start=1):
    print(no, ea)

# join jadi satu string
print("\njoin\n")
# bisa pake koma, atau apapun kalau mau yang lain tinggal ganti aja
matpel_join = ' - '.join(matpel)
print(matpel_join)
# split ubah string jadi list
matpel3 = matpel_join.split(" - ")
print(matpel3)

# tuple () kyk list tapi immutable gabs diganti

# set {} kyk list tapi gak ada order (unordered list) dan gak bisa doble ini cocok buat ngeeliminasi yang doble2

# list() convert menjadi list
print("\nconvert\n")
atuple = (1, 2, 3, 4, 5)
alist = list(atuple)
print(type(alist))  # jadi list
# set() convert menjadi set
aset = set(atuple)
print(type(aset))
# tuple() convert menjadi tuple
btuble = tuple(aset)
print(type(btuble))

# union ini khusus untuk set aja mengabungkan 2 set
seta = set(matpel)
print(seta)
setb = {'agama', 'sejarah', 'mat', 'geo', 'bio'}
print(setb)
print(seta.union(matpel2))

# intersection mengambil hanya yang sama dalam 2 set
print(seta.intersection(setb))

# difference mengambil hanya yang berbeda dalam 2 set
print(seta.difference(setb))

# Dictionary kyk list tapi satu unitnya terdiri dari key dan value
print('\nDictionary\n')
murid = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# mengambil dari dictionary
# tapi ini tidak disarankan karena kalau ga ada maka bakal error
print(murid['name'])
# cara yang disarankan dalam mengambil dict:
print(murid.get('name'))  # kalau ini misalny ga ada maka akan none
print(murid.get('asfn o3wh1'))
# kalau ga mau none bisa diganti dengan yang lain
print(murid.get('asfn o3wh1', 'Not Found'))
# cara mengupdate dict, kalau sudah ada key di dalamnya maka isinya akan diganti dengan yang baru
murid['phone'] = '089111555'
print(murid)
# atau .update cara lain mengupdate
murid.update({'name': "Jane", 'phone': '750384', 'school': 'OL'})
print(murid)
#del hapus
del murid['school']
print(murid)
# pop hapus dan return value
phone = murid.pop('phone')
print(murid)
print(phone)
# len untuk liat berapa key
print(len(murid))
# key untuk kasih liat key
print(murid.keys())
# values untuk kasih liat values
print(murid.values())
# items untuk kasih liat semuanya
print(murid.items())
# dictionary loop
for key in murid:
    print(key)  # metode ini cuma akan menampilkan key
# kalau mau menampilkan key dan values maka:
for key, value in murid.items():
    print(key, value)
# if kalau True maka lanjut kalau False maka stop
print('\nConditionals and Booleans\n')
if True:
    print('if')
# is membandingkan apakah berada dalam satu memori yang sama
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))  # a is not b karena
# else
if False:
    print('if')
else:
    print('else')
# elif
if False:
    print('if')
elif True:
    print('elif')
else:
    print('else')

# and or
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Welcome Admin')
else:
    print('Bad Creds')
# not
if not logged_in:
    print('please login')
else:
    print("login successful")

# apa saja yang termasuk false:
# False
# None
# 0
# empty sequence contohnya "", '', [], {}, ()

condition = -10
if condition:
    print('true')
else:
    print('false')

# loop
print('Loop')
# break

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('found')
        break
    print(num)  # loop akan berhenti dan num = 3 tidak diprint

# continue

for num in nums:
    if num == 3:
        print('found')
        continue
    print(num)  # angka 3 tidak di print dan loop tetap sampai akhir

#loop in loop
for num in nums:
    for letter in 'abc':
        # ini akan menghasilkan 1a, 1b, 1c, 2a, 2b, dst sampai 5c
        print(num, letter)

# range loop sebanyak x kali
for i in range(10):
    print(i)  # ini akan ngeloop sampai 10 kali dari 0-9

# while kalau pakai while bisa infinite loop
x = 0
while x < 10:
    print(x)
    x += 1  # ini akan ngeloop sampai 10 kali dari 0-9

# atau

x = 0
while True:
    if x == 10:
        break
    print(x)
    x += 1

# function
print("\nfunction\n")


def hello_func():
    pass  # pass ini menghindari error akibat function yang kosong


print(hello_func)  # ini hanya memperlihatkan nama func dan lokasi di memory
print(hello_func())  # ini akan menjalankan funtion


def hello_func():
    print("Hello")


hello_func()

# Return
# kalau di excecute function akan sama dengan value return


def hello_func():
    return 'return success!'


print(hello_func())
# upper bisa di chain bisa dilakukan karena return dari hello func adalah str
print(hello_func().upper())

# argument variabel , maksudnya bisa kyk x = apapun, jadi bisa digonta ganti variabelnya
print('\narg and kwarg\n')


def hello_func(arg):
    return f'{arg} Function berhasil'


print(hello_func('test'))

# multiple argumen variabel


def hello_func(arg, nama='kamu'):  # nama sebagai default value
    return f'{arg} {nama} Function berhasil'


print(hello_func('hallo'))
print(hello_func('halo', nama='saya'))  # default value bisa diganti

# args kwargs


def student_info(*args, **kwargs):
    print(args)  # args dalam hal ini adalah tuple
    print(kwargs)  # kwargs dalam hal ini adalah dictionary


student_info('math', 'art', age=20, name='john')

# versi yang lebih rapih
print('\nversi yang lebih rapih\n')


def student_info(*args, **kwargs):
    print(args)  # args dalam hal ini adalah tuple
    print(kwargs)  # kwargs dalam hal ini adalah dictionary


courses = ['math', 'art']
info = {'name': 'john', 'age': 20}

student_info(info, courses)
# ini gak bisa info duluan harus args dulu baru kwargs
student_info(*courses, **info)  # pakai * untuk hasilnya terpisah beda line

# module import

print("\nmodule\n")

print(matpel)
print(module.find(matpel, "sejarah"))

# as

print(mm.find(matpel, "sejarah"))

# from

#from module import find, test
print(find(matpel, 'sejarah'))

# from as

print(find(matpel, 'sejarah'))

# sys
print(sys.path)  # untuk mengecek module dari mana saja
# setting path
"sys.path.append('/home/pujas')"
# diatas contoh setting path
# Carakedua tulis di .profile (ubuntu) :
# export Pythonpath="/home/pujas"
# (windows) system properties > env variables > new > variable name : PYTHONPATH variable value: C:\Users\pujas

# stdlib yang berguna

# random
print("\nrandom\n")

print(random.choice(matpel))  # memilih random dari list

# math

print(math.radians(90))

# tanggal

print(datetime.date.today())
print(calendar.isleap(2220))

# OS
print(os.getcwd())  # print working directory
print(os.__file__)  # cek lokasi os.py

"""pip program installer python

$ pip help

$ pip list
untuk lihat aplikasi yang sudah diinstall

$ pip search <package name>
untuk cari paket di repo

$ pip uninstall <package name>

$ pip list -o
untuk lihat apakah ada update 

$ pip install -U <package name>
update

$ pip freeze
simpan list paket yang digunakan

$ pip freeze > <list.txt>
jadiin ke text untuk linux

$ pip install -r <list.txt>
untuk install aplikasi dari list
"""

# local, Enclossing, Global, Built-in

x = 'global x'


def test():
    global x  # membuat var local dipakai global
    print(x)


test()
print(x)


def outer():
    y = "outer y"

    def inner():
        nonlocal y  # membuat var dipakai non local
        y = 'inner y'
        print(y)

    inner()
    print(y)


outer()

# list comprehension
print("\nList Comprehension\n")
# coding standart :
nums = [0,1,2,3,4,5,6]

hasil = []
for n in nums:
    hasil.append(n**2)
print(hasil)

# kalau dengan list comprehension persamaannya:

hasil2 = [x**2 for x in nums]
print(hasil2)

# contoh lainnya menggunakan if:
# coding biasa:
hasil3 = []
for n in nums:
    if n%2==0:
        hasil3.append(n)
print(hasil3)
# List comprehension:
hasil3 = [n for n in nums if n%2==0]
print(hasil3)

# loop in loop
# standart
hasil4 = []
for huruf in 'abcd':
    for angka in range(4):
        hasil4.append([huruf,angka])
print(hasil4)
# LC
hasil4 = [[huruf,angka] for huruf in 'abcd' for angka in range(4)]
print(hasil4)
