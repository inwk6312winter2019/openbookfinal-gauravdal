import string

def read_by_words(*args):
	list1 = []
	for arg in args:
		list1.append(unique_words(arg))
	return list1
	
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

def count_the_article(lists):
	len_list =[]
	for list1 in lists:
		 len_list.append(len(list1))
	return len_list1
lists = read_by_words("Book1.txt","Book2.txt","Book3.txt")
count_the_article(lists)

