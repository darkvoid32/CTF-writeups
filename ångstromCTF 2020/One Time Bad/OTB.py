import random, time
import string
import base64
import os

def otp(a, b):
        r = ""
        for i, j in zip(a, b):
                r += chr(ord(i) ^ ord(j))
        print('r = ' + r)
        return r


def genSample():
        # Get random string with length 1-29 => p
        # Get random string with length p
        p = ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(random.randint(1, 30))])
        k = ''.join([string.ascii_letters[random.randint(0, len(string.ascii_letters)-1)] for _ in range(len(p))])
        print('p = ' + p)
        print('k = ' + k)
        x = otp(p, k)

        return x, p, k

# Same as OTP
def decode(a, b):
        r = ""
        for i, j in zip(a, b):
                r += chr(ord(i) ^ ord(j))
        return r

random.seed(int(time.time()))

print("Welcome to my one time pad service!\nIt's so unbreakable that *if* you do manage to decrypt my text, I'll give you a flag!")
print("You will be given the ciphertext and key for samples, and the ciphertext for when you try to decrypt. All will be given in base 64, but when you enter your answer, give it in ASCII.")
print("Enter:")
print("\t1) Request sample")
print("\t2) Try your luck at decrypting something!")

while True:
        choice = int(input("> "))
        if choice == 1:
                x, p, k = genSample()
                # Return base64 of OTP
                print(base64.b64encode(x.encode()).decode(), "with key", base64.b64encode(k.encode()).decode())
                x_enc = base64.b64encode(x.encode()).decode()
                k_enc = base64.b64encode(k.encode()).decode()
                print('PT = ' + decode(base64.b64decode(x_enc).decode('utf-8'), base64.b64decode(k_enc).decode('utf-8')))
        elif choice == 2:
                x, p, k = genSample()
                print(base64.b64encode(x.encode()).decode())
                a = input("Your answer: ").strip()
                if a == p:
                        print(os.environ.get("FLAG"))
                        break

                else:
                        print("Wrong! The correct answer was", p, "with key", k)
