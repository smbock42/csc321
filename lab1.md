Names: Logan Schwarz, Bella Boulais, Sam Bock, Rohit Bathula

# Overthewire.org Bandit CTF WriteUp

# PASSWORDS ARE PASSWORD TO ENTER THAT LEVEL
## -> made it more readable so the passwords are the passwords achieved at each level, so they match the commands used to get them 

# Level 0 -> 1:
ls 
vim readme
Password for level 1: NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

# Level 1 -> 2:
ls
cat ./-
Password for level 2: rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

# Level 2 -> 3:
ls
cat ./’spaces in this filename’
Password for level 3: aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

# Level 3 -> 4:
ls
cd inhere
ls -a
cat .hidden
Password for level 4: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

# Level 4 -> 5:
cd inhere
file ./*
cat ./-file07
Password for level 5: lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

# Level 5 -> 6:
cd inhere,
ls * -r -l -a
cd maybehere07
cat./.file2
Password for level 6: P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

# Level 6 -> 7:
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password
Password for level 7: z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

# Level 7 -> 8:
Grep -o ‘millionth.*’ data.txt OR cat data.txt | grep millionth
Password for level 8: TESKZC0XvTetK0S9xNwm25STk5iWrBvP

# Level 8 -> 9:
sort data.txt | uniq -u
Password for level 9: EN632PlfYiZbn3PhVK3XOGSlNInNE00t

# Level 9 -> 10: 
Grep -A 2 -a ‘=.*’ data.txt OR strings data.txt | grep ===
Password for level 10: G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

# Level 10 -> 11:
base64 -d data.txt
Password for level 11: 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

# Level 11 -> 12: 
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
Password for level 12: JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

# Level 12 -> 13:
Make temp directory /tmp/logan123 and copy data.txt into it 
Xxd -r data.txt into compressed.txt
Xxd compressed.txt shows either 425a or 1f8b in the first byte block
If its 1f8b, mv compressed.txt compressed.gz 
Then gzip -d compressed.gz
Then xxd compressed
If its 425a, mv compressed compressed.bz2
Then bzip2 -d compressed.bz2
Xxd compressed
Do this until first byte is something else than gzip or bzip2 
I saw data5.bin, so
mv compressed compressed.tar
tar -xf compressed.tar
Which puts data5.bin in the directory
Xxd data5.bin shows data6.bin so 
 tar -xf data5.bin which puts data6.bin in directory
Xxd data6.bin again has 425a in this first bit, means its a bzip2 compressed
Bzip2 -d data6.bin
Puts data6.bin.out in directory
xxd data6.bin.out shows data8.bin, so
Tar -xf datat6.bin.out
Data8.bin is in og directory, xxd data8.bin has 1f8b, so gzip -d and found password
Password for level 13: wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

# Level 13 -> 14:
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
Password for level 14: fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

# Level 14 -> 15:
echo "fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq" | nc localhost 30000
Password for level 15: jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

# Level 15 -> 16:
openssl s_client -connect localhost:30001
Password for level 16: JQttfApK4SeyHwDlI9SXGR50qclOAil1

# Level 16 -> 17:
nmap -p 31000-32000 --open 127.0.0.1
See which ports are open
nc localhost <port> 
Press enter and type password. If no password gets returned, that’s correct port. 
openssl s_client -connect localhost:31790
Type password. 
Private key gets returned and nano into new file. 
Copy private key to a file on my own computer
Chmod 600 filename
ssh -i ssh.txt bandit17@bandit.labs.overthewire.org -p 2220

Password for level 17: VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e

# Level 17 -> 18:
diff passwords.new passwords.old
Password for level 18: hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

# Level 18 -> 19:
ssh -t bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
Password for level 19: awhqfNnAbc1naukrpqDYcF95h7HoMTrC

# Level 19 -> 20:
./bandit20-do cat /etc/bandit_pass/bandit20
Password for level 20: VxCazJaVykI6W36BkBU0mJTCM8rR95XT

# Level 20 -> 21
nmap -p 1-65535 --open 127.0.0. (I’m not sure nmap is completely necessary)
echo "VxCazJaVykI6W36BkBU0mJTCM8rR95XT" | nc -lp 65535 &
./suconnect 65535
Password for level 21: NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

# Level 21 -> 22
ls /etc/cron.d/
cat /etc/cron.d/cronjob_bandit22
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Password for level 22: WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff

# Level 22 -> 23
 ls  /etc/cron.d/
 cat /etc/cron.d/cronjob_bandit23
cat /usr/bin/cronjob_bandit23.sh
whoami is the user bandit23
$mytarget is a file named echo I am user $myname | md5sum | cut -d ' ' -f 1
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
Run “echo I am user $myname | md5sum | cut -d ' ' -f 1 “ with $myname = bandit23 to get the real file name 
 cat /tmp/8ca319486bfbbc3663ea0fbe81326349
Password for level 23: QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

# Level 23 -> 24: 
Same steps as before to look into cronjob_bandit24
The cronjob script runs and then deletes scripts in foo
Make a temporary directory
In tmp/whatever make a script to be run as bandit24
Open nano with nano script24.sh
#!/bin/bash
Cat /etc/bandit_pass/bandit24 > /tmp/<tmpvals>/password
Touch password
Chmod 777 -R tmp/<tmpvals>/
Ls -la to check its all there
Then put script in foo with cp script.sh /var/spool/bandit24/foo
After a minute cat /var/spool/bandit24/foo/script.sh should return no file
 Cat password shows password

Password for level 24: VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar



# Level 24 -> 25: 
for i in {0000..9999}; do echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i"; done | nc localhost 30002 > res.txt
Grep -v res.txt “Wrong!”

Password for level 25: p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

# Level 25 -> 26: 
Resize window 
ssh -i bandit26.sshkey bandit26@localhost -p 2220
Press v to enter vim visual
:shell
cat /etc/bandit_pass/bandit26
Password for level 26: c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1


# Level 26 -> 27: 
./bandit27-do cat /etc/bandit_pass/bandit27
Password for level 27: YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS

# Level 27 -> 28:
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo /tmp/smb27
Cd repo
Cat README
Password for level 28: AVanL161y9rsbcJIsFHuw35rjaOM19nR

# Level 28 -> 29:
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo /tmp/smb28
Cd repo
Cat README
Git log
git diff f08b9cc63fa1a4602fb065257633c2dae6e5651b

Password for level 29: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

# Level 29 -> 30:
git clone  ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
Cd repo
Git branch -a
Show all remote branches
Git checkout dev
Cat README

Password for level 30: xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

# Level 30 -> 31:
git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cd repo
Git tag
Git show secret

Password for level 31: OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

# Level 31 -> 32:
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
Cd repo
Echo ‘May I come in?’ > key.txt
Ls -a 
Echo “” > .gitignore
Git add .gitignore
Git commit -m “changed .gitignore”
Git push
Git add key.txt
Git commit -m “added key.txt”
Git push

Password for level 32: rmCBvG56y58BXzv98yZGdO7ATVL5dW8y

# Level 32 -> 33
$0
Cd /etc/bandit_pass
Cat bandit33

Password for level 33: odHo63fHiFqcWWJG9rLiLDtPm45KzUKy
