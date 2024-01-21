x = [1,2,3,4,5,6,7,8]

for ele in enumerate(x):
	#prints the tuples in (index,value) format
	print(ele)
for i,v in enumerate(x):
	#prints the indexes and values in the list
	print(f"index is {i} and value is {v}")

for i,v in enumerate(x, start = 2):
	#prints the index,values where index starts with 2

	print(f"index started with {i} and value is {v}")