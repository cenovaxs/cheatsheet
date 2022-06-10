# Huruf (STRING)
import re
import pytz
import time
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

t1 = time.time()

print("\nHuruf (STRING)\n")

# type() mengecek type variabel
# kalau mau import lebih dari satu bisa pake coma contoh:

message = 'string'
print(type(message))  # <class 'str'>
# mengecek class menggunakan is instance, bisa juga mengecek class buatan di OOP
# isinstance
print(isinstance(message, str)) # True

# hassattr
class Person:
    name = "John"
    age = 36
    country = "Norway"

x = hasattr(Person, 'age') # apakah ada attribute age dalam class person
print(x)  # True

# callable

def x():
    a = 5
    
print(callable(x)) # True

a = 5
print(callable(a)) # False karena a itu tidak callable

# untuk melihat lokasi python yang digunakan :
""" 
import sys
sys.version
sys.executable
"""
print('\nsys version')
print(sys.version)  
print('\nsys executable')
print(sys.executable)

print(r'\nspasi\n')  # r membuat ignore special case sehingga \n tetap ter print
# Id() mengecek lokasi dalam memory
print(id(message))  # 3229004571568

# untuk mengecek method apa saja yang bisa digunakan
print(dir(message))  # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# untuk mencari tau apa fungsi dari perintah tersebut :

# print(help(print))  # hasilnya panjang lihat aja di terminal

# Quote
# contoh dibawah '' yang salah
# message = 'Bobby's World'

# gunakan \ untuk mengubah command menjadi string
message = 'Bobby\'s World'
print(message)  # Bobby's World

# cara lain menggunakan """
message = """Booby"s world"""
print(message)  # Booby"s world

# len menghitung character dalam string
print(len(message))  # 13

# [] mengambil character ke dalam string
print(message[0])  # B

# mengambil dari huruf pertama sampai kelima
print(message[0:5])  # Booby
# atau
print(message[:5])  # Booby

# mengambil dari huruf keenam sampai akhir
print(message[5:])  # "s world

# mengubah jadi huruf kecil semua
print(message.lower())  # booby"s world

# mengubah jadi huruf kapital semua
print(message.upper())  # BOOBY"S WORLD

# menghitung jumlah huruf berapa kali ada di dalam kata
print(message.count('o'))  # 3

# cari kata di dalamnya kalau ada tunjukkan dimana lokasinya kalau ga ada -1
print(message.find('world'))  # 8

# Strip hilangin huruf atau space kosong setelah dan sebelum kata
print(message.strip())

# ganti kata sebagian dari variabel
message = message.replace('world', 'universe')
print(message)  # Booby"s universe

# concatenate
print("\nconcatenate and formating\n")
# cara 1
awal = "This is"
akhir = awal + " " + message
print(akhir)  # This is Booby"s universe
# cara 2
akhir = '{} {}'.format(awal, message)
print(akhir)  # This is Booby"s universe
# cara 2.1 ditandain supaya bisa diatur kata pertama yang mana
akhir = '{1} {0}'.format(awal, message)
print(akhir)  # Booby"s universe This is
# kalau dalam list bisa :
person = ['pujas', 'putri']
akhir = '{0[0]} {0[1]}'.format(person)  # jadi person sekali aja gak masalah
print(akhir)  # pujas putri
# cara 2.2
akhir = '{name} {age}'.format(name='Pujas', age='34')
print(akhir)  # Pujas 34
# cara 2.3 pakai kwargs
person = {'name': 'Pujas', 'age': 31}
akhir = 'My Name is {name} and my age is {age}'.format(**person)
# cara 3 f string untuk python 3.6 keatas
akhir = f'{awal} {message}'
print(akhir)  # This is Booby"s universe
# kelebihan f string bisa mengunakan method dan function
akhir = f'{awal} {message.upper()}'
print(akhir)  # This is BOOBY"S UNIVERSE
# contoh tambah langsung di dalam f string
tambah = f'seratus tambah seribu sama dengan {100+1000}'
print(tambah)  # seratus tambah seribu sama dengan 1100
# contoh lain n:02 berarti dua digit

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
# print format set digit

print('\nNumber Format\n')
print('\nSet digit\n')
# nambahin angka total berapa digit termasuk koma dan titik
num1 = '{:05}'.format(num)
print(num1)  # hasilnya 005.0
num2 = '{:.3f}'.format(num)  # nambahin angka dibelakang koma (pembulatan)
print(num2)  # hasilnya 5.000

for n in range(1, 11):
    # print 2 digit kalau ada koma termasuk di dalamnya
    sentence = f'Hitung {n:02}'
    print(sentence)
