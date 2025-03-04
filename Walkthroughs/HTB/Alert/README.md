# Alert

![](./.images/HTB-Alert-logo.png)  

|    OS    |   Linux   |
|---------:|:----------|
|Difficulty|    Easy   |
|  Points  |     20    |
| Release  |23 Nov 2024|
|    IP    |10.10.11.44|
|   Link   |[Alert](https://app.hackthebox.com/machines/Alert)|


## Recon

Let's start by looking for open ports with an nmap scan.

```
nmap  -A -sC -sV -p - -vv -oA alert-nmap 10.10.11.44
```

For a break down of most of the options here please take a look at the Chemistry walkthrough. The only new option is 

-sV: Probe open ports to determine service/version info

and here is the report:

``` 
# Nmap 7.95 scan initiated Mon Mar  3 20:29:48 2025 as: /usr/lib/nmap/nmap -A -sC -sV -p - -vv -oA alert-nmap 10.10.11.44
Increasing send delay for 10.10.11.44 from 10 to 20 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.11.44 from 20 to 40 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.11.44 from 40 to 80 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.11.44 from 80 to 160 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.11.44 from 160 to 320 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.11.44 from 320 to 640 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.11.44 from 640 to 1000 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for alert.htb (10.10.11.44)
Host is up, received reset ttl 63 (0.059s latency).
Scanned at 2025-03-03 20:29:49 CST for 8035s
Not shown: 65516 closed tcp ports (reset)
PORT      STATE    SERVICE        REASON                              VERSION
22/tcp    open     ssh            syn-ack ttl 63                      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7e:46:2c:46:6e:e6:d1:eb:2d:9d:34:25:e6:36:14:a7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDSrBVJEKTgtUohrzoK9i67CgzqLAxnhEsPmW8hS5CFFGYikUduAcNkKsmmgQI09Q+6pa+7YHsnxcerBnW0taI//IYB5TI/LSE3yUxyk/ROkKLXPNiNGUhC6QiCj3ZTvThyHrFD9ZTxWfZKEQTcOiPs15+HRPCZepPouRtREGwmJcvDal1ix8p/2/C8X57ekouEEpIk1wzDTG5AM2/D08gXXe0TP+KYEaZEzAKM/mQUAqNTxfjc9x5rlfPYW+50kTDwtyKta57tBkkRCnnns0YRnPNtt0AH374ZkYLcqpzxwN8iTNXaeVT/dGfF4mA1uW89hSMarmiRgRh20Y1KIaInHjv9YcvSlbWz+2sz3ev725d4IExQTvDR4sfUAdysIX/q1iNpleyRgM4cvDMjxD6lEKpvQYSWVlRoJwbUUnJqnmZXboRwzRl+V3XCUaABJrA/1K1gvJfsPcU5LX303CV6LDwvLJIcgXlEbtjhkcxz7b7CS78BEW9hPifCUDGKfUs=
|   256 45:7b:20:95:ec:17:c5:b4:d8:86:50:81:e0:8c:e8:b8 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHYLF+puo27gFRX69GBeZJqCeHN3ps2BScsUhKoDV66yEPMOo/Sn588F/wqBnJxsPB3KSFH+kbYW2M6erFI3U5k=
|   256 cb:92:ad:6b:fc:c8:8e:5e:9f:8c:a2:69:1b:6d:d0:f7 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG/QUl3gapBOWCGEHplsOKe2NlWjlrb5vTTLjg6gMuGl
80/tcp    open     http           syn-ack ttl 63                      Apache httpd 2.4.41 ((Ubuntu))
| http-title: Alert - Markdown Viewer
|_Requested resource was index.php?page=alert
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
1866/tcp  filtered swrmi          host-unreach from 10.10.14.1 ttl 64
2716/tcp  filtered inova-ip-disco no-response
12227/tcp filtered unknown        no-response
14505/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
17195/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
18535/tcp filtered unknown        no-response
19965/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
22547/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
29676/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
31785/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
38088/tcp filtered unknown        no-response
42008/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
47187/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
49271/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
53555/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
57453/tcp filtered unknown        host-unreach from 10.10.14.1 ttl 64
58207/tcp filtered unknown        no-response
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.19
TCP/IP fingerprint:
OS:SCAN(V=7.95%E=4%D=3/3%OT=22%CT=1%CU=39981%PV=Y%DS=2%DC=T%G=Y%TM=67C68500
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)OPS(
OS:O1=M53CST11NW7%O2=M53CST11NW7%O3=M53CNNT11NW7%O4=M53CST11NW7%O5=M53CST11
OS:NW7%O6=M53CST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(
OS:R=Y%DF=Y%T=40%W=FAF0%O=M53CNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS
OS:%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=
OS:Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=
OS:R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T
OS:=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=
OS:S)

Uptime guess: 48.245 days (since Tue Jan 14 16:50:57 2025)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1723/tcp)
HOP RTT      ADDRESS
1   58.73 ms 10.10.14.1
2   58.85 ms alert.htb (10.10.11.44)

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Mar  3 22:43:44 2025 -- 1 IP address (1 host up) scanned in 8035.42 seconds
```
