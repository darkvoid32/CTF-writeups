# X0R
> XOR is best method for OTPs, especially for flags.

ZIP file they gave contains the python file and the encrypted flag

From the title of the chall we already know that we have to use XOR somehow, and since our only output is encrypted flag, we will start from there.

Reading the python file they gave we will see that they first create a key from range 8-16, with random ascii letters.

Then the key is XOR'ed with the flag, and flag.enc is our output.

From here on out what we need to do is pretty simple, retrieve the key to decrypt flag.enc, but how?

We know that the flag format is hexCTF{...}, so we will start by XOR'ing the respective chars in flag.enc.

We will yield 

> ['J', 't', 'm', 'Z', 'z', 'C', 'J']

as the first few characters of the key, but we will very quickly see that problem here.

The length of the  key is 8-16, but the key we have right now has a length of 7, so there is some more work to do.

Appending every ascii letter to brute force the flag is the way to go, but outputting the flag is going to be troublesome.

The rules I set for this is that the output must have '}' as the last character and some other minor details.

Looking through some of the output we will eventually see that appending 2 characters gives us a seemingly good output (readable), but there are so many outputs, which one is correct?

After some looking around I realise that the flag probably does not have any '_', and is probably 1 word, 1 very long word.

Googling some characters made the flag quite obvious too.

> hexCTF{supercaliaragilisticexpialidocious}