from functools import wraps
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
# Huruf (STRING)
print("\nHuruf (STRING)\n")

# type() mengecek type variabel
# kalau mau import lebih dari satu bisa pake coma contoh:

# input untuk masukkin interactive input dari user
# x = input('masukkan nama: ')    # ini bakal ada tulisan pembuka untuk memberi tahu pengguna
# print("halo " + x)

message = 'string'
print(type(message))  # <class 'str'>
# mengecek class menggunakan is instance, bisa juga mengecek class buatan di OOP
# isinstance
print(isinstance(message, str))  # True

# hassattr


class Person:
    name = "John"
    age = 36
    country = "Norway"


x = hasattr(Person, 'age')  # apakah ada attribute age dalam class person
print(x)  # True

# callable


def x():
    a = 5


print(callable(x))  # True

a = 5
print(callable(a))  # False karena a itu tidak callable

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

print(
    r'\nspasi\n')  # r membuat ignore special case sehingga \n tetap ter print
# Id() mengecek lokasi dalam memory
print(id(message))  # 3229004571568

# untuk mengecek method apa saja yang bisa digunakan
print(
    dir(message)
)  # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
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
# contoh f string dictionary kwargs
# This is BOOBY"S UNIVERSE
akhir = f'My Name is {person["name"]} and my age is {person["age"]}'
# inget untuk contoh diatas harus diperhatikan quotenya biar gak error
# contoh artimatika langsung di dalam f string
tambah = f'seratus tambah seribu sama dengan {100+1000}'
print(tambah)  # seratus tambah seribu sama dengan 1100
# for dengan f'
for n in range(10):
    kalimat = f"countdown {n:02}"
    print(kalimat)
