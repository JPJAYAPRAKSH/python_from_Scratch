"""
List in python
-> one variable can store n numbers of values
-> [] sqaure brackets were used to define list
->( , ) is used seperate values within in list
-> Array homogenous ( store one of data type per variable)
-> List is hetrogeneous ( can store different types of vairiables)
note : python have only list
"""

lst_cs=["hi",10,20,30]
print(lst_cs)
print(lst_cs[0])#Forward indexing
print(lst_cs[-1])#reverse indexing
lst1=[1,2,3]
lst2=[4,5,6]
lst3=lst1+lst2
print(lst3)# list concatenation
lst3=lst2+lst1
print(lst3)#result have precedence
lst3=lst1*5#list Replication
print(lst3)
"""
#List methods
#len()--> print the length of the list
print(len(lst3))
#append()--> used to insert value at last position of the list
lst1.append(4)
print(lst1)
#extend()--> used to insert more than one element to the list
lst1.extend(lst2)# ==> lst1=lst1+lst2
print(lst1)
#insert()--> used to map the value where to be add within in the element
lst1.insert(0,0)
print(lst1)
lst1=[1,2,3]
lst1.append(lst2)# list can take any type of input. a list within another list is said to be nested list
print(lst1)
print(lst1[3])
#clear--> used to clear the value within the list
lst3.clear()#empty list
print(lst3)
#count--> used to print total number of same element within a list
lst0=[1,1,1,2,3,4,5]
print(lst0.count(1))
#index()--> used to print the index of a value # pass element of list which want the index value
print(lst0.index(1))#print first occurance of a index value ignore others
print(lst0.index(5))
lst1=[1,2,3,4,5,6]
#min()--> used to print minimum value of list
print(min(lst1))
#max()--> used to print maximum value of list
print(max(lst1))
lst=[3,2,1,4,5,6]
print("Before sorting",lst)
lst.sort()#ascending order
print("After sorting",lst)
lst.sort(reverse=True)
print("Desecding sorting",lst)
#sum()--> used to sum of the list elements
print(sum(lst))
#mutability
lst[0]=1000
print(lst)
#pop()--> used to remove the last element of the list
lst.pop()
print(lst)
lst.pop(1)# index value used to remove the desired element from the list
print(lst)
#remove()--> the element of the list is passed as argument which will be remove from the list
lst.remove(1000)
print(lst)
lst=[[1,2,3],[4,5,6]]
print(lst[0][0])
print(lst[1][2])
print(lst[-1][-1])
"""

