from Crypto.Cipher import AES
##from secret import flag
import time
from hashlib import md5

flag = '{FLAG_REDACT}'
key = md5(str.encode(str(int(time.time())))).digest()
padding = 16 - len(flag) % 16
aes = AES.new(key, AES.MODE_ECB)
##outData = aes.encrypt(flag + padding * hex(padding)[2:].decode('hex'))
print(padding)
print(hex(padding))
print(hex(padding)[2:])
outData = aes.encrypt(flag + padding * bytes.fromhex(hex(padding)[2:]).decode('utf8'))
print(outData.encode('base64'))