# f' dengan datetime
birthday = datetime.datetime(1990, 1, 1)
kalimat = f"Ulang tahunku tanggal {birthday:%B %d, %Y}"
print(kalimat)

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
print(7 // 2)  # 3
print(4 // 2)  # 2
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

# List and Tuples
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
# split bisa juga seperti ini tapi inget jumlah instance harus sama dengan jumlah item dalam list:
instance1, instance2, instance3, instance4, instance5 = matpel_join.split(
    " - ")
print(f'{instance1}, {instance2}')  # agama, bahasa

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
# del hapus
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

# named tupple
# tupple yang dicustom sehingga mudah untuk memanggilnya dan mengupdatenya
# pertama harus import dulu from collections import namedtuple
"""
from collections import namedtuple

# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])

cara masukkan variable:
color = Color(blue=55,green=155,red=255)
atau
color = Color(55,155,255)

cara panggil:
print(color.red)
print(color.blue)
# atau tapi bisa juga pakai manual
print(color[1])
"""

# generator kyk list tapi menunggu untuk di eksekusi, ini bisa simpan memory
print("\nGenerator\n")


def kuadrat(q2):
    for i in q2:
        yield (i * i)


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

y = 6
if x == 5 or y == 6:
    print("if or if")

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

# loop in loop
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
# dibawah ini untuk return nama funct
print(hello_func.__name__)  # hello func
# dibawah ini akan menjalankan funtio
print(hello_func())  # None


def hello_func():
    print("Hello")


x = hello_func(
)  # hati2 meskipun hanya membuat variable tapi hello_func tetap dipanggil
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
# (['math', 'art'], {'name': 'john', 'age': 20})
# {}

# pakai * untuk hasilnya terpisah beda line tapi harus tuple dulu baru dict kalau terbalik error
student_info(*courses, **info)
# ('math', 'art')
# {'name': 'john', 'age': 20}

# module import dan std library

print("\nmodule\n")
# import module
# ini bakal nyari module yang ada dalam local folder
print(matpel)  # ['agama', 'bahasa', 'fis', 'mat', 'sejarah']
print(module.find(matpel, "sejarah"))  # 4
# harus dalam format <module>.<function>

# as
# import module as mm
print(mm.find(matpel, "sejarah"))  # 4

# from dipakai supaya pendek jadi langsung function aja
# from module import find
# from module import find, test  = untuk mengimport multiple
# from module import *  = untuk menimport semua function
print(find(matpel, 'sejarah'))  # 4

# from as
# from module import find as fi
print(fi(matpel, 'sejarah'))

# sys
print("\nsys.path\n")
# dibawah ini untuk mengecek module dari mana saja
print(
    sys.path
)  # ['e:\\pujas\\programing\\cheatsheet', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\pujas\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Users\\pujas\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']
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

print(datetime.datetime.today())  # tanggal hari ini local
# tanggal hari ini default local tp bisa diganti
print(datetime.datetime.now())
print(datetime.datetime.utcnow())  # tanggal hari ini ikut timezone UTC
print(calendar.isleap(2220))  # True

# datetime.date hanya mengakomodasi tahun bulan hari
# datetime.time hanya mengakomodasi jam menit detik microsecond
# datetime.datetime mengakomodasi semuanya

print('\nFormat Datetime\n')
my_date = datetime.datetime(2022, 5, 31, 22, 51, 0)
# Default python format    2022-05-31 22:51:00
print('Default python format\t', my_date)

# ambil hanya tertentu tahun/tanggal/bulan/dll
print(my_date.year)  # 2022
print(my_date.month)  # 5
print(my_date.day)  # 31
print(my_date.hour)  # 22
print(my_date.minute)  # 51
print(my_date.second)  # 0

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
    my_date
)  # jangan lupa taruh 0 karena kita menggunakan 3 variabel namun satu argument
print(complexdate)  # May 31, 2022 jatuh pada hari Tuesday dan hari ke 151

print('\nPytz timezone aware datetime\n')
# pytz timezone aware datetime
# pip install pytz
# import pytz

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
print(
    hasil4
)  # [['a', 0], ['a', 1], ['a', 2], ['a', 3], ['b', 0], ['b', 1], ['b', 2], ['b', 3], ['c', 0], ['c', 1], ['c', 2], ['c', 3], ['d', 0], ['d', 1], ['d', 2], ['d', 3]]
# LC
hasil4 = [[huruf, angka] for huruf in 'abcd' for angka in range(4)]
print(
    hasil4
)  # [['a', 0], ['a', 1], ['a', 2], ['a', 3], ['b', 0], ['b', 1], ['b', 2], ['b', 3], ['c', 0], ['c', 1], ['c', 2], ['c', 3], ['d', 0], ['d', 1], ['d', 2], ['d', 3]]

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
        yield n * n


my_gen = gen_func(nums)

print(list(my_gen))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# generator comprehension :

my_gen = (n * n for n in nums)

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
# Isi dari file txt. Read kalau selesai membaca dia akan ke akhir jadinya tidak bisa baca ulang
print(f.read())
print(f.read(100)) # membaca isi 100 character pertama saja
print(len(f.read())) # melihat berapa Character sampai tulisan habis
print(f.tell()) # melihat posisi sudah sampai dimana
f.seek(0) # kembali ke posisi 0 awal
# membuat list yang berisi setiap baris dalam isi file, jadi bisa dipanggil per baris
print(f.readlines())
# membaca baris per baris, argumen2 end='' mengatur hasilnya menjadi spasi karena karena default dari end adalah baris baru
print(f.readline(), end='')

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
print(
    t2 - t1
)  # di awal code ada t1=time.time() di baris 15, t2-t1 menunjukkan waktu yang diperlukan komputer untuk menjalankan program sampai titik ini

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

# Closure (function dalam function yang siap di ekesekusi)
print('\nClosure\n')


def outer_func(arg):
    message = arg

    def inner_func(arg2):
        print(arg + arg2)

    return inner_func


outer_func("test")('aja')  # testaja
# <function outer_func.<locals>.inner_func at 0x7f8f6b607430>
print(outer_func("test"))
print(outer_func)  # <function outer_func at 0x7f8f6b6074c0>

# Decorator
print('\nDecorator\n')
# tujuan decorator itu dipakai supaya satu fungsi bisa dipakai di banyak fungsi lainnya tanpa atau sedikit perubahan

# introduction


def decorator_function(original_function):

    def wrapper_function():
        print(f'wrapper executed before {original_function.__name__}')
        return original_function()

    print(f'decorator executed before {wrapper_function.__name__}')
    return wrapper_function


def display():
    print('Display function ran')


decorated_display = decorator_function(display)
decorated_display()
# wrapper function  >> karena decorator function return wrapper funtion
print(decorated_display.__name__)
# @decorator_function itu sama aja dengan display = decorator_function(display) tapi decorator bisa sebelum def display():


@decorator_function
def display():
    print('Decorator display function ran')


display()

# Decorator yang biasa dipakai umum
print('\nDecorator Umum\n')


def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print(f'wrapper_function executed before {original_function.__name__}')
        return original_function(*args, **kwargs)

    print(f'decorator executed before {original_function.__name__}')
    return wrapper_function


@decorator_function
def display_info(name, age):
    print(f'My name is {name} and my age is {age} years old')


display_info('test', 100)
print(display_info.__name__)
"""
kalau di iterate seperti berikut:
decorator_function(display_info('test',100)
wrapper_function(display_info('test', 100)
display_info('test', 100)
"""

# Decorator Class
print('\nDecorator Class\n')


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    # __call__ mebuat class bisa dipanggil seperti function biasa menggunakan ()
    def __call__(self, *args, **kwargs):
        print(
            f'call method executed this before {self.original_function.__name__}'
        )
        return self.original_function(*args, **kwargs)


@decorator_class
def display_info(name, age):
    print(f'My name is {name} and my age is {age} years old')


display_info('test', 100)

# multiple decorator
print('\nMultiple Decorator\n')
# stacking decorator


def my_timer(orig_func):

    def wrapper_timer(*args, **kwargs):
        print(f'wrapper_timer executed before {orig_func.__name__}')
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in {t2} sec')
        return result  # function bisa berjalan tanpa line ini

    print(f"my_timer_func executed before {orig_func.__name__}")
    return wrapper_timer


# kedua decorator dibawah sama dengan :
# display_info = decorator_function(my_timer(displayinfo))


@decorator_function
@my_timer
def display_info(name, age):
    print(f'My name is {name} and my age is {age} years old')


display_info('test', 100)
print(display_info.__name__)  # wrapper_func

# Nah kalau urutan kebalik maka nama funtion berubah :
print("\nkebalik\n")

# perbedaan nama function saat urutan dibalik akan merusak decorator yang name sensitive karena nama funtion bukan original melainkan wrapper dari decorator yang pertama
# display_info = my_timer(decorator_function(displayinfo))


@my_timer
@decorator_function
def display_info(name, age):
    print(f'My name is {name} and my age is {age} years old')


display_info('test', 100)
print(display_info.__name__)  # wrapper_timer

print('\nfunctools import wraps\n')
# dalam hal ini yang dihitung waktunya oleh my_timer adalah wrapper_function bukan display_info. hal tersebut bukanlah yang kita mau
"""
Solusinya adalah:
menggunakan wraps. Wraps akan membuat nama yang digunakan selalu original function
from functools import wraps
"""


def decorator_function(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print(f'wrapper_function executed before {original_function.__name__}')
        return original_function(*args, **kwargs)

    print(f'decorator executed before {original_function.__name__}')
    return wrapper_function


def my_timer(orig_func):

    @wraps(orig_func)
    def wrapper_timer(*args, **kwargs):
        print(f'wrapper_timer executed before {orig_func.__name__}')
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in {t2} sec')
        return result  # function bisa berjalan tanpa line ini

    print(f"my_timer_func executed before {orig_func.__name__}")
    return wrapper_timer


@my_timer
@decorator_function
def display_info(name, age):
    print(f'My name is {name} and my age is {age} years old')


display_info('test', 100)
print(display_info.__name__)  # display_info

# decorator with arguments
# beberapa decorator dapat memiliki argumen caranya adalah dengan menambah satu layer wrapper
# berikut contohnya:


def prefix_decorator(prefix):

    def decorator_function(original_function):

        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)

# OOP Object Oriented Programming
print('\nOOP Object Oriented Programming\n')

# pertama buat class ini berfungsi juga untuk group


class Employee:
    # kedua __init__ dan self. Init dan self ini membuat variable pada global menjadi variable dalam class
    def __init__(self, first, last, pay):  # self pertama jangan lupa
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(
        self
    ):  # self yang init dapat digunakan kembali pada method lain di class yang sama
        return '{} {}'.format(self.first, self.last)


# rumus penamaan adalah sebagai berikut:
# self = ClassName(first, last, pay)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# cara panggil argument

print(emp_1.first)

# cara panggil method ada 2 :

print(emp_1.fullname())  # jangan lupa () karena ini method
# atau
print(Employee.fullname(emp_1))

# untuk melihat atrribut apa saja yang dimiliki sebuah class:
print(Employee.__dict__)

# Instance variable dan class variables
print('\nInstance Variable\n')


class Employee:

    kenaikan = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def naik_gaji(self):
        self.pay = int(self.pay * self.kenaikan)
        # atau
        # self.pay = int(self.pay * Employee.kenaikan)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)  # 50000
emp_1.naik_gaji()  # jalankan naik gaji untuk emp_1
print(emp_1.pay)  # 52500
print(emp_2.pay)  # 60000     tetap tidak naik karena emp_2 tidak dijalankan

#  memanggil kenaikan
print(Employee.kenaikan)  # 1.05
print(emp_1.kenaikan)  # 1.05
print(emp_2.kenaikan)  # 1.05

# sebenernya emp_1.kenaikan itu gak ada dia ambil dari Employee.kenaikan
# cara liatnya pakai __dict__
print(emp_1.__dict__)  # hasilnya tidak ada kenaikan
print(Employee.__dict__)  # hasilnya disini ada kenaikan

# Kalau mau tambah manual
Employee.kenaikan = 1.06
emp_1.kenaikan = 1.07

print(Employee.kenaikan)  # 1.06
print(emp_1.kenaikan)  # 1.07
print(emp_2.kenaikan)  # 1.06

# skrg emp_1.kenaikan punya atribut kenaikan setelah ditambah manual
print(emp_1.__dict__)  # ada atribut kenaikan
print(Employee.__dict__)  # atribut kenaikan berubah jadi 1.06
# tidak ada atribut kenaikan, sehingga dia tetap mencari dari Employee
print(emp_2.__dict__)

# contoh lain jumlah employee


class Employee:

    jumlah_employee = 0  # set awal jumlah employee
    kenaikan = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        # tiap kali def __init__ berjalan akan menambah Employee sebanyak 1 jadinya kita bisa lihat total employee
        Employee.jumlah_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def naik_gaji(self):
        self.pay = int(self.pay * self.kenaikan)
        # atau
        # self.pay = int(self.pay * Employee.kenaikan)


print(Employee.jumlah_employee)  # 0

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.jumlah_employee)  # 2
# 2 karena emp_1.jumlah_employee tidak ada dan akan menggunakan Employee.jumlah_employee
print(emp_1.jumlah_employee)

