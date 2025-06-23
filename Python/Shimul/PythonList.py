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
