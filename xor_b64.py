from itertools import izip, cycle
import base64
# only Python2
# Script solving PentesterAcademy WAP Challenge 


def xor_en_de_crypt(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x, y) in izip(data, cycle(key)))


key = raw_input("encryption key: ") # for example "12345"
print("First decode base64 then XOR decrypt (1). First XOR encrypt then base64 encode (2)")
tmp = input("1/2?: ")


if tmp == 1:
    data = raw_input("Base64-encoded-string to decode: ")
    # first base64-decode the string, then XOR with the key (for example: "RVdAQA==")
    secret_data_decoded = base64.decodestring(data)
    solution = xor_en_de_crypt(secret_data_decoded, key)
    print(solution)

elif tmp == 2:
    data = raw_input("String to encode: ")
    # first XOR with the key, then base64-encode (for example: "test")
    data_encoded = xor_en_de_crypt(data, key)
    solution = base64.encodestring(data_encoded)
    print(solution)
