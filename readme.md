## MAYK TERMINAL CLIENT FOR LINUX


### What this is?
It is python script that checks what does mayk's cafeteria have in menu and print's it to your terminal.


### How to use?
You need to just download the ```ruoka``` and put it in your $PATH. 

#### Tutorial
0. You need to have python installed.
1. ```git clone https://github.com/carrot8/Mayk-Terminal-Client.git```
2. Optional: ```mv ruoka whatUwantToCallIt```
3. Optional: use your favorite text editor to change the VEGAN value to show only the vegan/meat food.
4. ```mv ruoka /usr/bin/```
5. Just run ```ruoka``` in  your terminal

### How it works?
It just gets the www.mayk.fi/tietoa-meista/ruokailu like ```curl``` and parses it with regex and styles it.

### Photos
![image](https://user-images.githubusercontent.com/78662938/142719948-c03b7a53-4547-41ec-b7fe-35845e66b187.png)
