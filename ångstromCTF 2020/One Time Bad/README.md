# one time bad
> My super secure service is available now!
> Heck, even with the source, I bet you won't figure it out.
> nc misc.2020.chall.actf.co 20301

This is a One Time Pad challenge, and from wikipedia you can see the conditions for OTP to be perfect :
>  If the key is (1) truly random, (2) at least as long as the plaintext, (3) never reused in whole or in part, and (4) kept completely secret, then the resulting ciphertext will be impossible to decrypt or break.

We know the conditions 2-4 is met by reading the source code, the key is randomly generated to the length of the plaintext. But condition 1, however is not.
Since the random seed is generated using
> random.seed(time.time())

We can abuse it by similarly calling random.seed(time.time()) to hopefuly get the same seed when we netcat to the server
Though I cannot get the same seed perfectly 100% since I got lazy, running the program a couplf of times will result in that happening
The result is just inversing what the XOR operations done
