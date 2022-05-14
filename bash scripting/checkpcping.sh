#!/bin/bash
if ping -c 1 192.168.2.5
then
echo PC nyala
else 
echo PC mati
fi

#jangan lupa "$ chmod +x ping.sh" untuk ubah jadi executable