N,M = map(int,input().split())
temp = 0
one = []
two = []
three = []
for i in range(M):
  s,c = map(int,input().split())
  if s == 1:
    #temp+=c*100
    one.append(c)
  elif s == 2:
    #temp+=c*10
    two.append(c)
  elif s == 3:
    #temp+=c
    three.append(c)
one = list(set(one))
two = list(set(two))
three = list(set(three))

#print (one)
#print (two)
#print (three)

#print (len(one))
#print (len(two))
#print (len(three))

if len(one)==0:
  one.append(0)
if len(two)==0:
  two.append(0)
if len(three)==0:
  three.append(0)

if len(one)>=2 or len(two)>=2 or len(three)>=2:
  print (-1)
elif one[0]==0 and two[0]==0 and three[0]==0:
  print (-1)
else:
  print (one[0]*100+two[0]*10+three[0])