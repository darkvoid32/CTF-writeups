# Reasonably Strong Algorithm
> RSA strikes again!

Generic RSA question
> n : 126390312099294739294606157407778835887
> e : 65537
> c : 13612260682947644362892911986815626931

Plugging n into alpertron will immediately return p and q. After getting p and q just the other variables

> phi = (p-1) * (q-1) 
> d = modInverse(e, phi)
> pt = pow(ct, d, n)

pt is a bytearray. Deciphering will return 

> actf{10minutes}