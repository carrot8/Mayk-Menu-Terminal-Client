## MAYK MENU TERMINAL CLIENT FOR LINUX
V.1.0

### What this is?
Mayk-Menu Terminal Client is a python script that displays the contents of the Mayk food menu for the current week.
### How it works?
It just gets the www.mayk.fi/tietoa-meista/ruokailu like ```curl``` and parses it with regex and styles it.

---

### Quick guide
Just run `git clone https://github.com/openMayk/Mayk-Menu-Terminal-Client.git; cd Mayk-Menu-Terminal-Client; mv ./ruoka /usr/bin; chmod +x /usr/bin/ruoka/; pip install colorama` and `ruoka --help` to get info on the program

#### Install python (if you dont have i't already)
###### Debian based (ubuntu, pop_!os etc):
`sudo apt install python`
###### Arch based (manjaro, endeavourOS):
`sudo pacman -S python`
###### Redhat based(fedora)
`sudo rpm -i python`

#### Installation (for linux)
0. Install python if you dont have it please check above the installation guide.
1. ```git clone https://github.com/openMayk/Mayk-Menu-Terminal-Client``` Clone the repo
2. ```cd Mayk-Menu-Terminal-Client``` Change dir to the cloned repo
3. ```chmod +x ruoka``` Give executable permissions for the program
4. ```mv ruoka /usr/bin/``` Move the program to bin
5. If any problems just feel free to contact me!

#### Installation for crazies(aka. termux users)
0. Install python `pkg i python`
1. git clone https://github.com/openMayk/Mayk-Menu-Terminal-Client
2. `cd Mayk-Menu-Terminal-Client`
3. Use your favorite text editor to change the `#! /usr/bin/python` to `#! /data/data/com.termux/files/usr/bin/python`
4. Then you will need to use that editor again to add the RUOKA to your path `vim ~/.bashrc` then add `export PATH=$PATH:~/Mayk-Menu-Terminal-Client/ruoka` to the end
5. Now you can just run `ruoka --help`
6. If any problems feel free to contact me!

---
### Photos
![image](https://user-images.githubusercontent.com/78662938/142903922-3735a3ee-d7ce-420a-a0c8-427ddce1b555.png)
![termuxMaykMenu](https://user-images.githubusercontent.com/78662938/142901876-8cb567b8-12d1-4cc6-a374-df852e1c0a69.jpg)

### Contact info
Found in [Carrot8](https://github.com/carrot8) GitHub profile.
