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

def starts_with_vow(list1):
	total_list = []
	len_vow_list = []
	for list in list1:
		for word in list:
		vow_lists = []
			if(word.startswith(("a","e","i","o","u"))):
				vow_lists.append(word)
		totat_list.append(vow_lists)
	for list in total_list:
		len_vow_list.append(len(list))
		print("here")
	return len_vow_list
 

list1 = read_by_words("Book1.txt","Book2.txt","Book3.txt")
starts_with_vow(list1)