# contoh lain {:.4f} berarti 4 digit setelah coma dengan pembulatan dan f yang berarti floating
hasil = 9.87654321
sentence = f'hasil = {hasil:.4}'  # berarti 3 digit setelah koma
print(sentence)  # hasil = 9.877

num3 = '{:,}'.format(1000**2)  # kasih koma setiap 3 angka
print(num3)  # 1,000,000

# bisa juga dikombinasi koma dan titik
num4 = '{:,.2f}'.format(1000**2)
print(num4)  # 1,000,000.00

#List and Tuples
print("\nList and Tuples\n")
matpel = ['sejarah', 'mat', 'fis', 'agama']
# melihat jumlah item dalam list
print(len(matpel))  # 4
# List Slicing
print("\nList Slicing\n")

# rumusnya list[star:stop:step]
print(matpel[1:5])  # ['mat', 'fis', 'agama']
# bisa juga negatif
print(matpel[-5:-1])  # ['sejarah', 'mat', 'fis']
print(matpel[0])  # melihat hanya isi item pertama
print(matpel[-1])  # melihat hanya isi item terakhir
print(matpel[0:2])  # melihat isi pertama sampai kedua
print(matpel[:2])  # sama kyk diatas
print(matpel[2:])  # melihat isi ketiga sampai akhir
print(matpel[::-1])  # melihat isi reverse
print(matpel[-1:0:-1])  # mulai dari belakang ke nomor 2
print(matpel[-1::-2])  # mulai dari belakang skip satu
print(matpel[::-1])  # reverse list

# bisa juga slice String
print("\nString Slicing\n")
string_slicing = "Lorem Ipsum"
print(string_slicing[6:])  # hasilnya Ipsum

# append tambah dibelakang
print("\nappend\n")
matpel.append('seni')
print(matpel)  # hasilnya ['sejarah', 'mat', 'fis', 'agama', 'seni']
# tambah di posisi awal, bisa juga diatur posisi sesuai dengan keinginan
matpel.insert(0, 'seni')

# apabila mau menggabungkan list tidak bisa menggunakan append
matpel2 = ['seni', 'olahraga']
matpel.append(matpel2)  # karena akan menambahkan list di dalam list
# ['seni', 'sejarah', 'mat', 'fis', 'agama', 'seni', ['seni', 'olahraga']]
print(matpel)

# extend menggabungkan dua list
# gunakan extend untuk menggabungkan dua list
print("\nextend\n")
matpel = ['sejarah', 'mat', 'fis', 'agama']
matpel.extend(matpel2)
print(matpel)  # ['sejarah', 'mat', 'fis', 'agama', 'seni', 'olahraga']

# membuang list
print("\nremove\n")
matpel.remove(matpel[0])
print(matpel)  # ['mat', 'fis', 'agama', 'seni', 'olahraga']
# atau
matpel.remove('mat')
print(matpel)  # ['fis', 'agama', 'seni', 'olahraga']
# pop membuang yang paling belakang dan return value
popped = matpel.pop()
popped2 = matpel.pop()
print(matpel)  # ['fis', 'agama']
print(popped)  # olahraga
print(popped2)  # seni

# reverse sebutkan isi list dari belakang
print("\nreverse\n")
matpel = ['sejarah', 'mat', 'fis', 'agama', 'bahasa']
matpel.reverse()
print(matpel)  # ['bahasa', 'agama', 'fis', 'mat', 'sejarah']

# sort atur sesuai aplhabetical
# .sort() hanya berlaku untuk list tidak bisa untuk tuple dan dict
print("\nsort\n")
matpel.sort()
print(matpel)  # ['agama', 'bahasa', 'fis', 'mat', 'sejarah']
# bisa juga digunakan untuk mengurutkan angka dari kecil ke besar
listangka = [6, -24, 52, 100, 2, 5, 20, 80]
listangka.sort()
print(listangka)  # [-24, 2, 5, 6, 20, 52, 80, 100]
# kalau mau terbalik bisa dengan reverse dan kalau mau abaikan minus bisa dengan abs:
listangka.sort(reverse=True, key=abs)
print(listangka)  # [100, 80, 52, -24, 20, 6, 5, 2]

# sorted kyk sort tapi return value, ini kepakai kalau ga mau ganti originalnya
sorted_matpel = sorted(matpel)
print(sorted_matpel)  # ['agama', 'bahasa', 'fis', 'mat', 'sejarah']

# bisa reverse abaikan minus juga
listangka2 = [6, -24, 52, 100, 2, 5, 20, 80]
sorted_listangka = sorted(listangka2, reverse=True, key=abs)
print(sorted_listangka)  # [100, 80, 52, -24, 20, 6, 5, 2]

