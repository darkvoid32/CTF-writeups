# Wacko Images
> How to make hiding stuff a e s t h e t i c? And can you make it normal again? enc.png image-encryption.py
> The flag is actf{x#xx#xx_xx#xxx} where x represents any lowercase letter and # represents any one digit number.

The image is just a bunch of random gibberish obviously, however we do have the encryption script to reverse.
The only encrypting part of the script is the line :

> pixel[i] = pixel[i] * key[i] % 251

Since I got lazy I decided to just brute force this as there are only 255 numbers to check.
> if ((n * key[i]) % 251 == pixel[i]):
> 	pixel[i] = n

If the number n, from 1 - 255 matches the above condition we know the n is the correct number. This will give us the decrypted image : 

> actf{m0dd1ng_sk1llz}