#!/bin/bash
#berikut contoh function
showmess(){
    echo My favorite food is: $1 $2 atau $*
}
echo ""
showmess sayur bening
showmess nanas
showmess daging matang kentang

# berikut contoh funtion dengan read atau input
# Functions harus duluan sebelum read
func1() {
echo " This message is from function 1"
}
func2() {
echo " This message is from function 2" 
}
func3() { 
echo " This message is from function 3" 
}

# tanya ke user apa pilihan dia dan masukkan ke variabel n
echo "Enter a number from 1 to 3"
read n

# panggil function dengan variabel n
func$n