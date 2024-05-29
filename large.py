test_list = [5, 6, 3, 7, 8, 1, 2, 10, 5]
indices=[3,7]

for i in sorted(indices, reverse=True):
	del test_list[i]
	
print(test_list)
