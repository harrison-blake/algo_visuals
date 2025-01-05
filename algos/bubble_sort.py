unsorted = [4, 2, 1, 782, 98, 8, 10, 101]

for i in range(len(unsorted)):
	for j in range(1, len(unsorted)-i):
		if(unsorted[j-1]>unsorted[j]):
			temp = unsorted[j]
			unsorted[j] = unsorted[j-1]
			unsorted[j-1] = temp

print(unsorted)
