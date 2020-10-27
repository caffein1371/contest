import itertools
import math

N= int(input())
place =[]
for i in range(N):
  placelist = list(map(int,input().split()))
  place.append(placelist)
  
ans = 0
count =0
for i in itertools.permutations(place, r=N):
  print (i)
  print (i[0])
  print (i[2][0])
  print ("{} {}".format(i[0][0],i[1][0]))#x
  print ("{} {}".format(i[0][1],i[1][1]))#x
  
  #print ("{} {}".format(i[0][1],i[1][1]))#y
  #print ("{} {}".format(i[0][1],i[1][1]))#y
  #print (math.sqrt(((i[0][0]-i[1][0])*(i[0][0]-i[1][0]))))
  ans+= math.sqrt(((i[0][0]-i[1][0])*(i[0][0]-i[1][0])+(i[0][1]-i[1][1])*(i[0][1]-i[1][1])))
  count+=1
  
print (count)
print (ans)
print (ans/count)
  