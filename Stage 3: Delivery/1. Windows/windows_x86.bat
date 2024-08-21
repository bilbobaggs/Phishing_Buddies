@echo off
whoami
whoami /priv
whoami /groups
net users
net localgroup
hostname
systeminfo
wmic qfe
tasklist /SVC
ipconfig /ALL
route print
netstat -ano
sc query windefend
netsh firewall show state