# class method @classmethod
# regular method mengambil instance untuk dijadikan argumen,
# class method mengambil class sebagai argumen
print('\nClass Method\n')


class Employee:

    jumlah_employee = 0
    kenaikan = 1.05

    @classmethod
    def set_raise_amt(cls, amount):  # ambil class sebagai argument
        cls.kenaikan = amount

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.jumlah_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def naik_gaji(self):
        self.pay = int(self.pay * self.kenaikan)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
# untuk jalankan caranya :
# cls.classmethod(amount)
Employee.set_raise_amt(1.08)

print(Employee.kenaikan)
print(emp_1.kenaikan)
print(emp_2.kenaikan)

emp_2.naik_gaji()
print(emp_2.pay)  # 64800
print(emp_1.pay)  # 50000     belum naik karena emp_1.naikgaji() tidak dijalankan
print(emp_1.__dict__)
print(emp_2.__dict__)


# contoh 2 misalkan data raw bentuknya string:
# cara 1 manual
emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-60000'
emp_str3 = 'Jane-Richard-90000'

# untuk mengubah kita menggunakan .split
first, last, pay = emp_str1.split('-')

# masukkan hasilnya ke dalam class
new_emp1 = Employee(first, last, pay)

print(new_emp1.email)
print(new_emp1.pay)

