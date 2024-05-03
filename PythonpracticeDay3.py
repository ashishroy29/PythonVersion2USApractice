## There is another type of collection we all can create that is tuple
## What is tuple?
## how it is going to work and what kind of data you can store inside a tuple.
## What kind of a data manipulation we can perform in terms/respect of tuple

## It is like a list but not exactly a list
## It is a type collection of datatype where we will be able to hold multiple elements, and the notation is curly brackets ()


t = (1,2,3,4,5)

type(t)

t1 = ("Ashish", 345, 45+8j, 535.43,True) #Tuple

l = ["Ashish", 345, 45+8j, 535.43,True] #List

type(l)

#### 1st Difference is that each of these elements are represented by different brackets

t2 = ()

type(t2)

l

l[0:2]

t1[0:2]

t1[::-1]

t1[-1]

t1[::-1]

l

l1 = [4,5,6,7]

l1[0] = 'ashish'
l1

t1 = 'kumar'

t1[0] = 'kimar'

# Tuples is nothing but immutable collection, It does not support item assignment

a = 'ashi'

a[0] = 'b'

#In tuples it wont work at all,they are immutable objects

t1

t2 = (23,34,5,67,7)

t1 + t2 #here it is just concatinating (this is something kind of a append operation)

l+l1

t1*2

t1

t1.count('Ashish')

l.index('Ashish')

l

t1.index('Ashish') #it basically tells us the first occurance of any elements inside a collection


## when do we use tuples?

## when do we use list?

## For data security, wherever we need to create an element
## Where someone will not be able to access, in that case we use tuples

## Example ::

## Gmail Account, Facebook, applications etc

## we keep on changing password, if we dont want anyone to access any location and change it we use tuples so that no one will be able to change it any point of a time

## Anywhere where we have a fixed size of collections, that is called as tuples, because it never supports append, expand etc

t = (34,34,54,67,8,8,3,(1,2,3,4),'Ashi')

type(t) # the above is called as nested tuple and it is possible to do so

t[7][0]


t1 = ([1,2,3,4,5], ('Sd',56,4),'Sda')

t1[0][2] = 'ASHI'
t1

t1[1][1] = 'Ashi'

t1[0] = '1as'

t1[0]

## It is a set of collection.
## what is set and how is it different from others

l = [1,2,3,4,5,56,3,4,45,5,6,67,7,8,4,34,3,3,2]

##can you please try remove duplicate element
## here we can see that we were able to remove all the duplicates
set(l)


# Remove all the duplicate and give the 2nd max number

New_list = list(set(l))
print(New_list)

Max_list = max(New_list)
print(Max_list)

for i in New_list:
    if i >= Max_list:
        pass
    elif i < Max_list:
        zz = [i]
else:
        pass

Second_Largest = zz[-1]
Second_Largest


#Another Easy way to do this
# Original list with duplicates
l = [1, 2, 3, 4, 5, 56, 3, 4, 45, 5, 6, 67, 7, 8, 4, 34, 3, 3, 2]

# Remove duplicates and convert to a list
New_list = list(set(l))

# Sort the list in descending order
New_list.sort(reverse=True)

# Get the second largest element
Second_Largest = New_list[1]

print("Original list:", l)
print("List without duplicates:", New_list)
print("Second largest element:", Second_Largest)

##can you please try remove duplicate element
## here we can see that we were able to remove all the duplicates
set(l)


#Set is a collection which will try to remove all the duplicate element by itself

## Creating a set
s = {}


type(s)


s1 = {2,3,4}

type(s1)

#When we have not used any kind of an element and we have used only curly bracket(it is a Dictionary)
#When we have used curly bracket and we have some unique Non duplicate element its called as set


s2 = {1,1,2,2,23,2,3,4,4,4,4,4,}

s2 #By default it is removing a duplicate element, because it is the property of set

type(s2)

s2[0]

#slicing is not allowed in set, it is a unordered collection, it is not possible to get any indexes


s2 = list(s2)
s2
s2[1]


s2
s2 = {1,1,2,2,23,2,3,4,4,4,4,4,}

s2.add(122324) #adding few elements into the system

s2

s2.add("asds")

s2

s2.add('asds')

s2

type(s2)

s2[0]


s2.add([1,2,3,4,4]) #List is not available inside a set. (It is different in case of set)

{[1,2,2,3,3,3],3,3,3,3,3,} #set always hold unordered collection of unique elements, it can only holt primitive dataset


{(1,2,2,3,3,3),3,3,3,3,3,}


# Tuple is subscrible
#t is not going to allow any sort of mutable type inside a set but it allows immutable inside the set such as tuples

{(1,2,2,3,3,3),(1,2,2,3,3,3),3,3,3,3,3} #It is going to remove the duplicate of tuples.

s = {(1,2,2,3,3,3),(1,2,2,3,3,3),3,4,5,6,7}

