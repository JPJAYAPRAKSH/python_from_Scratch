#nested loops
n=int(input("Enter a number : "))
for i in range(1,n+1):
      for j in range(1,i+1):
          print("*",end=' ')
      print()
      
for i in range (n):
    for j in range(n):
        print('*',end=" ")
    print()