# cara 2 pakai class method


class Employee:

    jumlah_employee = 0
    kenaikan = 1.05

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')   # split string
        # masukkan hasil split ke dalam class
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.kenaikan = amount

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.jumlah_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def naik_gaji(self):
        self.pay = int(self.pay * self.kenaikan)


# rumus untuk apply :
# Instance = cls.classmethod(emp_str)   contoh:
new_emp2 = Employee.from_string(emp_str2)
print(new_emp2.email)

# static method
print('\nStatic Method\n')
# Static method adalah method yang tidak mengambil instance dan class untuk dijadikan argument


class Employee:

    jumlah_employee = 0
    kenaikan = 1.05

    @staticmethod       # static method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # cek apakah jatuh hari sabtu dan minggu (5/6)
            return False    # kalau benar maka false
        return True         # kalau salah maka True

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.kenaikan = amount

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.jumlah_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def naik_gaji(self):
        self.pay = int(self.pay * self.kenaikan)


my_date2 = datetime.date(2016, 7, 10)
# Check ini jatuhnya hari apa
print(datetime.date(2016, 7, 10).weekday())     # 6     hari minggu
# Rumusnya:
# Class.staticmethod(day)
print(Employee.is_workday(my_date2))            # False

# Subclasses
print('\nSubclassess\n')


