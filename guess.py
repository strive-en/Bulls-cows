import random

r = random.randint(1, 100)
while True:
    A = int(input("請輸入答案："))
    if A == r:
        print("你答對了！")
        break
    elif A < r:
        print("答案比較大")
    elif A > r:
        print("答案比較小")