# kalau dipakai buat dictionary yang di sort default adalah keynya
di = {'name': 'Corey', 'job': 'programming', 'age': 34, "os": 'Ubuntu'}
s_di = sorted(di)
print('Dict\t', s_di)  # Dict     ['age', 'job', 'name', 'os']


# min value minimum yang paling rendah
print(min(matpel))  # agama
# max value paling tinggi
print(max(matpel))  # sejarah
# sum jumlah
print(sum(listangka))  # 241

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
print(matpel_join)  # agama - bahasa - fis - mat - sejarah
# split ubah string jadi list
matpel3 = matpel_join.split(" - ")
print(matpel3)  # ['agama', 'bahasa', 'fis', 'mat', 'sejarah']

# tuple () kyk list tapi immutable gabs diganti

# set {} kyk list tapi gak ada order (unordered list) dan gak bisa doble ini cocok buat ngeeliminasi yang doble2

# list() convert menjadi list
print("\nconvert\n")
atuple = (1, 2, 3, 4, 5)
alist = list(atuple)  # convert tuple jadi list
print(type(alist))  # <class 'list'>
# set() convert menjadi set
aset = set(atuple)
print(type(aset))  # <class 'set'>
# tuple() convert menjadi tuple
btuble = tuple(aset)
print(type(btuble))  # <class 'tuple'>

# union ini khusus untuk set aja mengabungkan 2 set
seta = set(matpel)
print(seta)  # {'fis', 'bahasa', 'agama', 'sejarah', 'mat'}
setb = {'agama', 'sejarah', 'mat', 'geo', 'bio'}
print(setb)  # {'agama', 'sejarah', 'mat', 'geo', 'bio'}
# {'fis', 'seni', 'agama', 'sejarah', 'mat', 'olahraga', 'bahasa'}
print(seta.union(matpel2))

# intersection mengambil hanya yang sama dalam 2 set
print(seta.intersection(setb))  # {'agama', 'sejarah', 'mat'}

# difference mengambil hanya yang berbeda dalam 2 set
print(seta.difference(setb))  # {'fis', 'bahasa'}

# Dictionary kyk list tapi satu unitnya terdiri dari key dan value
print('\nDictionary\n')
murid = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# mengambil dari dictionary
# tapi ini tidak disarankan karena kalau ga ada maka bakal error
print(murid['name'])  # John
# cara yang disarankan dalam mengambil dict:
print(murid.get('name'))  # John tapi kalau ini misalny ga ada maka akan none
print(murid.get('asfn o3wh1'))  # None
# kalau ga mau none bisa diganti dengan yang lain
print(murid.get('asfn o3wh1', 'Not Found'))  # Not Found
# cara mengupdate dict, kalau sudah ada key di dalamnya maka isinya akan diganti dengan yang baru
murid['phone'] = '089111555'
# {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '089111555'}
print(murid)
# atau .update cara lain mengupdate
murid.update({'name': "Jane", 'phone': '750384', 'school': 'OL'})
# {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '750384', 'school': 'OL'}
print(murid)
#del hapus
del murid['school']
# {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '750384'}
print(murid)
# pop hapus dan return value
phone = murid.pop('phone')
print(murid)  # {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci']}
print(phone)  # 750384
# len untuk liat berapa key
print(len(murid))  # 3
# key untuk kasih liat key
print(murid.keys())  # dict_keys(['name', 'age', 'courses'])
# values untuk kasih liat values
print(murid.values())  # dict_values(['Jane', 25, ['Math', 'CompSci']])
# items untuk kasih liat semuanya
# dict_items([('name', 'Jane'), ('age', 25), ('courses', ['Math', 'CompSci'])])
print(murid.items())
# dictionary loop
for key in murid:
    print(key)  # metode ini cuma akan menampilkan key
# kalau mau menampilkan key dan values maka:
for key, value in murid.items():
    print(key, value)

# generator kyk list tapi menunggu untuk di eksekusi, ini bisa simpan memory
print("\nGenerator\n")


def kuadrat(q2):
    for i in q2:
        yield (i*i)


hasil_gen = kuadrat([1, 2, 3, 4])

# generator gak bisa di print kayak list dia harus di iterate satu persatu
print(hasil_gen)  # <generator object kuadrat at 0x0000013DEE39D900>

# cara panggil
# 1 lewat next(). Next akan panggil satu hasil generator berikutnya
print(next(hasil_gen))  # 1
print(next(hasil_gen))  # 4
print(next(hasil_gen))  # 9
print(next(hasil_gen))  # 16
# print(next(hasil_gen))  # StopIteration  > Kalau diterusin error stop iteration

