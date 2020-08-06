#delete_stock.py
"""
削除用
ただし、在庫にないと消せない
"""
import datetime
import time
now = datetime.datetime.now()


path_log = "./DB/log/del_" + now.strftime("%Y%m%d_%H%M%S") + ".log"
path_stock = "./DB/data/okayama.stock"
path_history = "./DB/history/廃棄履歴.csv"
num = []
print("在庫削除\nEnter で保存&終了します")

with open(path_stock) as st:
    stock = [a.strip() for a in st.readlines()]
while True:
    a = (input("廃棄の製品管理番号:"))
    if a == "":
        break
    num.append(a)
input("本当に削除しますか？ Please press Enter...")
for a in num:
    stock.remove(a)
    with open(path_history,"a") as history:
        history.write("\n".join("\n"))
        history.write(now.strftime("%y-%m%d"))
        history.write(" ")
        history.write(a)
    print(a, "was deleted")

with open(path_stock, "w") as st_w:
    st_w.write("\n".join(stock))
with open(path_log, "w") as log:
    log.write("\n". join(num))

print("終了しています。誤りがある場合発生時刻を確認後、製作者に確認してください")
time.sleep(2)