#!/usr/bin/env python3
import socket
import sys
from urllib.parse import urlsplit
import threading

startPort = 1
endPort = 1000
domain = None
threads = 5

totalPortsScanned = 0

def display_help():
    tool_name = "Gazillion port scanner"
    box_width = len(tool_name) + 4  

    print(f"\033[1;33m{'*' * box_width}")
    print(f"* \033[1;32m{tool_name.upper()}\033[1;33m *")
    print(f"{'*' * box_width}\033[0m")

    print("\n\033[1;36mUSAGE:")
    print(f"  python portLookup.py -t <target> -p <port or port range> -threads <number of threads>")

    print("\n\033[1;36mOPTIONS:")
    print("  -t <target>: Specify the target IP or domain name.")
    print("  -p <ports>: Specify the port or port range.")
    print("      Examples:")
    print("        - Single port or start from port 1 up to the provided port: -p 80")
    print("        - Port range: -p 80-100")
    print("  -threads, --threads <number of threads>: Specify the number of threads. [Default: 5]")
    print("  -h: Display this help message.\033[0m")

    print("\n\033[1;93mEXAMPLE:")
    print(f" \033[1;93mpython portLookup.py -t example.com -p 1000 -threads 20\033[0m")
    print(f" \033[1;93mpython portLookup.py -t example.com -p 22-5000 --threads 25\033[0m")


def portScan(ip,startPort,endPort):
	global totalPortsScanned
	if(startPort == 0):
		for port in range(endPort + 1):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(1)
			result = s.connect_ex((ip,port))
			if result == 0:
				print(f"Port {port} is open")
			s.close()
			totalPortsScanned = totalPortsScanned + 1
	else:
		for port in range(startPort, endPort + 1):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(1)
			result = s.connect_ex((ip,port))
			if result == 0:
				print(f"Port {port} is open")
			s.close()
			totalPortsScanned = totalPortsScanned + 1

def startThreading(ip,startPort,endPort):
	t = threading.Thread(target=portScan,kwargs={'ip':ip,'startPort':startPort,'endPort':endPort})
	t.start()
	return

def calculateThreads(domain,startPort,endPort,threads):
	ip = socket.gethostbyname(domain);
	print(domain, '=====>', ip);
	if threads > 1:
		totalPorts = endPort - startPort + 1
		if totalPorts > 0:
			dividedval = str(totalPorts / threads)
			splittedarr = dividedval.split('.')
			if int(splittedarr[1]) > 5:
				average = int(dividedval.split('.')[0]) + 1
			else:
				average = int(dividedval.split('.')[0])
			beginFrom = startPort
			endAt = startPort + average
			while(endAt < endPort):
				startThreading(ip,beginFrom,endAt)
				beginFrom = endAt + 1
				if(endAt + 1 + average > endPort):
					startThreading(ip,beginFrom,endPort)
					break
				else:
					endAt = endAt + 1 + average
		else:
			print("Error: No of ports is less than 0!")
			return
	else:
		startThreading(ip,startPort,endPort)



for i in range(1,len(sys.argv),2):
	if "-h" in sys.argv or "--help" in sys.argv:
		display_help()
		break
	elif sys.argv[i] == '-t':
		url_parts = urlsplit(sys.argv[i+1])
		if url_parts.netloc:
			domain = url_parts.netloc
		elif url_parts.path:
			domain =  url_parts.path
		else:
			print('Invalid domain, use -h to get the manual')
			break
	elif sys.argv[i] == '-p':
		ports = sys.argv[i+1]
		splitports = ports.split('-')
		if len(splitports) == 1:
			startPort = 1
			endPort = int(splitports[0])
		elif len(splitports) == 2:
			startPort = int(splitports[0])
			endPort = int(splitports[1])
		else:
			print("Invalid port number, use -h to get the manual")
			break
	elif sys.argv[i] == '-threads':
		threads = int(sys.argv[i+1])
	elif sys.argv[i] == '--threads':
		threads = int(sys.argv[i+1])
	else:
		print('Invalid arguments, use -h to get the manual')
		break
	if i+2 == len(sys.argv):
		print("Domain:", domain)
		print("Scanning ports:", f'{startPort} - {endPort}')
		if domain != None:
			calculateThreads(domain,startPort,endPort,threads)
		else:
			print("Domain name is incorrect, use -h to get the manual")
