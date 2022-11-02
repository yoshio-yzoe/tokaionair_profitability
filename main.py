import random
import sys


def yes_no_input():
    while True:
        choice = input("途中結果を表示する場合はyesを、表示しない場合はNoを入力してください").lower()
        if choice in ['y', 'ye', 'yes', 'Yes', 'YES']:
            return True
        elif choice in ['n', 'no', 'No', 'NO']:
            return False


if __name__ == '__main__':
    YN = yes_no_input()

    # 文系チーム
    bunkei = int(input("文系チームの検証です。0か1か好きな値を入力してください"))
    if (bunkei < 0) or (bunkei > 1):
        print("無効な値です")
        sys.exit()
    finish_bunkei = 0
    count_bunkei = 1
    while finish_bunkei < 10:
        if YN == True:
            print("{}回目の".format(count_bunkei))
        x = random.randint(0, 1)
        if x == bunkei:
            finish_bunkei += 1
            if YN == True:
                print("{}回目 : ".format(finish_bunkei))
                print(x)
        else:
            if YN == True:
                print("{}回目 : ".format(finish_bunkei))
                print(x)
            finish_bunkei = 0
            count_bunkei += 1

    print('文系チームの検証が終了しました。今回の記録は {} 回でした'.format(count_bunkei))

    # 理系チーム
    rikei = int(input("理系チームの検証です。1~1024の間の整数で好きな数字を入力してください"))
    if (rikei < 1) or (rikei > 1024):
        print("無効な値です")
        sys.exit()
    x = 1025
    count_rikei = 0
    while (x != rikei):
        x = random.randint(1, 1024)
        count_rikei += 1
        if YN == True:
            print("{} : {}回目".format(x, count_rikei))

    print('理系チームの検証が終了しました。今回の記録は {} 回でした'.format(count_rikei))
    if (count_bunkei < count_rikei):
        result = "文系チームの勝利です!"
    elif (count_bunkei > count_rikei):
        result = "理系チームの勝利です!"
    else:
        result = "引き分けです!"
    print('今回は文系チームが{}回、理系チームが{}回で、{}'.format(count_bunkei, count_rikei, result))