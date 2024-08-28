my_list = []

print("This is the initial list")

my_list = [10,20,30,40]

print(my_list)

print( "This is the list after adding 15 to the second position")

my_list.insert(1,15)
print(my_list)

print("This is the list after apending the new values")

my_list.append([50,60,70])
print (my_list)

print("In this list I have removed the last element with the pop function")
my_list.pop()
print(my_list)

print("this is the sorted version of the list using the sort function")
my_list.sort()
print(my_list)

if 30 in my_list:
	x = my_list.index(30)
	print(x)
print("above is the index of 30 after looping the list and using the index() function")