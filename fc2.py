x = ['a', 'b', 'a', 'a', 'c', 'c', 'q', 'q']

def list_counter(list):
	dict = {}
	for i in list:
		if i in dict:
			dict[i] = dict[i] + 1
		else:
			dict[i] =1
	return dict

print (list_counter(x))# python-2

# I CHANGED THIS SHIT YO