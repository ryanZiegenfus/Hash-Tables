import hashlib

key = b"str"


for i in range(10):
    print(hashlib.sha256(key))