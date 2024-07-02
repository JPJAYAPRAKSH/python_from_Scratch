#empty statements
if 5==5:
    pass
print("true block skipped and here continue")
for i in range(1,11):
     pass
print("Code block skipped and here continue")
#jump statements
for i in range(1,11):
    if i==5:
        continue#skip the current iteration and move to next iteration
    print(i)
for i in range(1,11):
    if i==5:
        break#control flow jump to next block code
    print(i)
print("break statement , here passed the control flow")
