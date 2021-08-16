#!/bin/bash
#contoh pengaplikasian if
if [ -f "$1" ] # [] atau bisa juga [[]] digunakan untuk check value=true or false, -f untuk ngecek apabila file betulan bukan symlink ada maka true
then
    echo file "$1 exists" 
else
    echo file "$1" does not exist
fi
#contoh 2 dengan 
angka=100
if [$angka -eq 100] ; then
    echo "nilai angka sama" ; else
    echo "nilai angka tidak sama"
fi

#contoh pengaplikasian if then elif
if [ sometest ] ; then
    echo Passed test1 
elif [ somothertest ] ; then
    echo Passed test2 
fi

#contoh pengaplikasian || sebagai pengganti elif
echo what is your name
read name
if [[ "$name" == John ]] || [[ "$name" == Ringgo ]] || [[ "$name" == George ]] || [[ "$name" == Paul ]]
then    
    echo welcome $name
else
    echo you are not welcome
fi