s.remove(3) #it removes the element 3

s

s.discard(5) #it removes the element 5

s

#Difference between remove and discard

s.remove(45) #it is not present ,so it gives key error.

s.discard(45) #the def says if it is not a member then do nothing so thats why no error and it executes

{'sudh','Sudh'} #set is a case sensitive element

#whereever we want to eliminate the duplicates we go-ahead and use set, we pass the set, These comes under NLP section

s = {4,5,6,7,8,8,9,34,34,43,4,5,6,7,7,'ashi','deepak','deepak'}


s

# DICTIONARY

# It is another type of collection where we will be able to hold any number of elements and where we will be able to access it.

# We can store things in key and value pair

d = {}

type(d)

d = {2,2,3}

type(d)

# we can compare this to an oxford dictionary (There should be a word and meaning)

d = {4:'sudh'}

d


#here 4 is a key and 'sudh is value pair'

d1 = {"Key1":12345, "Key2" : 'Ashi', 'Key3': [2,3,4,5,6]}

d1

d1 = {"Key1":12345, "Key2" : 'Ashi', 45: [2,3,4,5,6]}

d1


l  = [2,3,4,5,6,6] 

d1


#how to access 3 our of this dictinary
l[1]

d1['Key1']

d1[45][0]


d1['Key2'][0]


#Dictionary is another type of a collection which holds data, in Key value fashion

#Properties


d = {3 : ['asdasds','dasdasd',2,1,3,4,5,6,7]}


#d = {@ : ['asdasds','dasdasd',2,1,3,4,5,6,7]}#It dosent work with special case character

d = {.4 : ['asdasds','dasdasd',2,1,3,4,5,6,7]} # it works as it is a decimal character

d = {'Ashi' : 'asdasds'} # it works with a string value

d = {'Ashi' : ['asdasds',12,3,4]} # it works with a List value


d = {'KEY': (2,3,4,5,6)} #it works with a Tuple value
d['KEY'][0]



d = {'KEY': {2,3,4,5,6}} #it works with a set Value

## The Difference between a set and a curly braces are whenever we are trying to create a dictionary, we are supposed to create a key and value pair,
## if not created then it wont create a dictionary, in set yes you can create a value but it will create in a unique elements

d1 = {"key1" : [2,3,4,5] , "key2" : "sudh", "key1" : 45} #here are duplicates of key1, what value will it come

d1['key1'] # Key 1 is a repeated one and key1 is repeated and it assigns the latest value


# Key value should not be duplicate, if duplicated then it only holds the recent one rather than the old value, Key should be unique at any point of the time
# is it possible to create a duplicate indexes? no , its a unique, but in pandas series chapter it is possible


d1 = {"key1" : [2,3,4,5] , "key2" : [2,3,4,5], "key1" : 45} #here the values can be same but not the keys, here it will not give any error but it will update the value.

d1 = {"key1" : [2,3,4,5] , "key2" : [2,3,4,5], "John" : 45} 

d1["John"]

# Creating a dictionary

d = {'Name': 'Ashish',
     "Mobile_No" : 1233445,
     'mail_id': 'ashishroyofficial@gmail.com',
     'Key1':[1,2,3,4,5,5],
     "key2":(12,3,4,5,6,7),
     "key3":{2,2,3,4,5,6},
     "key4":{2:2,3:5}
    }

d['key3']

type(d['key3'])

d['key4']

type(d['key4'])

d['key4'][3] #this is a slicing operation


d.keys() #try to find list of all the keys

d.values() #trying to find the list of all the values

d.items() #to access all the items, heere we will get key value pair, as a list of a tuples.

type(d.items())

d = {'key1' : 'sudh', "key2" : [1,2,3,4,5]}

d

#Adding new key , or new values for new key
d['key3'] = 'kumar'

d

d[4] = [1,2,3,4,56]

d

d['key1'] = 'ashashdhasdh'

d

#Deleting the key value, we cannot change the key value
del d['key1']

d

# creating another dictionary
d1 = {'key1':'sudh','key2':[3,4,5,6,6,7]}

d1[[1,2,3]] = 'ineuron' #Key as a list is not going to work

d1[(1,2,3)] = 'ineuron' #key as a tuple is going to work


d1 #key is supposed to be a immutable element

d1.get('key1') #if there is a value then it gives out the value of the key

d1 = {'key1':"ineuron","key":'FSDS'}

d2 = {'key2':456,'key3':[2,2,2,2,]}

d1.update(d2) #it has updated d1 with d2, it has basically combined it, this is kind of a append function

d1

d2

d1+d2 #it works in list, it doesent work in dictionary although it is homogenious statement

d1

d2

d1

key = ('name','mobile_no','email_id')
value = "sudh"

d = d1.fromkeys(key,value) # it will map and create a new dictionary for us

d
