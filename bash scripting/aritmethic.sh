#!/bin/bash

# Functions.  must be before the main part of the script

# in each case method 1 uses $((..))
#              method 2 uses let
#              method 3 uses expr tapi method ini sudah sebaiknya tidak digunakan

add() {
    answer1=$(($1 + $2))
    let answer2=($1 + $2)
    answer3=`expr $1 + $2`
}
sub() {
    answer1=$(($1 - $2))
    let answer2=($1 - $2)
    answer3=`expr $1 - $2`
}
mult() {
    answer1=$(($1 * $2))
    let answer2=($1 * $2)
    answer3=`expr $1 \* $2`
}
div() {
    answer1=$(($1 / $2))
    let answer2=($1 / $2)
    answer3=`expr $1 / $2`
}
# End of functions
#

# Main part of the script

# setting 3 argumen $1 = type, $2 = angka kedua, $3 = angka ketiga  

op=$1 ; arg1=$2 ; arg2=$3
#check apakah argumen yang dimasukkan ada 3 caranya jumlah argumen lebih kecil dari 3 message dan exit error berjalan
[[ $# -lt 3 ]] && \
    echo "Usage: Provide an operation (a,s,m,d) and two numbers" && exit 1
#check apakah op sesuai dengan modenya kalau semua terpenuhi maka echo terbaca tapi kalau ada salah satu yang tidak terpenuhi maka echo berjalan
[[ $op != a ]] && [[ $op != s ]] && [[ $op != d ]] && [[ $op != m ]] && \
    echo operator must be a, s, m, or d, not $op as supplied

# ok, do the work!

if [[ $op == a ]] ; then add $arg1 $arg2
elif [[ $op == s ]] ; then sub $arg1 $arg2
elif [[ $op == m ]] ; then mult $arg1 $arg2
elif [[ $op == d ]] ; then div $arg1 $arg2
else
echo $op is not a, s, m, or d, aborting ; exit 2 #exit 2 artinya keluar karena function tidak ada
fi

# Show the answers
echo $arg1 $op $arg2 :
echo 'Method 1, $((..)),' Answer is  $answer1
echo 'Method 2, let,    ' Answer is  $answer2
echo 'Method 3, expr,   ' Answer is  $answer3