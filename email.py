import re
list=[]
n=int(input("enter"))
for i in range(n):
    check=input()
    mat=re.search(r'[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}',check)
    if mat!=None:
        list.append(check)
list.sort()
print(list)
      
      
