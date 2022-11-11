import random
import matplotlib.pyplot as plt


if __name__ == '__main__':

    bunkei_result = 0
    rikei_result = 0
    draw = 0
    xx = [0] *10000
    yy = [0] *10000

    N = int(input("文系と理系を戦わせる回数を整数で入力してください"))

    for i in range(N):
        # 文系チーム
        bunkei = 0
        finish_bunkei = 0
        count_bunkei = 1
        while finish_bunkei < 10:
            x = random.randint(0, 1)
            if x == bunkei:
                finish_bunkei += 1
            else:
                finish_bunkei = 0
                count_bunkei += 1
        xx[count_bunkei] += 1

        # 理系チーム
        rikei = 1
        x = 1025
        count_rikei = 0
        while (x != rikei):
            x = random.randint(1, 1024)
            count_rikei += 1
        if (count_bunkei < count_rikei):
            bunkei_result += 1
        elif (count_bunkei > count_rikei):
            rikei_result += 1
        else:
            draw += 1
        yy[count_rikei] += 1
    if (bunkei_result > rikei_result):
        result = "文系の勝利です！"
    elif (bunkei_result < rikei_result):
        result = "理系の勝利です！"
    else:
        result = "引き分けです！"
    print('今回は文系チームが{}回勝利、理系チームが{}回勝利、引き分けが{}回で、{}'.format(bunkei_result, rikei_result, draw, result))
    print(sum(xx))
    # 対象データ
    x1 = range(10000)

    # figureを生成する
    fig = plt.figure()

    # axをfigureに設定する
    ax = fig.add_subplot(1, 1, 1)

    # axesに散布図を設定する
    ax.scatter(x1, xx, c='b')
    plt.show()
    ax.scatter(x1, yy, c='b')

    # 表示する
    plt.show()