# 2 lewat iterasi  > tapi kalau generator sudah pernah di next() dia mulai dari berikutnya, jadi kalau ada next harus ikutin
for num in hasil_gen:
    print(num)


# if kalau True maka lanjut kalau False maka stop
print('\nConditionals and Booleans (if else)\n')
if True:
    print('if')  # if
# is membandingkan apakah berada dalam satu memori yang sama
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False
print(id(a))  # 3229014061440
print(id(b))  # 3229016471360
# else
if False:
    print('if')
else:
    print('else')  # else
# elif
if False:
    print('if')
elif True:
    print('elif')  # elif
else:
    print('else')

# and or
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Welcome Admin')  # Welcome Admin
else:
    print('Bad Creds')
# not
if not logged_in:
    print('please login')
else:
    print("login successful")  # login successful

# apa saja yang termasuk false:
# False
# None
# 0
# empty sequence contohnya "", '', [], {}, ()

condition = -10
if condition:
    print('true')  # true
else:
    print('false')

# loop
print('\nLoop\n')
# break
print('\nfor\n')
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

print('\nWhile\n')
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


# dibawah ini hanya memperlihatkan nama func dan lokasi di memory
print(hello_func)  # <function hello_func at 0x000002EFD05F44C0>
# dibawah ini akan menjalankan funtio
print(hello_func())  # None


def hello_func():
    print("Hello")


hello_func()  # Hello

# Return
# kalau di excecute function akan sama dengan value return


def hello_func():
    return 'return success!'


print(hello_func())  # return success!
# upper bisa di chain bisa dilakukan karena return dari hello func adalah str
print(hello_func().upper())  # RETURN SUCCESS!

# argument variabel , maksudnya bisa kyk x = apapun, jadi bisa digonta ganti variabelnya
print('\narg and kwarg\n')


def hello_func(arg):
    return f'{arg} Function berhasil'


print(hello_func('test'))  # test Function berhasil

# multiple argumen variabel


def hello_func(arg, nama='kamu'):  # nama sebagai default value bisa diganti
    return f'{arg} {nama} Function berhasil'


print(hello_func('hallo'))  # hallo kamu Function berhasil
print(hello_func('halo', nama='saya'))  # halo saya Function berhasil

# args kwargs


def student_info(*args, **kwargs):
    # args dalam hal ini adalah tuple
    print(args)
    # kwargs dalam hal ini adalah dictionary
    print(kwargs)


student_info('math', 'art', age=20, name='john')
# hasilnya:
# ('math', 'art')
# {'age': 20, 'name': 'john'}
# versi yang lebih rapih
print('\nversi yang lebih rapih\n')


def student_info(*args, **kwargs):
    print(args)  # args dalam hal ini adalah tuple
    print(kwargs)  # kwargs dalam hal ini adalah dictionary


courses = ['math', 'art']
info = {'name': 'john', 'age': 20}

# kalau tanpa bintang dibuat maka akan dianggap args kemudian kwargs menjadi dictionary kosong
student_info(info, courses)
# ({'name': 'john', 'age': 20}, ['math', 'art'])   >>semua jadi satu tuple
# {}   >> hasilnya dict kosong

student_info(courses, info)
#(['math', 'art'], {'name': 'john', 'age': 20})
# {}

# pakai * untuk hasilnya terpisah beda line tapi harus tuple dulu baru dict kalau terbalik error
student_info(*courses, **info)
# ('math', 'art')
# {'name': 'john', 'age': 20}


# module import dan std library

print("\nmodule\n")
#import module
# ini bakal nyari module yang ada dalam local folder
print(matpel)  # ['agama', 'bahasa', 'fis', 'mat', 'sejarah']
print(module.find(matpel, "sejarah"))  # 4
# harus dalam format <module>.<function>

# as
#import module as mm
print(mm.find(matpel, "sejarah"))  # 4

# from dipakai supaya pendek jadi langsung function aja
# from module import find
# from module import find, test  = untuk mengimport multiple
# from module import *  = untuk menimport semua function
print(find(matpel, 'sejarah'))  # 4

# from as
#from module import find as fi
print(fi(matpel, 'sejarah'))

# sys
print("\nsys.path\n")
# dibawah ini untuk mengecek module dari mana saja
print(sys.path)  # ['e:\\pujas\\programing\\cheatsheet', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\pujas\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']
# local folder, std lbr, dll

# setting path
# untuk nambah custom path caranya:
"sys.path.append('/home/pujas')"
# diatas contoh setting path
# Carakedua tulis di .profile (ubuntu) :
# export Pythonpath="/home/pujas"
# (windows) system properties > env variables > new > variable name : PYTHONPATH variable value: C:\Users\pujas

