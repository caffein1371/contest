S = input()

num = 753
number = []
minnum = 1000
for i,n in enumerate(S):
  number.append(n)
  if i>=2:
    print (int(''.join(number))
    if minnum > abs(int(''.join(number))-num):
      minnum = abs(int(''.join(number))-num)
    number.pop(0)
    
print (minnum)