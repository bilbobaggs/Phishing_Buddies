# Titanic

![](./.images/Titanic-logo.png)

|    OS    |   Linux   |
|---------:|:----------|
|Difficulty|    Easy   |
|  Points  |     20    |
| Release  |15 Feb 2025|
|    IP    |10.10.11.55|
|   Link   |[Titanic](https://app.hackthebox.com/machines/Titanic)|

## Recon

## Recon

Let's start by looking for open ports with an nmap scan.

```
nmap  -A -sC -sV -p - -vv -oA titanic-nmap 10.10.11.55
```

For a break down of most of the options here please take a look at the Alert walkthrough.

and here is the report:

```
# Nmap 7.95 scan initiated Tue Mar 11 07:59:43 2025 as: /usr/lib/nmap/nmap -sV -sC -T4 -A -p - -vv -oA titanic-nmap 10.10.11.55
Increasing send delay for 10.10.11.55 from 5 to 10 due to 11 out of 14 dropped probes since last increase.
Warning: 10.10.11.55 giving up on port because retransmission cap hit (6).
adjust_timeouts2: packet supposedly had rtt of -74942 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -74942 microseconds.  Ignoring time.
Nmap scan report for titanic.htb (10.10.11.55)
Host is up, received echo-reply ttl 63 (0.16s latency).
Scanned at 2025-03-11 07:59:43 CDT for 640s
Not shown: 65468 closed tcp ports (reset)
PORT      STATE    SERVICE        REASON         VERSION
22/tcp    open     ssh            syn-ack ttl 63 OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 73:03:9c:76:eb:04:f1:fe:c9:e9:80:44:9c:7f:13:46 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGZG4yHYcDPrtn7U0l+ertBhGBgjIeH9vWnZcmqH0cvmCNvdcDY/ItR3tdB4yMJp0ZTth5itUVtlJJGHRYAZ8Wg=
|   256 d5:bd:1d:5e:9a:86:1c:eb:88:63:4d:5f:88:4b:7e:04 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDT1btWpkcbHWpNEEqICTtbAcQQitzOiPOmc3ZE0A69Z
80/tcp    open     http           syn-ack ttl 63 Apache httpd 2.4.52
|_http-favicon: Unknown favicon MD5: 79E1E0A79A613646F473CFEDA9E231F1
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
| http-server-header: 
|   Apache/2.4.52 (Ubuntu)
|_  Werkzeug/3.0.3 Python/3.10.12
|_http-title: Titanic - Book Your Ship Trip
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.19
TCP/IP fingerprint:
OS:SCAN(V=7.95%E=4%D=3/11%OT=22%CT=1%CU=30762%PV=Y%DS=2%DC=T%G=Y%TM=67D0363
OS:F%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=10B%TI=Z%CI=Z%TS=A)OPS(O1=M
OS:53CST11NW7%O2=M53CST11NW7%O3=M53CNNT11NW7%O4=M53CST11NW7%O5=M53CST11NW7%
OS:O6=M53CST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%
OS:DF=Y%T=40%W=FAF0%O=M53CNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=
OS:0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF
OS:=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=
OS:%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%
OS:IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 9.791 days (since Sat Mar  1 12:10:45 2025)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 554/tcp)
HOP RTT       ADDRESS
1   232.15 ms 10.10.14.1
2   232.26 ms titanic.htb (10.10.11.55)

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Mar 11 08:10:23 2025 -- 1 IP address (1 host up) scanned in 640.53 seconds
```

| Port |Description|Version|
|:----:|:---------:|:-----:|
|  22  |  OpenSSH  | 8.9p1 |
|  80  |   Apache  | 2.4.52|

Based on that output, we need to adjust our /etc/hosts

![](./.images/Screenshot-Titanic_Hosts-1.png)

Sweet now we can move on to the ffuf report.

```
ffuf -u http://titanic.htb/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt:FUZZ -recursion -ic -c -of md -o titanic.htb-ffuf.md
```

| FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash |
| :--- | :-- | :--------------- | :------- | :---------- | :------------- | :------------ | :------------ | :----------- | :------- | :--------- | :---------- | :------: |
| book | http://titanic.htb/book |  |  336 |     405     |       153      |       16      |        6      | text/html; charset=utf-8 | 120.428606ms |  |       | 66450150 |
| server-status | http://titanic.htb/server-status |  | 4227 | 403 |  276 |       20      |       10      | text/html; charset=iso-8859-1 | 118.69692ms |  |   |664501083 |

And now for the sub-domain enumeration.

```
ffuf -u http://titanic.htb -H Host:FUZZ.titanic.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -fc 301 -c -of md -o titanic.htb-subdomain-ffuf.md
```

| FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash |
| :--- | :-- | :--------------- | :------- | :---------- | :------------- | :------------ | :------------ | :----------- | :------- | :--------- | :---------- | :------: |
|  dev | http://dev.titanic.htb |   |  19  |     200     |      13982     |      1107     |      276      | text/html; charset=utf-8 | 5.150837676s |  |       |  123b413 |

By jove we got one, now we have to do more enumeration and to make another update to our /etc/hosts file.

![](./.images/Screenshot-Titanic_Hosts-2.png)

```
ffuf -u http://dev.titanic.htb/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt:FUZZ -recursion -ic -c -of md -o dev.titanic.htb-ffuf.md
```

| FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash |
| :--- | :-- | :--------------- | :------- | :---------- | :------------- | :------------ | :------------ | :----------- | :------- | :--------- | :---------- | :------: |
| administrator | http://dev.titanic.htb/administrator |  | 17 | 200 | 19997 |    1619    |       417     | text/html; charset=utf-8 | 369.445302ms |  |       |  2434311 |
|  v2  | http://dev.titanic.htb/v2 |  | 619 |     401    |       50       |       1       |        2      | application/json | 82.876511ms |     |             | 2434326b |
| developer | http://dev.titanic.htb/developer |  | 1758 | 200 |  25150   |      2139     |       506     | text/html; charset=utf-8 | 90.633011ms |  |        | 243436de |
| Administrator | http://dev.titanic.htb/Administrator |  | 3222 | 200 | 19997 |   1619   |       417     | text/html; charset=utf-8 | 208.437628ms |  |       | 24343c96 |
| nano | http://dev.titanic.htb/nano |  | 9282 |   200   |      19844     |       1619    |       417     | text/html; charset=utf-8 | 105.865781ms |  |       |243432442 |
| Developer | http://dev.titanic.htb/Developer |  | 9751 | 200 |   25151  |       2139    |       506     | text/html; charset=utf-8 | 100.392759ms |  |       |243432617 |