# stdlib yang berguna

# random
print("\nrandom\n")

matpel = ['sejarah', 'mat', 'fis', 'agama', 'bahasa']

print(random.random())  # buat random antara 0 - 1 dalam float
print(random.uniform(1, 10))  # random antara 1 - 10 dalam float
print(random.randint(1, 10))  # random antara 1 - 10 integer
print(random.choice(matpel))  # memilih random dari list
print(random.choices(matpel, k=10))  # random dari list sebanyak k kali
# weights mengatur seberapa kali lebih sering dia bakal muncul
print(random.choices(matpel, weights=[5, 20, 10, 1, 3], k=10))
deck = list(range(1, 53))
print(deck)
# kyk kocok kartu ambil random yang ud diambil tidak diambil lagi sampai semua diambil
random.shuffle(deck)
print(deck)
# ambil sebanyak 5 kali, 5 nomor acak dari deck
print(random.sample(deck, k=5))

# math
print('\nMath\n')

print(math.radians(90))  # 1.5707963267948966

# tanggal

print('\nDatetime\n')

print(datetime.datetime.today())    # tanggal hari ini local
# tanggal hari ini default local tp bisa diganti
print(datetime.datetime.now())
print(datetime.datetime.utcnow())   # tanggal hari ini ikut timezone UTC
print(calendar.isleap(2220))  # True

# datetime.date hanya mengakomodasi tahun bulan hari
# datetime.time hanya mengakomodasi jam menit detik microsecond
# datetime.datetime mengakomodasi semuanya

print('\nFormat Datetime\n')
my_date = datetime.datetime(2022, 5, 31, 22, 51, 0)
# Default python format    2022-05-31 22:51:00
print('Default python format\t', my_date)

# ambil hanya tertentu tahun/tanggal/bulan/dll
print(my_date.year)     # 2022
print(my_date.month)    # 5
print(my_date.day)      # 31
print(my_date.hour)     # 22
print(my_date.minute)   # 51
print(my_date.second)   # 0

# weekday cek hari apa?
print(my_date.weekday())  # 1   karena jatuh hari selasa mengikuti aturan :
# senin 0 minggu 6
print(my_date.isoweekday())  # 2
# senin 1 minggu 7

# untuk tambah hari
tdelta = datetime.timedelta(days=7)  # set time delta 7 hari
print(my_date + tdelta)  # 2022-06-07 22:51:00
# bisa juga dikurang
print(my_date - tdelta)  # 2022-05-24 22:51:00

# cari selisih hari
# yang harus diperhatikan keduanya haru sama jenisnya tidak boleh datetime.date dengan datetime.datetime
new_date = datetime.datetime(2022, 6, 1)
print(new_date - my_date)  # 1:09:00
print(my_date - new_date)  # -1 day, 22:51:00
# bisa diubah dalam detik
print((my_date - new_date).total_seconds())  # -4140.0

print('\nCustom Datetime\t')
# untuk format yang lain cari di internet "strftime" atau "strptime"
newDatetime = '{:%B %d %Y}'.format(my_date)
print(newDatetime)  # May 31 2022
# contoh lain lebih complex
complexdate = '{0:%B %d, %Y} jatuh pada hari {0:%A} dan hari ke {0:%j}'.format(
    my_date)  # jangan lupa taruh 0 karena kita menggunakan 3 variabel namun satu argument
print(complexdate)  # May 31, 2022 jatuh pada hari Tuesday dan hari ke 151

print('\nPytz timezone aware datetime\n')
# pytz timezone aware datetime
# pip install pytz
#import pytz

# cara apply :
# 1 datetime.datetime
my_date2 = datetime.datetime(2022, 5, 31, 22, 51, 0, tzinfo=pytz.UTC)
print(my_date2)  # 2022-05-31 22:51:00+00:00
# 2 datetime.datetime.now
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
# 3 datetime.datetime.utcnow
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
# pilih timezone sesuai yang diinginkan
dt_jakarta = dt_now.astimezone(pytz.timezone('Asia/Jakarta'))
print(dt_jakarta)  # 2022-06-01 23:38:41.909889+07:00

# untuk lihat list timezone lainnya dapat dilihat di pytz.all_timezones:
"""
for tz in pytz.all_timezones:
    print(tz)
"""
# cara ubah naive datetime ke timezone aware
naive = datetime.datetime.now()
jkttime = pytz.timezone('Asia/Jakarta')
waktujakarta = jkttime.localize(naive)
print(waktujakarta)  # 2022-06-01 23:51:53.986948+07:00

