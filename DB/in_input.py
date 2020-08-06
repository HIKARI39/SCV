#in_input.py 
"""
戻ってきたもの用
"""
import datetime
import time
now = datetime.datetime.now()

path_lent = "./DB/data/lenting_out.stock"
path_log = "./DB/log/in_" + now.strftime("%Y%m%d_%H%M%S") + ".log"
path_stock = "./DB/data/okayama.stock"
num = []

print("Enter で保存&終了します")

with open(path_lent) as lent:
    lend = [a.strip() for a in lent.readlines()]
with open(path_stock) as st:
    stock = [a.strip() for a in st.readlines()]
while True:
    a = (input("入庫-製品管理番号:"))
    if a == "":
        break
    num.append(a)
for a in num:
    stock.append(a)
    lend.remove(a)

    path_stback = "./DB/data/stock_back/" + a + ".stock"

    with open(path_stback) as stback:
        con = stback.read()

    path_con = "./DB/data/construction/" + con +".stock"
    
    with open(path_con) as con_f:
        plu = [a.strip() for a in con_f.readlines()]
    plu.remove(a)
    with open(path_con,"w") as con_w:
        con_w.write("\n". join(plu))
    print(a, "inputted")

with open(path_stock,"w") as st_w:
    st_w.write("\n". join(stock))
with open(path_lent,"w") as lent_W:
    lent_W.write("\n". join(lend))
with open(path_log, "w") as log:
    log.write("\n". join(num))

l = len(num)
print("Total %d 件　入庫しました" % (l))
print("終了しています。誤りがある場合発生時刻を確認後、製作者に確認してください")
time.sleep(2)
"""
入庫作成完了
数字を入れるとファイルに書き込む＆バックアップでlogにも入る
空白エンターで終了
入力件数をカウントして報告
"""