class Developer(Employee):      # Developer menjadi subclass dari Employee, semua method yang ada di Employee dapat diakses oleh Developer meskipun developer tidak memiliki method sama sekali
    pass


dev1 = Developer('Corey', 'Schafer', 50000)
print(dev1.email)

# method resolution order: Developer, Employee, builtins.object
# print(help(Developer))
# help diatas bisa menunjukkan method apa yang bisa diakses oleh developer

# 1     dibawah ini menunjukkan meskipun developer yang diakses namun hal tersebut dihitung sebagai Employee sehingga angka jumlah Employee naik
print(Employee.jumlah_employee)


class Developer(Employee):
    kenaikan = 1.1


print(Developer.__dict__)   # skrg Developer punya local dict kenaikan 1,1

dev1 = Developer('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(dev1.pay)  # 50000
print(emp_2.pay)  # 60000
dev1.naik_gaji()
emp_2.naik_gaji()
print(dev1.pay)  # 55000    naik 10% Developer
print(emp_2.pay)  # 63000    naik 5%  Employee
# kenaikan pada Class Developer tidak mempengaruhi kenaikan pada Class Employee


# Super() menambah function tanpa perlu mengulang method yang sudah ada di class utama
# misalnya kita mau tambah programing languange  :

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # atau bisa juga
        # Employee.__init__(self, first, last, pay)     tapi ini gak disarankan karena ada super()
        self.prog_lang = prog_lang

    kenaikan = 1.1


dev1 = Developer('Corey', 'Schafer', 50000, 'python')
print(dev1.prog_lang)   # python

# contoh lain bikin class manager


class Manager(Employee):
    # set default sebagai None jangan empty list []
    def __init__(self, first, last, pay, ab=None):
        super().__init__(first, last, pay)
        if ab is None:          # kalau ab None
            self.ab = []        # buat list kosong
        else:
            self.ab = ab        # bikin daftar anak buah

    def tambah_ab(self, emp):   # terima 2 argumen instance(mgr1) dan anak buah
        if emp not in self.ab:  # apabila anak buah tidak ada di dalam daftar
            self.ab.append(emp)  # tambah anak buah ke dalam daftar

    def hapus_ab(self, emp):
        if emp in self.ab:
            self.ab.remove(emp)

    def print_ab(self):
        for emp in self.ab:
            print(emp.fullname())


mgr1 = Manager('Sue', 'Smith', 90000, [dev1])


print(mgr1.fullname())
mgr1.print_ab()         # Corey Schafer
mgr1.tambah_ab(emp_2)
mgr1.print_ab()         # Test Employee


# isinstance untuk cek apakah instance dari class
print(isinstance(mgr1, Employee))       # True
print(isinstance(mgr1, Manager))        # True
print(isinstance(mgr1, Developer))      # False

# issubclass untuk cek apakah subclass dari class
print(issubclass(Manager, Employee))    # True
print(issubclass(Developer, Employee))  # True
print(issubclass(Employee, Employee))   # True

"""
str() vs repr()
str() itu bentuk string final yang kita tidak bisa tau kode python apa yang menyebabkan string tsb
repr() itu string yang masih bisa kita ketahui kode python yang menghasilkan string tersebut 
str() itu dipakai untuk pengguna
repr() itu dipakai untuk developer
contoh:"""

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)

