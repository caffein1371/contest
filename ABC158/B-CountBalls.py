# ABC158
# 問題文
# 高橋君は青と赤の2色のボールを持っており、これらを一列に並べようとしています。
# 初め、列にボールはありません。
# 根気のある高橋君は、次の操作を10**100回繰り返します。

# 列の末尾に、A個の青いボールを加える。その後、列の末尾にB個の赤いボールを加える。
# こうしてできる列の先頭からN個のボールのうち、青いボールの個数はいくつでしょうか。

N,A,B = map(int,input().split())

sum = 0
#print (N//(A+B))


sum+=A*(N//(A+B))

if N%(A+B)>A:
  sum+= A
else :
  sum+= N%(A+B)
print (sum)