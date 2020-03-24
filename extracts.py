from tqdm import tqdm
import codecs
import zipfile
import optparse
import os
import sys
import time
from termcolor import colored
#import threading

def extracts(files, password):
    file = zipfile.ZipFile(files)
    #zipfile passwords are always encoded, default = utf-8
    file.extractall(pwd = password.encode())
    file.close()

def main():
    print(colored("[+] Written by Romeos CyberGypsy","blue"))
    print(colored("[+] Bruteforce locked zipfiles fast","yellow"))
    print(" ")
    #option parser
    parser = optparse.OptionParser()
    parser.add_option("-z","--zipfile",dest = "zip",help = "Zipfile to crack")
    parser.add_option("-w","--wordlist",dest = "wordlist",help = "Password file")
    (values, keys) = parser.parse_args()
    f = codecs.open(values.wordlist,"r")
    num = 0
    for file in f.readlines():
        num+=1

    f.close()
    f = open(values.wordlist,"r", encoding = 'utf-8', errors = 'ignore')
    x = 1
    print(colored("[-] Cracking zipfile...Please wait","blue"))
    time1 = time.time()
    for password in tqdm(f.readlines()):
        password = password.strip("\n")
        #print(colored("[-] Trying password {} of {} : {}" .format(x,num,password),"green"))
        x+=1
        try:
            import math
            extracts(values.zip, password)
            time2 = time.time()
            time3 = time2 - time1
            os.system("clear")
            print(" ")
            password = colored(password,"yellow")
            print("[+] Password found:{}" .format(password))
            print("[+] Passwords tried: {}" .format(str(x)))
            print("[-] Time elapsed: {} seconds" .format(math.trunc(time3)))
            speed = x/time3
            speed = colored(str(math.trunc(speed)),"yellow")
            print("Bruteforce speed: {} words/sec" .format(str(speed)))
            break

        except:
            pass


if __name__ == '__main__':
    banner = '''
    ░▀▀█░▀█▀░█▀█░█▀▀░▀█▀░█░░░█▀▀░░░█▀▀░█▀▄░█▀█░█▀▀░█░█░█▀▀░█▀▄
    ░▄▀░░░█░░█▀▀░█▀▀░░█░░█░░░█▀▀░░░█░░░█▀▄░█▀█░█░░░█▀▄░█▀▀░█▀▄
    ░▀▀▀░▀▀▀░▀░░░▀░░░▀▀▀░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀'''
    print(colored(banner, "yellow"))

    main()
