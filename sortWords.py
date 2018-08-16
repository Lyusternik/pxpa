

fp = open("words.txt", "r")
fo = open("sWords.txt", "w")
words = fp.readlines()
words.sort(key=lambda a : 1/len(a))
for word in words:
	print(word)
	fo.write(word)
