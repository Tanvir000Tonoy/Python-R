#List
mylist = ["shimul","tanvir","bandhan","saikat"]
print(mylist) # Print the list items 
print(len(mylist)) # Print the length of this list 


#List items data types ( it can be of any data type)
mylist1 = ['shimul','tanvir','bandhan','saikat','alock'] #string type
mylist2 = [10,20,30,40,50,60] #integer type
mylist3 =[True,False,False,True] #boolean type
print (mylist1)
print (mylist2)
print (mylist3)

#Python_Access list items
print(mylist1[1]) #this is print will be tanvir 'tanvir'


#Range of indexes
print(mylist1[1:4]) #This will print items from position 1 to 4 and the item in position 4 is not included 

#Check if item exists  
if 'laow' in mylist1:
    print ("yes,'laow' is in the mylist1 list")
else:
    print ("no,'laow'is not int the mylist1 list")

#Change list item
mylist1[0]='apuuu'
print(mylist1)

#Change a range of item values
mylist1[0:2]=['apuuu','anuu']
print(mylist1)

#Insert items into the list by using insert() method
mylist1.insert(2,'boishakhi')
print(mylist1)

#Add list item by using append() method
mylist1.append('anoy')
print(mylist1)

#Append items from another list to the current list by using the extend() method
mylist4 =['habul','dabul','kabul']
mylist1.extend(mylist4)
print (mylist1)

#Remove specific item from the list,by using remove method 
mylist4.remove('dabul')
print(mylist4)
#Remove specific index item by using pop() method and del keyword
mylist1.pop(1)
print(mylist1)
del mylist1[0]
print(mylist1)

#Print all item using a for loop
for i in mylist1:
    print(i)

#Print all item using a while loop
i=0
while i<len(mylist1):
    print(mylist1[i])
    i=i+1

#List comprehension
mylist5=['python','java','php','javascript','c++']
newlist=[]
for x in mylist5:
    if 'p' in x:
        newlist.append(x)
print(newlist)

#Sort a list using sort() method
mylist5.sort()
print(mylist5)

apuurlist = [248, 578,165, 87, 53]
apuurlist.sort()
print(apuurlist)

#A case-insensitive sort function, use str.lower as a key function
thislist=['iphone','Samsung','oneplus','Xiaomi','nokia']
thislist.sort(key=str.lower)
print(thislist)

#Sort descending a list by using keyword argument reverse=True
apuurlist.sort(reverse=True)
print(apuurlist)

#Reverse the order of a list by using reverse() method
thislist.reverse()
print(thislist)

#Copy a list by using copy() method
mylist1 = ['shimul','tanvir','bandhan','saikat','alock']
mylist2 = mylist1.copy()
print (mylist2)