def checklist(List,i,ans):
  print ('i='+str(i))
  #print (List[i])
  if i+1<len(List):
    if List[i+1]<=List[i]:
      ans +=1
      return checklist(List,i+1,ans+1)
    else:
      print (ans)
      return ans
  else:
    print (ans)
    return ans

N = int(input())
Hlist = list(map(int,input().split()))
print (len(Hlist))

maxnum = 0
for i in range(len(Hlist)):
  ans =0
  checklist(Hlist,i,ans)
  #print (ans)
  if maxnum<=ans:
    maxnum =ans
print (maxnum)