print(f'str(a): {str(a)}')      # 2022-06-17 14:41:03.999198+00:00
print(f'str(b): {str(b)}')      # 2022-06-17 14:41:03.999198+00:00
# datetime.datetime(2022, 6, 17, 14, 41, 3, 999198, tzinfo=<UTC>)
print(f'repr(a): {repr(a)}')
print(f'repr(b): {repr(b)}')    # '2022-06-17 14:41:03.999198+00:00'


print('\nMagic Dunder\n')
# Magic dunder
# berikut list magic methods apa aja yang bisa digunakan di python
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# __repr__ dan __str__
print('\n__repr__ dan __str__\n')
# tujuannya adalah apabila kita panggil str() dan repr() maka dia akan menjalankan method __str__ dan __repr__ yang ada dalam class


class Employee:

    jumlah_employee = 0
    kenaikan = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def __str__(self):          # buat dunder __str__
        return f'{self.fullname()}, {self.email}'

    def __repr__(self):         # buat dunder __repr__
        return f'Employee({self.first}, {self.last}, {self.pay})'

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.kenaikan = amount

        Employee.jumlah_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def naik_gaji(self):
        self.pay = int(self.pay * self.kenaikan)


emp_1 = Employee('Corey', 'Schafer', 50000)

# untuk panggil repr caranya:
print(repr(emp_1))  # Employee(Corey, Schafer, 50000)
# atau
print(emp_1.__repr__())  # Employee(Corey, Schafer, 50000)

# untuk panggil str caranya :

# secara default klo di print(emp_1) yang keluar adalah str(emp_1)
print(emp_1)  # Corey Schafer, Corey.Schafer@email.com

# kalau memang mau spesial bisa:
print(str(emp_1))  # Corey Schafer, Corey.Schafer@email.com
# atau
print(emp_1.__str__())  # Corey Schafer, Corey.Schafer@email.com

print('\n__add__\n')
# dunder __add__
# disini kita menggunakan + untuk memanggil method __add__ yang ada pada class Employee
# selain add masih banyak yang lain kyk - * /,  dst bisa dilihat di

