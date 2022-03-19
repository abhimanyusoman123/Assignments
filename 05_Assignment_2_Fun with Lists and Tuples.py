
final_list = [] 
line = input("Enter the list of tuples:\n") 
while(line !=''): 
	#final_list.append(tuple(line.split()))
	final_list.append(tuple(map(int,line.split())))
	line = input() 
 
#print(final_list) 

#a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)
print(sort_list_last(final_list))

