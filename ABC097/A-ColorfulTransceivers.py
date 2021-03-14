a,b,c,d = map(int,input().split())

if c-a<=d:
  pirnt('Yes')
elif c-b <=d and b-a<=d:
  print ('Yes')
else:
  print ('No')