# format datetime
# iso format
print(waktujakarta.isoformat())  # 2022-06-01T23:57:44.949860+07:00
# custom format strftime
print(waktujakarta.strftime('%B %d, %Y'))  # June 01, 2022

# ubah dari string ke datetime strptime
dt_string = 'June 01, 2022'
dt_convert = datetime.datetime.strptime(dt_string, '%B %d, %Y')
print(dt_convert)  # 2022-06-01 00:00:00

print('\nOS\n')
# OS
# lihat method apa saja yang bisa dilakukan os
print(dir(os))
# print working directory
print(os.getcwd())  # E:\pujas\programing\cheatsheet
# cek lokasi os.py
# C:\Users\pujas\AppData\Local\Programs\Python\Python38\lib\os.py
print(os.__file__)

# pindah folder
# os.chdir('/home/kali/Programming/Cheatsheet') # pindah working directory

# ls menggunakan OS
# kyk ls di bash melihat file dan folder yang ada di working directory
print(os.listdir())

# buat folder ada dua cara :
# os.mkdir('new folder') # ini cuma bikin satu folder
# os.makedirs('newfolder1/newfolder2') # ini untuk bikin folder dengan subfoldernya

# delete folder ada dua cara :
# os.rmdir('new folder') # delete satu folder
# os.removedirs('newfolder1/newfolder2') # delete multiple folder

# os.rename('nama lama', 'nama baru') # ganti nama

# print(os.stat('file')) # liat statistic file
# print(os.stat('file').st_size) # liat ukuradsan file
# print(os.stat('file').st_mttime) # liat waktu modifikasi

# untuk liat human readable time
# modtime = (os.stat('file').st_mttime)
# print(datetime.datetime.fromtimestamp(modtime))
# datetime.datetime bisa disingkat pakai # from datetime import datetime

# tree list (os.walk) digunakan untuk melihat seluruh folder dan subfolder serta file
# os walk akan membuat generator dengan urutan sbb berikut: path, folder, file
# print(list(os.walk('/home/kali/Programming/test folder')))
# cara yang baik untuk mengaksesnya adalah :
"""
for path, dir, file in os.walk('/home/kali/Programming/test folder')
    print('path:', path)
    print('folder:', dir)
    print('file:', file)
    print()
"""

# Environment Variable melihat path
# print(os.environ.get('HOME')) # in buat linux dan mac
# print(os.environ.get('USERPROFILE')) # buat windows

# ambil nama file aja
# print(os.path.basename('~/Programming/test folder/python.py')) # python.py

# ambil nama folder saja
# print(os.path.dirname('~/Programming/test folder/python.py')) # ~/Programming/test folder

# ambil nama folder dan file
# print(os.path.split('~/Programming/test folder/python.py')) # ('~/Programming/test folder', 'python.py')

# check apakah file tersebut ada
# print(os.path.exists('~/Programming/test folder/test.py')) # False
# false karena gak boleh pake ~ dia harus full path
# print(os.path.exists('/home/kali/Programming/test folder/test.py')) # True

# test apakah directory
# print(os.path.isdir('/home/kali/Programming/test folder/test.py')) # False

# test apakah file
# print(os.path.isfile('/home/kali/Programming/test folder/test.py')) # True

# lepas (split) extension
# print(os.path.splitext('/home/kali/Programming/test folder/test.py')) # ('/home/kali/Programming/test folder/test', '.py')

# Nyambung path bisa pakai contatination tp ada mehod yang otomatis
# os.path.join(path1, path2)
# os.path.join(os.environ.get('HOME'), 'test.txt')
# hasil : /home/kali/test.txt

# untuk yang lain bisa dicek disini:
# print(dir(os.path))

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


print("\nScope\n")
# prioritas dalam variabel mengikuti acuan LEGB :
# local, Enclossing, Global, Built-in
x = 'global x'  # contoh variable global
print(x)  # global x


def test0():
    x = 'local x'  # contoh variable local


def test():
    global x  # membuat var local dipakai global
    x = 'local x'  # variabel harus ditaroh setelah command global kalau
    print(x)


test()  # local x
print(x)  # local x


def outer():
    y = "outer y"  # contoh enclosing

    def inner():
        nonlocal y  # membuat var dipakai non local
        y = 'inner y'
        print(y)

    inner()
    print(y)


outer()
# inner y
# inner y

# list comprehension
print("\nList Comprehension\n")
# coding standart :
nums = [0, 1, 2, 3, 4, 5, 6]

hasil = []
for n in nums:
    hasil.append(n**2)
print(hasil)  # [0, 1, 4, 9, 16, 25, 36]

# kalau dengan list comprehension persamaannya:

