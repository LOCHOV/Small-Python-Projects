# This script explains how the response hash is created on http-digest-authenticatino on RFC2617

# Compute digest authentication hash creation (md5)

import hashlib
'''
You can pick the data from wireshark filtering for "http" after 
you have done a loggin attempt with http-digest-authentication
hash1 is a md5 hash of: username:realm:password
'''

hash1_string = 'username:realm:password'
hash1 = hashlib.md5(hash1_string.encode('utf-8')).hexdigest()
print("hash1_ "+hash1)

# hash 2 consists of: method:URI
hash2_string = 'GET:/'
hash2 = hashlib.md5(hash2_string.encode('utf-8')).hexdigest()
print("hash2_ " + hash2)

# the result (RESPONSE) if an md5 hash that consists of:
# hash1:nonce:noncecount:clientnonce:QOP:hash2

nonce = "nonce"
noncecount = "noncec"
clientnonce = "cnonce"
qop = "auth"

response_string = hash1+":"+nonce+":"+noncecount+":"+clientnonce+":"+qop+":"+hash2
response = hashlib.md5(response_string.encode('utf-8')).hexdigest()
print("response_ "+response)

'''
it is possible to try to reverse the hash via rainbow table. 
However it's not recommendable since there is risk of MD5 collision.
'''
