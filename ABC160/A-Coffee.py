# 問題文
# ある長さ 6の英小文字からなる文字列がcoffeeに似ているとは、3文字目と 4文字目が等しく、
# 5文字目と 6文字目も等しいことを言います。与えられる文字列 Sがcoffeeに似ているか判定してください。

S = input()

Ans = "No"
if S[2]==S[3] and S[4]==S[5]:
  Ans = "Yes"
print (Ans)