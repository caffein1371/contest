# ABC56
# 問題文
# 高橋君はプログラミングコンテストサイト「ButCoder」の会員です。
# ButCoder の会員には 
# 2つのレーティング 内部レーティング と 表示レーティング が割り当てられています。
# 表示レーティングは、その会員のコンテスト参加回数が 10以上のときは内部レーティングに等しく、そうでないときは、会員のコンテスト参加回数を Kとして、内部レーティングから 100×(10−K)を引いたものになります。
# 高橋君のコンテスト参加回数が Nで表示レーティングがRであるとき、高橋君の内部レーティングを求めてください。


N,R = map(int,input().split())

if N<10:
  print(100*(10-N)+R)
else:
  print (R)