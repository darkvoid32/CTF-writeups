# Shifter
> What a strange challenge...
> It'll be no problem for you, of course!
> nc misc.2020.chall.actf.co 20300

Solve 50 of these epic problems in a row to prove you are a master crypto man like Aplet123!
You'll be given a number n and also a plaintext p.
Caesar shift `p` with the nth Fibonacci number.
n < 50, p is completely uppercase and alphabetic, len(p) < 50
You have 60 seconds!
--------------------
Shift VFKGGPTEKQYCBLLONRLGWKOQCDJMAYQCNPDZQQQ by n=44:

This is what you get when you netcat to the server, which is just a normal netcat question
Creating the fibonacci sequence in this case will take too long for the 60 second time limit as I found out, so after googling around I found out that creating a list of fibonacci sequence numbers will allow me to access the numbers exponentially faster.
Since we know the upper limit of the sequence, which is less than fifty, creating a list to that limit will allow us to solve this question easily.

> actf{h0p3_y0u_us3d_th3_f0rmu14-1985098}