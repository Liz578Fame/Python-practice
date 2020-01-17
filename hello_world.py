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





# +,-,*,/

# Problem 3)

#
# Strings 
#
# string_arr = ('141.1','1.2','1.3','1.4','1.5')
# int_arr = (12,13,14,15,16)

# Make a new tuple in which each value is equal to
# string_arr/int_arr, except for the last value which is 
# equal to string_arr*int_arr

# Logic operators

# is equal     ==
# not equal    !=
# less than    <
# greater than >

# in          lists/tuples

# Combining logical operators

# not
# and 
# or


#print(4 > 10 or 5 > 3)


#if(x < 0):
#	print('X is less than 0')
#elif(x == 0):
#	print('X is equal to 0')
#elif(x > 0):
#	print('X is greater than 0')

#print(6%5)


# * : multiplication
# / : division
# + : addition
# - : subtraction



def x(number):
    '''
    Description : A function which prints the input
    '''
    if(not isinstance(number,int) and not isinstance(number,float)):
        return False
    y = int(number)
    return y
    
	
y = x('asdf')

if(not y):
	print("The program has failed on line 97")


#Convert strings to lists
values = '190.33 139402.29 2490.489 49042.84'

arr_vales = values.split(' ')
arr_vales = [float(i) for i in arr_vales]
print(arr_vales)





### Programming practice

# Fib. function

# def fib(n):

# Returns a list of all the values for the nth value in
#the fibbinocci series upto and including n
#
# n = 7
# y = fib(n)
# print(y)
# output : [1,1,2,3,5,8,13]





# Fizzbuzz
# 
# def fizzbuzz(n)
#
# Returns a list of the fizzbuzz values for
# the positive integer n
# if evenly divisible by 3 : fizz
# if evenly divisible by 5 : buzz
# if evenly divisible by 3 and 5 : fizzbuzz
# else just the normal number

# y = fizzbuzz(5)
# print(y)
# 
# output : [1,2,fizz,4,buzz]
#
# y = fizzbuzz('dfskl')
# print(y)
# output : False
#
# y = fizzbuzz('5')
# print(y)
#
# output : [1,2,fizz,4,buzz]



































