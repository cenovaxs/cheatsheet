#!/bin/bash

#string extract, ambil sebagian aja
Name=Eddie.Haskel
#menyimpan string jadi variable
fullname=${Name} ; echo fullname = $fullname
#untuk yang dibawah ini mirip python
first=${Name:0:5} ; echo first name = $first
#yang dibawah ini mengambil semua setelah titik
last=${Name#*.} ; echo last name = $last
#menyimpan panjang kata menjadi variabel (len klo di python)
panjang=${#Name} ; echo jumlah huruf = $panjang

# contoh 2 read string, ini bisa diganti directory contoh :
#read file
#[[ -f $file ]]
# contoh dibawah mengecek kata ada atau tidak, kalau ada dia bilang isi klo tidak dia bilang tidak
read angka
if [[ -z $angka ]]
then
echo kosong
else
echo isi
fi

# check two string arguments were given
[[ $# -lt 2 ]] && \
    echo "Usage: Give two strings as arguments" && exit 1

str1=$1
str2=$2

#------------------------------------
## test command

echo "apakah kata pertama yang diinput tidak memiliki isi? kalau 1 berarti FALSE"
[ -z "$str1" ]
echo $?
# test apakah $str1 kosong bisa juga pakai [[ -z $str1 ]] atau [[ -z "$str1" ]]


echo "Apakah kata kedua memiliki isi? kalau 0 berarti TRUE;"
[ -n $str2 ]
echo $?

## comparing the lengths of two string

len1=${#str1}
len2=${#str2}
echo length of string1 = $len1, length of string2 = $len2

if [ $len1 -gt $len2 ]
then
    echo "kata pertama lebih panjang dari kata kedua"
else
    if [ $len2 -gt $len1 ]
    then
	echo "kata kedua lebih panjang dari kata pertama"
    else
	echo "kedua kata sama panjangnya"
    fi
fi

## compare the two strings to see if they are the same

if [[ $str1 == $str2 ]]
then
    echo "kedua kata sama"
else
    if [[ $str1 != $str2 ]]
    then
	echo "kata pertama tidak sama dengan kata kedua"
    fi
fi



