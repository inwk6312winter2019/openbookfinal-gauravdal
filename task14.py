import string

def read_by_words(*args):
	list1 = []
	for arg in args:
		list1.append(character_word_count(arg))
	return list1

def character_word_count(book1):
	d1 = dict()
	list1 =[]
	fout = open(book1, "r")
	for line in fout:
		line = line.split()
		for index in range(0, len(line)):
			word = line[index].strip(string.whitespace + string.punctuation)
			d1[word] = d1.get(word, 0) + 1
			#gauravbamania
	return d1

dictionaries = read_by_words("Book1.txt","Book2.txt","Book3.txt")
#print(dictionaries)
