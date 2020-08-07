#out_input.py
"""
出ていく用
"""
import datetime
import time
import sys
now = datetime.datetime.now()


path_lent = "./DB/data/lenting_out.stock"
path_log = "./DB/log/out_" + now.strftime("%Y%m%d_%H%M%S") + ".log"
path_stock = "./DB/data/okayama.stock"
num = []
cou = 0

print("Enter で保存&終了します")

with open(path_lent) as lent:
    lend = [a.strip() for a in lent.readlines()]
with open(path_stock) as st:
    stock = [a.strip() for a in st.readlines()]
con = input("工事番号:")
if con == "":
    print("無効な値 - 終了します")
    time.sleep(2)
    sys.exit(0)

path_con = "./DB/data/construction/" + con +".stock"

while True:
    a = input("出庫-製品管理番号:")
    if a == "":
        if cou == 0:
            print("無効な値 - 終了します")
            time.sleep(2)
            sys.exit(0)
        break
    num.append(a)
    cou += 1
for a in num:
    stock.remove(a)
    lend.append(a)
    #print(a, "removing...")
    
    path_stback = ("./DB/data/stock_back/" + a + ".stock")
    
    with open(path_stback, "w") as stback:
        stback.write(con)
with open(path_lent, "w") as f:
    f.write("\n". join(lend))
with open(path_log, "w") as log:
    log.write("\n". join(num))
with open(path_stock,"w") as st_w: #追加だけにしたら処理が速くなる
    st_w.write("\n". join(stock))
with open(path_con, "a") as cons:
    cons.write("\n".join(num))
    cons.write("\n".join("\n"))

l = len(num)
print("Total %d 件　出庫しました" % (l))
print("誤りがある場合発生時刻を確認後、製作者に確認してください")
time.sleep(2)

"""
出庫
工事番号で・・・
"""