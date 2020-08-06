#lenting_ck_one.py
"""
貸し出し中の特定の取引先を表示する
"""
con = input("調べたい工事番号を入力してください")

path_url = "./DB/data/construction/" + con +".stock"
with open(path_url) as f:
    ls_str = [a.strip() for a in f.readlines()]
ls = [int(s) for s in ls_str]
bou = 0
net = 0
for i in ls:
    if i < 200000:
        bou += 1
    elif i < 300000:
        net += 1
print("\n", con,"> 棒は",bou,"個　ネットは",net,"枚\n")
input("Press Enter...")