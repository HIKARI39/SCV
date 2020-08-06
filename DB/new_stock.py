#new_stock.py
"""
在庫の新規登録
"""
import datetime
import time
now = datetime.datetime.now()

path_log = "./DB/log/new_" + now.strftime("%Y%m%d_%H%M%S") + ".log"
path_stock = "./DB/data/okayama.stock"
path_history = "./DB/history/新規登録履歴.csv"
num = []

print("新規在庫登録\nEnter で保存&終了します")
print("※100000-:棒 200000-:ネット")
while True:
    a = (input("製品管理番号:"))
    if a == "":
        break
    num.append(a)
for a in num:
    with open(path_history,"a") as history:
        history.write("\n".join("\n"))
        history.write(now.strftime("%y-%m%d"))
        history.write(" ")
        history.write(a)
with open(path_stock, "a") as new:
    new.write("\n".join("\n"))
    new.write("\n".join(num))
with open(path_log, "w") as log:
    log.write("\n". join(num))

print("Total", len(num), "件　新規登録しました")
print("終了しています。データに誤りがある場合発生時刻を確認後、製作者に確認してください")
time.sleep(2)
