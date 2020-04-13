# RSAPWN
> We must train the next generation of hackers.

> nc challenges.tamuctf.com 8573

> We must train future hackers to break RSA quickly. Here is how this will work.
> I will multiply together two big primes (<= 10000000), give you the result,
> and you must reply to me in less than two seconds telling me what primes I
> multiplied.

The number they set is usually close to 100000000000000, i.e. 99997320006931, and the primes are close to 10000000, i.e. 9999971 & 9999761.
Hence finding the lowest prime number does not work well here, since they are so similar, and normal prime factor functions take longer than 2 seconds.
Seeing this I tried to create a work around by assuming all prime factors in this case is close to 10000000.
So starting with 10000000 and slowly decreasing till I find the prime. I thought you had to give a couple of examples for the flag but apparently once is enough

> gigem{g00d_job_yOu_h4aaxx0rrR}