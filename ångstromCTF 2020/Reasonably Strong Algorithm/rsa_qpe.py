import fractions
from binascii import unhexlify


# https://www.alpertron.com.ar/ECM.HTM
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

def long_to_bytes (val, endianness='big'):
    """
    Use :ref:`string formatting` and :func:`~binascii.unhexlify` to
    convert ``val``, a :func:`long`, to a byte :func:`str`.

    :param long val: The value to pack

    :param str endianness: The endianness of the result. ``'big'`` for
      big-endian, ``'little'`` for little-endian.

    If you want byte- and word-ordering to differ, you're on your own.

    Using :ref:`string formatting` lets us use Python's C innards.
    """

    # one (1) hex digit per four (4) bits
    width = val.bit_length()

    # unhexlify wants an even multiple of eight (8) bits, but we don't
    # want more digits than we need (hence the ternary-ish 'or')
    width += 8 - ((width % 8) or 8)

    # format width specifier: four (4) bits per hex digit
    fmt = '%%0%dx' % (width // 4)

    # prepend zero (0) to the width, to zero-pad the output
    s = unhexlify(fmt % val)

    if endianness == 'little':
        # see http://stackoverflow.com/a/931095/309233
        s = s[::-1]

    return s

def main():
    p = "13 536574 980062 068373".replace(" ", "")
    q = "9 336949 138571 181619".replace(" ", "")
    e = 65537
    ct = 13612260682947644362892911986815626931

    p = int(p)
    q = int(q)
    # compute n
    n = p * q
    # Compute phi(n)
    phi = (p - 1) * (q - 1)

     # Compute modular inverse of e
    d = getModInverse(e, phi)

    print("n:  " + str(d))

    # Decrypt ciphertext
    pt = pow(ct, d, n)
    print("pt: " + str(pt))
    print('pt_byte: ' + str(long_to_bytes(pt)))

#172070576318285777902351017014850513943749891499547486454156569029770767741

if __name__ == "__main__":
    main()


#!/usr/bin/python
## RSA - Given p,q and e.. recover and use private key w/ Extended Euclidean Algorithm - crypto150-what_is_this_encryption @ alexctf 2017
# @author intrd - http://dann.com.br/ (original script here: http://crypto.stackexchange.com/questions/19444/rsa-given-q-p-and-e)
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

##import binascii, base64
##
##p = 13536574980062068373
##q = 9336949138571181619
##e = 65537
##ct = 13612260682947644362892911986815626931
##
##def egcd(a, b):
##    x,y, u,v = 0,1, 1,0
##    while a != 0:
##        q, r = b//a, b%a
##        m, n = x-u*q, y-v*q
##        b,a, x,y, u,v = a,r, u,v, m,n
##        gcd = b
##    return gcd, x, y
##
##n = p*q #product of primes
##phi = (p-1)*(q-1) #modular multiplicative inverse
##gcd, a, b = egcd(e, phi) #calling extended euclidean algorithm
##d = a #a is decryption key
##
##out = hex(d)
##print("d_hex: " + str(out));
##print("n_dec: " + str(d));
##
##pt = pow(ct, d, n)
##print("pt_dec: " + str(pt))
##
##out = hex(pt)
####out = str(out[2:-1])
##print("flag")
##print(bytes.fromhex(out).decode('utf-8'))
