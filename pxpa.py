import sys

def run(text, blocksize, wordfile):
	fw = open(wordfile,"r")
	words = fw.read().split('\n')
	offsets = setOffsets(words)
	fp = open(text, "rb")
	plaintext = fp.read()
	fw = open("out1.txt", "w")
	fm = open("out2.txt", "w")
	for word in words:
		print(word)
		match = traverse(word, words, plaintext, offsets)
		if match:
			fm.write(match)
			fw.write(word)
		else:
			fm.write('x' * len(word))
			fw.write('x' * len(word))
	
def setOffsets(words):
	offsets = []
	offsets.append(0)
	length = len(words[0])
	for i in range(0, len(words)):
		if length != len(words[i]):
			offsets.append(i)
			length = len(words[i])
	return offsets

def matchWord(c, word, words, offsets):
	length = len(word)
	index = 0
	while len(words[offsets[index]]) != length:
		index += 1
	start = offsets[index]
	end = offsets[index+1]
	sublist = words[start:end]
	pWord = xorBytes(word, c).decode("utf8")
	print(pWord)
	if pWord in sublist:
		return pWord
	else:
		return None

def xorBytes(a,b):
	c = bytearray([])
	for byte in range(0, len(b)):
		c.append(a[byte] ^ b[byte])
	return c


def traverse(word, words, plaintext, offsets):
	length = len(word)
	a = bytearray(word,'utf8') #drop newline
	for i in range(0, len(plaintext)):
		b = bytearray(plaintext[i:i+length])
		c = xorBytes(a,b)
		if any(val > 122 or val < 65 for val in c):
			continue
		else:
			print("match check")
			print(a)
			print(b)
			print(c)
			match = matchWord(c, a, words, offsets)
			if match != None:
				print("match at ", i, ": " + word + " with " + match)		
	return match


if __name__ == "__main__":
	run(sys.argv[1], sys.argv[2], sys.argv[3])
