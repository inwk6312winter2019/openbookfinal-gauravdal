import string
def unique_words(book1):
	d1 = dict()
	list1 =[]
	fout = open(book1, "r")
	for line in fout:
		line = line.split()
		for index in range(0, len(line)):
			word = line[index].strip(string.whitespace + string.punctuation)
			d1[word] = d1.get(word, 0) + 1
			#gauravbamania
	for word in d1.keys():
		list1.append(word)
	return list1 

unique_words("Book1.txt")
