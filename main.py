"""Disclaimer: This script should NEVER be utilized for malicious purposes. This has been created to help learn.
This script will not get past 2FA and Captcha. Most apps will lock out an account after a certain amount of failed
attempts. This script will not bypass that."""

import requests
from termcolor import colored

# User provided information
URL = input("[+] Provide Target App URL--> ")
FILE = input("[+] Provide name of the file you want to scan--> ")

# Create a list of all of the different directory names provided from the file
with open(FILE, "r") as files:
	file_names = files.readlines()
	print(colored(f"[+] Currently compiling list of directory names. Total = {len(file_names)}..."), "blue")
	print(colored("[+] Beginning scan of directories..."), "blue")
# Loop through each directory combination and listen for a response back
r = []
for f in file_names:
	file = f.strip()
	full_path = f"{URL}/{file}"
	try:
		response = requests.get(f"http://{full_path}")
	except requests.exceptions.ConnectionError:
		pass
	if response:
		print(colored(f"[+] Directory Discovered at ----> {full_path}"), "green")
		r.append(full_path)

if not response:
	print(colored("No directories located based on file provided and URL. Please try again. Exiting program."), "red")
