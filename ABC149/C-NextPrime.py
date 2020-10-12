X = int(input())

map = 100004


while True:
  if X%2!=0 and X%3!=0 and X%5!=0 and X%7!=0:
    break
  X+=1

print (X)