from copy import deepcopy
import sys
ciphertextFile = open(sys.argv[1], "rb")
outfile = open(sys.argv[2], "wb")
cTextOriginal = bytearray(ciphertextFile.read()) #Opens files and creates buffers out of them, to be manipulated
cTextCopy = deepcopy(cTextOriginal)
cTextPos = 0
block1Pos = 0
for char in cTextOriginal:
    cTextCopy[cTextPos] = char ^ cTextOriginal[block1Pos] #XORs the first 256 blocks of ciphertext with every subsequent set 
    cTextPos += 1
    block1Pos += 1
    block1Pos %= 256 * 16 #resets the counter to stay in the first block
outfile.write(cTextCopy)
