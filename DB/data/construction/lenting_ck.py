#/data/construction/lenting_ck.py
"""
貸し出し中の取引先一覧を表示する
"""
from glob import glob
import os
print("貸し出し中の取引先を表示します")
count = 0
count_item = 0
for file in glob("./DB/data/construction/*.stock"):
    if os.path.getsize(file) == 0: #空のファイルの削除（これで処理を軽くする）
        os.remove(file)
    with open(file) as f:
        ls_str = [a.strip() for a in f.readlines()]
    ls = [int(s) for s in ls_str]
    bou = 0
    net = 0
    for i in ls:
        if i < 200000:
            bou += 1
        elif i < 300000:
            net += 1
    
    count += 1
    count_item += bou + net
    print("\n",count,"件目　",file,"> 棒は",bou,"個　ネットは",net,"枚\n")
print(count,"件の取引先 >  全部で",count_item,"個 貸し出しています")
input("Press Enter...")