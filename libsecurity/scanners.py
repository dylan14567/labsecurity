import os
import sys
import time
import nmap
import urllib.request
import json
import requests
import dns.resolver
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

init(autoreset=True)


class scanner:

    def ___init__(self):
        #print ("Welcome")
        return

    def scanports(self, ip):
        self.ip = ip
        nm = nmap.PortScanner()
        ports_open = "-p "
        results = nm.scan(self.ip, arguments="--top-ports 1000 -sT -n -Pn -T4")
        count = 0
        #print (results)
        print("\nHost : {}".format(self.ip))
        print("State : {}".format(nm[self.ip].state()))
        for proto in nm[self.ip].all_protocols():
            print("Protocol : {}".format(proto))
            lport = nm[self.ip][proto].keys()
            sorted(lport)
            for port in lport:
                print("port : {}\tstate : {}".format(
                    port, nm[ip][proto][port]["state"]))
                if count == 0:
                    ports_open = ports_open+str(port)
                    count = 1
                else:
                    ports_open = ports_open+","+str(port)

        print(Style.BRIGHT + Fore.BLUE +
              "\n[*] Ports Open: " + ports_open + " " + "Host: "+str(self.ip))
        print(Style.BRIGHT + Fore.BLUE + "[*] Scan finished")

    def scanport(self, ip, port):
        self.ip = ip
        self.port = port
        nm = nmap.PortScanner()
        nm.scan(self.ip, self.port, arguments='-sV --version-intensity 3')
        print("Protocols used: {}".format(nm[self.ip].all_protocols()))
        print("Machine status: {}".format(nm[self.ip].state()))

        for ports in nm[self.ip]['tcp'].keys():
            for data in nm[self.ip]['tcp'][ports]:
                print(data + " : " + nm[self.ip]['tcp'][ports][data])

        print(Style.BRIGHT + Fore.BLUE + "[*] Scan finished")

    def scanns(self, ip):
        try:
            self.ip = ip
            target = dns.resolver.resolve(self.ip, "NS")
            for x in target:
                print(x)

            print(Style.BRIGHT + Fore.BLUE + "[*] Scan finished")
        except:
            print(Style.BRIGHT + Fore.RED +
                  "[*] Error, could not connect to server")

    def scanip(self, ip):
        self.ip = ip
        url = 'https://ipinfo.io/'+self.ip+'/json'
        openurl = urllib.request.urlopen(url)
        loadurl = json.load(openurl)

        for i in loadurl:
            print(i + " : " + loadurl[i])

        print(Style.BRIGHT + Fore.BLUE + "[*] Scan finished")

    def getwpv (self, link):
        try:
            self.link = link
            header = {'User-Agent' : 'Firefox'}
            petition = requests.get (url=self.link, headers=header)
            soup = BeautifulSoup(petition.text, 'html5lib')
            for v in soup.find_all ('meta'):
               if v.get('name') == 'generator'):
                      version = v.get ('content')
            
            print (version)
        except:
            print (Style.BRIGHT + Fore.RED + "[*] Error, could not get wp version")

    def scanweb(self, link):
        try:
            self.link = link
            target = requests.get(url=self.link)
            header = dict(target.headers)
            for x in header:
                print(x + " : "+header[x])

            print(Style.BRIGHT + Fore.BLUE + "[*] Scan finished")
        except:
            print(Style.BRIGHT + Fore.RED + "[*] Error, could not connect to server")
