from random import choice, randint
from string import ascii_letters
from itertools import cycle

##key = ''.join([choice(ascii_letters) for i in range(randint(8, 16))])
##print(key)
##
##flag = '{REDACTEd}'
####with open("flag.txt", "r") as file:
####    flag = file.read()
##
##key_gen = cycle(key) # cycle('ABCD') -> A B C D A B C D ...
##
##data = []
##for i in range(len(flag)):
##    data.append(chr(ord(flag[i]) ^ ord(next(key_gen))))
##
##with open("flag.enc", "w+") as file:
##    file.write(''.join(data))

with open("flag.enc", "r") as file:
    flag_enc = file.read()

print(flag_enc)

flag_start = 'hexCTF{'

##data = []
##for i in range(len(flag_start)):
##    data.append(chr(ord(flag_enc[i]) ^ ord(flag_start[i])))
##
##print(data) # ['J', 't', 'm', 'Z', 'z', 'C', 'J']


for a in ascii_letters:
    for u in ascii_letters:
        key = ['J', 't', 'm', 'Z', 'z', 'C', 'J']
        key.append(a)
        key.append(u)
        key_gen = cycle(key)
        data = ''
        for i in range(len(flag_enc)):
            data += (chr(ord(flag_enc[i]) ^ ord(next(key_gen))))
        if data[-1:] == '}' and '\\' not in data and '^' not in data:
            print(data + ' || ' + ''.join(key))

# hexCTF{supercaliaragilisticexpialidocious}


