# pxpa
Plaintext Xor Plaintext Analyzer

## Purpose
Some flawed crypto implementations or attacks (namely, nonce reuse) can result in an unusual scenario where blocks of plaintext are XOR'd with themselves or other subsequent blocks.

These blocks are still very difficult to decipher directly but are clearly not a secure cipher.

I've seen a few research papers on the subject, but there does not yet appear to be a program of this type available widely.

## Method
I'm currently using what amounts to a brute force method for the moment, which is not very efficient. I have the wordlist from [first20hours](https://github.com/first20hours/google-10000-english), and it iterates over the file to located plaintexts that align exactly e.g. an 8 letter word will match with other 8 letter words if they align exactly between plaintexts.

This has two primary problems. It doesn't work very well (matches are highly infrequent) and it's very, very slow. 

This is not a good method, and natural language processing seems to be the way forward. 
