# Pasteables
A little tip for using these, if you run 'set IP_ADDRESS=TARGET' and replace 'TARGET' with the address you get from hack the box, you can just copy paste in to command line and press enter.

## TCP Scanning with nmap
---
nmap -sC -sV $IP_ADDRESS
nmap -sC -sV -p- $IP_ADDRESS
nmap --script vuln $IP_ADDRESS
---

## UDP Scanning with nmap
---
nmap -sU -sV --top-ports 20 $IP_ADDRESS
---