print(1+2)
# itu sebenarnya adalah:
print(int.__add__(1, 2))
# sementara :
print('a'+'b')
# di awal ada str. yang membedakan dan membuat tidak error
print(str.__add__('a', 'b'))


class Employee:

    jumlah_employee = 0
    kenaikan = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def __str__(self):
        return f'{self.fullname()}, {self.email}'

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __add__(self, other):       # buat def dunder add
        return self.pay + other.pay

    def __len__(self):              # buat def dunder add
        return len(self.fullname())

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.kenaikan = amount

        Employee.jumlah_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def naik_gaji(self):
        self.pay = int(self.pay * self.kenaikan)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)  # 110000       hasil jumlah kedua gaji

# contoh dunder lain len()

print(len('test'))
# sama dengan :
print('test'.__len__())

print(len(emp_1))  # 13   karena ada def __len__ di class Employee

# untuk dunder lainya:
# https://docs.python.org/3/reference/datamodel.html#special-method-names


# kalau misalnya kita ganti first name jadi pujas maka email tidak berubah karena email tidak melihat emp_1.first melainkan self.first


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1.first = 'pujas'           # ganti ke pujas

print(emp_1.first)  # pujas
print(emp_1.last)   # Schafer
# Corey.Schafer@email.com  >> ini gak berubah karena tidak melihat emp_1.first
print(emp_1.email)
print(emp_1.fullname())      # pujas Schafer

# karena itu kita harus ubah email atribute menjadi method


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    def email(self):
        return '{}_{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1.first = 'pujas'

print(emp_1.first)          # pujas
print(emp_1.last)           # Schafer
print(emp_1.email())        # pujas_Schafer@email.com    >> Nah sekarang berhasil berubah tapi permasalahannya dia bentuknya atribut bukan method, kalau sudah terlanjur dipakai classnya oleh program lain maka semua harus ditambah ()
print(emp_1.fullname())     # pujas Schafer

# Property Decorator
print('\nProperty Decorator\n')
# property decorator fungsinya mengubah method untuk bisa dipanggil sebagai atribut
# contohnya emp_1.email() setelah pakai property decorator bakal bisa dipanggil hanya dengan emp_1.email


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}_{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1.first = 'pujas'

print(emp_1.first)          # pujas
print(emp_1.last)           # Schafer
# pujas_Schafer@email.com    >> Nah skrg method bisa dipanggil sebagai atribut
print(emp_1.email)
print(emp_1.fullname)     # pujas Schafer

# setter
print('\nSetter\n')
# kalau kita mau ganti langsung dari fullname kan ga bisa karena fullname itu method bukan atribut contoh:
# emp_1.fullname = 'test', 'name'  >> attribute error cant set atribut

# Kalau mau kita itu bisa kita lakukan dengan .setter
# kalau kita tidak pakai setter maka cuma fullname saja yang update yang lain masih atribut yang lama


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}_{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1.first = 'pujas'
emp_1.fullname = 'test name'

print(emp_1.first)          # test                      # first berubah
print(emp_1.last)           # name                      # last berubah
print(emp_1.email)          # test_name@email.com       # email pun ikut berubah
print(emp_1.fullname)       # test name

print('\nDeleter\n')
# Deleter berfungsi untuk menjalankan program dengan command del


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}_{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Database deleted')
        self.first = None       # gak harus delete sebenarnya bisa apa aja
        self.last = None


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1.first = 'pujas'
emp_1.fullname = 'test name'

print(emp_1.first)          # test
print(emp_1.last)           # name
print(emp_1.email)          # test_name@email.com
print(emp_1.fullname)       # test name

del emp_1.fullname          # gunakan command del untuk menjalankannya

print(emp_1.first)          # None
print(emp_1.last)           # None
print(emp_1.email)          # None_None@email.com
print(emp_1.fullname)       # None None
