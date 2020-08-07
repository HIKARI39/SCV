#delete_stock.py
"""
削除用
ただし、在庫にないと消せない
"""
import datetime
import time
import sys
now = datetime.datetime.now()


path_log = "./DB/log/del_" + now.strftime("%Y%m%d_%H%M%S") + ".log"
path_stock = "./DB/data/okayama.stock"
path_history = "./DB/history/廃棄履歴.csv"
num = []
cou = 0
print("在庫削除\nEnter で保存&終了します")

with open(path_stock) as st:
    stock = [a.strip() for a in st.readlines()]
while True:
    a = (input("製品管理番号:"))
    if a == "":
        if cou == 0:
            print("無効な入力 - 終了します")
            time.sleep(2)
            sys.exit(0)
        break
    num.append(a)
    cou += 1
#input("本当に削除しますか？ Please press Enter...")
for a in num:
    stock.remove(a)
    with open(path_history,"a") as history:
        history.write("\n".join("\n"))
        history.write(now.strftime("%y-%m%d"))
        history.write(" ")
        history.write(a)
    #print(a, "was deleted")

with open(path_stock, "w") as st_w:
    st_w.write("\n".join(stock))
with open(path_log, "w") as log:
    log.write("\n". join(num))
print(cou,"件廃棄しました")
print("終了しています。誤りがある場合発生時刻を確認後、製作者に確認してください")
time.sleep(2)