import fractions
from binascii import unhexlify

def getModInverse(a, m):
    if fractions.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def main():
    p = '6359219'
    q = '151'
    e = 347 
    ct = [346046109,295161774,616062960,790750242,259677897,945606673,321883599,625021022,731220302,556994500,118512782,843462311,321883599,202294479,725148418,725148418,636253020,70699533,475241234,530533280,860892522,530533280,657690757,110489031,271790171,221180981,221180981,278854535,202294479,231979042,725148418,787183046,346046109,657690757,530533280,770057231,271790171,584652061,405302860,137112544,137112544,851931432,118512782,683778547,616062960,508395428,271790171,185391473,923405109,227720616,563542899,770121847,185391473,546341739,851931432,657690757,851931432,284629213,289862692,788320338,770057231,770121847]

    p = int(p)
    q = int(q)
    # compute n
    n = p * q
    # Compute phi(n)
    phi = (p - 1) * (q - 1)

     # Compute modular inverse of e
    d = getModInverse(e, phi)

    print("n:  " + str(d))

    s = ''
    for val in ct:
        # Decrypt ciphertext
        pt = pow(val, d, n)
        print("pt: " + str(pt))
        s += chr(pt)
        #print(unhexlify(hex(pt)))
    print(s)
    
#172070576318285777902351017014850513943749891499547486454156569029770767741

if __name__ == "__main__":
    main()