hasil2 = [x**2 for x in nums]
print(hasil2)  # [0, 1, 4, 9, 16, 25, 36]

# contoh lainnya menggunakan if:
# coding biasa:
hasil3 = []
for n in nums:
    if n % 2 == 0:
        hasil3.append(n)
print(hasil3)  # [0, 2, 4, 6]
# List comprehension:
hasil3 = [n for n in nums if n % 2 == 0]
print(hasil3)  # [0, 2, 4, 6]

# loop in loop
# standart
hasil4 = []
for huruf in 'abcd':
    for angka in range(4):
        hasil4.append([huruf, angka])
print(hasil4)  # [['a', 0], ['a', 1], ['a', 2], ['a', 3], ['b', 0], ['b', 1], ['b', 2], ['b', 3], ['c', 0], ['c', 1], ['c', 2], ['c', 3], ['d', 0], ['d', 1], ['d', 2], ['d', 3]]
# LC
hasil4 = [[huruf, angka] for huruf in 'abcd' for angka in range(4)]
print(hasil4)  # [['a', 0], ['a', 1], ['a', 2], ['a', 3], ['b', 0], ['b', 1], ['b', 2], ['b', 3], ['c', 0], ['c', 1], ['c', 2], ['c', 3], ['d', 0], ['d', 1], ['d', 2], ['d', 3]]

print('\nZip Function\n')

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# zip function = pair two list into one
# {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
print(dict(zip(names, heroes)))

# dictionary comprehension
print("\nDictionary Comprehension\n")
# coding normal
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero

# {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
print(my_dict)
# DC
my_dict2 = {name: hero for name, hero in zip(names, heroes)}
# {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
print(my_dict2)
# misalnya kita mau buang peter
my_dict2 = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
# {'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
print(my_dict2)

# Ini bisa juga untuk SET
print('\nSet Comprehension\n')
# normal coding
nums = [1, 1, 1, 2, 3, 4, 5, 5, 3, 2, 4, 5]
my_set = set(nums)
for n in nums:
    my_set.add(n)
print(my_set)

# Set Comprehension
my_set = {n for n in nums}
print(my_set)


# Generator Expression

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# generator normal :


def gen_func(nums):
    for n in nums:
        yield n*n


my_gen = gen_func(nums)

print(list(my_gen))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# generator comprehension :

my_gen = (n*n for n in nums)

print(list(my_gen))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# File Objects - Reading Writing files
print('\nFile Objects - Reading Writing Files\n')

# Tanpa context manager:
"""
f = open('test.txt', 'r') # Argumen pertama path file, Argumen kedua r untuk read, w untuk write, a untuk append r+w untuk read and write
# contoh path file > f = open('/home/pujas/Programming/cheatsheet/Vi', 'r')
# method .name untuk melihat nama dari file, .mode untuk cek apakah write atau read, .closed untuk ngecek apakah sudah diclose
print(f.name) # test.txt
print(f.mode) # r
print(f.closed) # False
print(f.read()) # Isi dari file txt. Read kalau selesai membaca dia akan ke akhir jadinya tidak bisa baca ulang
print(f.read(100)) # membaca isi 100 character pertama saja
print(len(f.read())) # melihat berapa Character sampai tulisan habis
print(f.tell()) # melihat posisi sudah sampai dimana
f.seek(0) # kembali ke posisi 0 awal
print(f.readlines()) # membuat list yang berisi setiap baris dalam isi file, jadi bisa dipanggil per baris
print(f.readline(), end='') # membaca baris per baris, argumen2 end='' mengatur hasilnya menjadi spasi karena karena default dari end adalah baris baru

f.close() # harus di close biar file gak bocor dan bikin error
"""

# dengan context manager:

""" Cara 1 dengan read method
with open('test.txt', 'r') as f: 
    print(f.read())
"""

""" Cara 2 dengan baca satu persatu
with open('test.txt', 'r') as f: 
    print(f.readline(), end='') # baris pertama
    print(f.readline()) # baris berikutnya
    print(f.readline())
print(f.closed) # True  > karena context manager otomatis close filenya 
"""

# Cara yang lebih rapih dengan for tanpa method read
"""
with open('test.txt', 'r') as f: 
    for line in f:
        print(line, end='')
"""

# Membaca menggunakan While
"""
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
"""

# Menulis Write
"""
with open('test.txt', 'w') as f: # kalau file belum ada maka bakal dibuat file baru
    f.write('Test') # tulis Test ke dalam file
    f.write('lagi') # lanjut tulis lagi setelah Test
"""

# Menambah Append

