#! /usr/bin/python

import urllib.request
import urllib.parse
import re
from sys import argv
from colorama import Fore, Style

argc = len(argv)

def usage(program):
    print(f"""usage: {program} [FLAGS]
    -V          show vegan food options
    -h --help   show this menu and exit
    -p          print the source code
    """)
    exit(0)

print(Style.BRIGHT, end="")

def parse_args():
    vegan = False
    i = 1
    while i < argc:
        opt = argv[i]
        if opt == "-V":
            vegan = True
        elif opt == "-p":
            print(open(__file__).read())
            exit(0)
        elif opt == "--help" or opt == "-h":
            usage(argv[0])
        else:
            print(f"Unknown option {opt}")
        i += 1
    return vegan

vegan = parse_args()

print("Getting food menu...")

menu = re.findall(r'<p class=\"ruoka-header-(ruoka|kasvisruoka)\">([^<]*)<',str(urllib.request.urlopen(urllib.request.Request('https://www.mayk.fi/tietoa-meista/ruokailu')).read()))

days = ["ma", "ti", "ke", "to", "pe"]

for i, foods in enumerate(menu):
    f = ",".join(foods[1:]).replace("\\xc3\\xb6", 'ö').replace("\\xc3\\xa4", 'ä')
    if i % 2 == 0:
        print(Fore.CYAN + days[len(days) - len(foods) + (i // 2)])
        ft = Fore.WHITE + "Norm: "
        print(ft, f)
        if not vegan:
            print()
	
    else:
        if vegan:
            ft = Fore.GREEN + "Vege: "
            print(ft, f)
            print()
   
print(Style.RESET_ALL, end="")
