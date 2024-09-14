#!/bin/zsh

if [[ -f `which which` ]]
	then if [[ ! -f `which zsh` ]]
 		then echo -e "Please install zsh"
   	fi
fi

echo -ne "Please enter the target site: "
read RemoteHost

echo -ne "Please enter the workspace path: "
read LocalWorkingDirectory

if [[ ! -d $LocalWorkingDirectory ]];then
	mkdir -p $LocalWorkingDirectory
fi

cd $LocalWorkingDirectory

echo -e "--Let's start with some nmap action--"
nmap -sS $RemoteHost -vv -T5 -AO -p- -sC -sV -oN $RemoteHost-nmap.txt

echo -e "--It's fuzzing time--"
ffuf -u http://$RemoteHost/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-directories.txt:FUZZ -recursion -ic -c -of csv -o $RemoteHost-ffuf.csv 

/ffuf -u http://FUZZ.$RemoteHost -w usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt:FUZZ -ic -c -of csv -o $RemoteHost-files-ffuf.csv 

ffuf -u http://FUZZ.$RemoteHost -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt:FUZZ -ic -c -of csv -o $RemoteHost-subdomain-ffuf.csv 

echo -e "--Let's hit it with some nikto action--"
nikto -host http://$RemoteHost -C all -output $RemoteHost-nikto.xml -Format xml

echo -e "--Let's try to clone the site--"
wget -Eme robots=off http://$RemoteHost

#echo -e "--If there are any 200's we'll grab them here--"
#mkdir -p ${LocalWorkingDirectory}/${RemoteHost}/Additional\ Files
#cat 