# with open('test.txt', 'a') as f: # ini akan menambah, file lama tidak akan dihapus
#     f.write('\nTambah') # tulis Test ke dalam file
#     f.write('\nlagi') # lanjut tulis lagi setelah Test

# Copy Text File
"""
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
"""

# Copy non text file harus ubah pakai binary mode
"""
with open('test.jpg', 'rb') as rf:
    with open('test_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
"""

# Copy non text file dengan chunk size
"""
with open('test.jpg', 'rb') as rf:
    with open('test_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        read_chunk = rf.read(chunk_size)
        while len(read_chunk) > 0 :
            wf.write(read_chunk)
            read_chunk = rf.read(chunk_size)
"""

# Time

print(time.sleep(0))  # pause selama 0 detik
# menghitung lama proses
t2 = time.time()  # time menunjukkan detik setelah epoch (1st January 1970)
print(t2-t1)  # di awal code ada t1=time.time() di baris 15, t2-t1 menunjukkan waktu yang diperlukan komputer untuk menjalankan program sampai titik ini

print('\nRegex\n')


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
https://www.youtube.com
http://google.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# cara 1 pakai finditer harus di loop

pattern = re.compile(r'\d{3}\W\d{3}\W\d{3}', re.I)

pattern_finditer = pattern.finditer(text_to_search)

for i in (pattern_finditer):
    print(i)

# untuk regex pada file lain bisa kombinasikan with open
"""
with open('data.txt', 'r', endoding='utf-8') as f:
    contents = f.read()

    pattern_finditer = pattern.finditer(text_to_search)

    for i in (pattern_finditer):
        print(i)
"""

# Group

pattern = re.compile(r'(https)?(://)?(www\.)?(.+)\.[a-zA-Z0-9-.]+')

pattern_finditer = pattern.finditer(text_to_search)

for i in (pattern_finditer):
    print(i.group(0))  # group 0 = print semua
    print(i.group(4))  # group n = print hanya group ke n

# shorcut substition group cari pattern dari existing regex

suba = pattern.sub(r'\3\4', text_to_search)  # pakai ulang regex dari pattern
# print(suba)

# cara 2 pakai search tapi hanya keluar hasil pertama aja

pattern = re.compile(r'start', re.I)  # re.I =re.IGNORECASE

matches = pattern.search(sentence)

print(matches)


# Cara 3 pakai findall # yang keluar bentuknya string kalau ada group maka buat tuple dengan hasilnya per grup

pattern = re.compile(r'\d{3}\W\d{3}\W\d{3}', re.IGNORECASE)

pattern_finditer = pattern.findall(text_to_search)

for i in (pattern_finditer):
    print(i)

# cara 4 pakai match tapi hanya menemukan cara pertama saja jangan dipakai

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)

print('\nTry Except Else Finally\n')

# Try  Except

# program tetap jalan dan bisa membuat pesan custom apabila ada error
try:
    hsl = skg + 3
except Exception:
    print('Variable tidak ada')

# Exception as
try:
    hsl = skg + 3
except Exception as e:
    print(e)  # print default error message dan program tetap lanjut

# Specific exception & Multiple exception Else exception, Finally

try:
    hsl = skg + 3
    print(hsl)  # perintah bisa dijalankan disini atau setelah else
except FileNotFoundError:  # akan mengecek error berurutan mulai dari yang pertama
    print("File tidak ada")
except NameError:  # karena error NameError, maka ini yang dipilih
    print('Variable tidak ada')
except Exception:  # yang umum harus ditaroh paling bawah
    print("Unknown Error")
else:
    # bedanya kalau setelah else ada error lagi gak terdeteksi dan program interrupt setelah error
    print(hsl)
finally:
    print('finally')  # meskipun ada error di else finally akan tetap berjalan

print("tanpa finally")

# Raise bikin error/exception sendiri

skg = 5
try:
    hsl = skg + 3
    if hsl == 8:
        raise Exception
except Exception:
    print('Sacred number detected')

print("\nEnvironment Variable (simpen password di luar file python")
print("Linux/Mac")
"""
umum (windows Linux, Mac, Windows)
1 di file python :
import os
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

2.1 Linux
Simpen password python di .bashrc
Kalau mac di .bash_profile
buka .bashrc lokasinya di home
kemudian masukkan berikut di dalam file .bashrc :
export DB_USER="Username"    >> ganti sesuai username
export DB_PASS="Password"    >> ganti sesuai password

atau

2.2 Windows
cari "environment variables" di advance system settings > system properties > Environment Variables
User Variables > New 
Variable name : DB_USER
Variable value : Username   >> ganti sesuai username
User Variables > New
Variable name : DB_PASS
Variable value : Password   >> ganti sesuai password
"""