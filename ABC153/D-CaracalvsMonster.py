H = int(input())

Alist = []
Alist.append(H)
count = 0
while len(Alist)>0:
  if Alist[0]==1:
    count+=1
    del Alist[0]
    #if len(Alist)==0:
     # break
  else:
    count+=1
    Alist.append(Alist[0]//2)
    Alist.append(Alist[0]//2)
    del Alist[0]
  
print (count)