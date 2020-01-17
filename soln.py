'''
Simple Python Program
'''

# Problem 1)

#
# Combine two lists 
#
# a = [1,3,5,7,9,11]
# b = [0,2,4,6,8,10,12]
#
# Combine to form a list c :
# c = [0,1,2,3,4,5,6,7,8,9,10,11,12]

#c=[]

#a = [1,3,5,7,9,11]
#b = [0,2,4,6,8,10,12]
#print len(a)
#print len(b)

#for i in range(len(a)):
#    for j in range(len(b)):
#	    c.append(b[j])
#	    c.append(a[i])


#print(c)


#c=[b[0],a[0],b[1],a[1],b[2],a[2],b[3],a[3],b[4],a[4],b[5],a[5],b[6]]
#print c

# Problem 2)

#
# Combine two lists' values 
#
# a = [1,3,5,7,9,11]
# b = [0,2,4,6,8,10,12]
#
# Add the values of lists a and b 
# while their indicies are the same
# to create a new list called c
 
#	
#a = [1,1,1,3,5,7,9,11]
#b = [0,2,4,6,8,10,12]	
#c=[]
#for i in range(len(a)):
#	for j in range(len(b)):
#		if i==j:
#			d = a[i]+b[j]
#			c.append(d)
#			print d


			

# Problem 3)

#
# Strings 
#
string_arr = ('141.1','1.2','1.3','1.4','1.5')
int_arr = (12,13,14,15,16)

# Make a new tuple in which each value is equal to
# string_arr/int_arr, except for the last value which is 
# equal to string_arr*int_arr

#Solution
#string_arr = ('141.1','1.2','1.3','1.4','1.5')
#int_str_arr= (int(string_arr[0]),int(string_arr[1]),int(string_arr[2]),int(string_arr[3]))

string_arr = [int(float(i)) for i in string_arr]
int_arr = list(int_arr)
c = []
for i in range(len(string_arr)-1):
	c.append(string_arr[i]/int_arr[i])
	
c.append(string_arr[i]*int_arr[i])
#c = tuple(c)
#print(c)

print(1./15)

#print int_str_arr
#int_arr = (12,13,14,15,16)

