tup=(170,180,190,1000)
print(type(tup))
print(tup[0])#indexing
#tup[1]=100# type error
#tup=(170,100,190,1000)
#len
print(len(tup))
#max,min
print(min(tup))
print(max(tup))
#count
print(tup.count(170))
print(tup.index(1000))
lst=list(tup)
print(lst)
print(type(lst))
tup1=tuple(lst)
print(tup1)
print(type(tup1))
num=(9)#it consider expression
print(type(num))
num=(9,)
print(type(num))
print(tup+tup1+num)
