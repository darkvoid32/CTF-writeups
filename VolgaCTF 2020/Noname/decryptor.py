import base64

with open('encrypted', 'r') as f:
    s = f.read()

ss = base64.b64decode(s).decode('latin-1')
#print(ss)

print('Block 1 : ' + ss[:16])
print('Block 2 : ' + ss[16:32])
print('Block 3 : ' + ss[32:48])
print('Block 4 : ' + ss[48:64])

# length is 64 (4 blocks of 16)
# means that ss is block 1 | block 2 | block 3 | block 4
# where ss is also flag + padding (?) / or flag + secret + padding
# we know the key is always 16 bytes

# TLDR : I think this is an ECB challenge with padding challenge with no oracle

# I suck :(

# flag - unknown
# secret - unknown
# padding - unknown (cant find because secret is unknown & cant be found)

from Crypto.Cipher import AES
from base64 import b64decode
import time
from hashlib import md5

enc = b64decode(open('encrypted').read())

for i in range(-24*60*60*6, 0):
    key = md5(str.encode(str(int(time.time()+i)))).digest()
    aes = AES.new(key, AES.MODE_ECB)
    f = aes.decrypt(enc).decode('latin-1')
    if 'Volga' in f:
        print(f)
