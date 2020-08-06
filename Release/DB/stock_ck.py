#stock_ck.py
"""
現在の在庫で何がどれだけあるか確認する
・以降のアップデートで今月やその日の出入りを表示させる
"""

path_stock = "./DB/data/okayama.stock"
path_lent = "./DB/data/lenting_out.stock"
bou = 0
net = 0
bou_lent = 0
net_lent = 0

with open(path_stock) as st:
    stock_str = [a.strip() for a in st.readlines()]
stock = [int(s) for s in stock_str]
for b in stock:
    if b < 200000:
        bou += 1
    elif b < 300000:
        net += 1

with open(path_lent) as lent:
    lend_str = [a.strip() for a in lent.readlines()]
lend = [int(s) for s in lend_str]
for b in lend:
    if b < 200000:
        bou_lent += 1
    elif b < 300000:
        net_lent += 1

print("在庫\n棒は", bou ,"本\nネットは", net ,"個")
print("\n出庫中\n棒は", bou_lent ,"本\nネットは", net_lent ,"個")
input("Press Enter...")