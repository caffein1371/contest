# ABC148
# 問題文
# 英小文字のみからなる長さ Nの文字列 S, Tが与えられます。
# Sの1文字目、Tの1文字目、Sの2文字目、Tの2文字目、Sの 3文字目、...、SのN文字目、TのN文字目というように、Sの各文字と Tの各文字を先頭から順に交互に文字を並べ、新しい文字列を作ります。この新しくできた文字列を出力してください。

N =int(input())
S,T =input().split()
for i in range(len(S)):
  print (str(S[i])+str(T[i]), end='')