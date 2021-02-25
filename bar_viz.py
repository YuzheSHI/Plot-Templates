import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import warnings
from matplotlib import colors

matplotlib.rc("font",family='AR PL SungtiL GB')

warnings.filterwarnings('ignore')


def vis_national(national, native, null, x):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    plt.title('2018-2020年度各区县馆编目数据占比')
    years = [
        '国图编目数据库',
        '本地编目数据库',
        '无编目数据库'
    ]
    total_width, n = 0.8, len(years)
    width = total_width / n
    xx = np.arange(len(x))
    xx = xx - (total_width - width) / 2

    plt.bar(xx, national, width=width, label=years[0])
    plt.bar(xx + width, native, width=width, label=years[1])
    plt.bar(xx + 2 * width, null, width=width, label=years[2])

    plt.xticks(range(len(x)), x, rotation = 45)
    plt.ylabel('百分比(%)')
    plt.xlabel('区县图书馆')
    plt.legend(loc='best')
    plt.axhline(50, color = 'r')
    name = 'data'
    plt.savefig(name)
    return 


def book_purchase(p18, p19, p20, x):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    plt.title('2018-2020年度各区县馆中文图书入藏量')
    years = [
        '2018',
        '2019',
        '2020'
    ]
    total_width, n = 0.8, len(years)
    width = total_width / n
    xx = np.arange(len(x))
    xx = xx - (total_width - width) / 2

    plt.bar(xx, p18, width=width, label=years[0])
    plt.bar(xx + width, p19, width=width, label=years[1])
    plt.bar(xx + 2 * width, p20, width=width, label=years[2])

    plt.xticks(range(len(x)), x, rotation = 45)
    plt.ylabel('中文图书入藏量（册）')
    plt.xlabel('区县图书馆')
    plt.legend(loc='best')
    plt.axhline(20000, color = 'r')

    max18 = np.argmax(np.array(p18))
    max19 = np.argmax(np.array(p19))
    max20 = np.argmax(np.array(p20))
    plt.annotate(
        x[max18] + str(p18[max18]), 
        xy = (max18, p18[max18]), 
        bbox = dict(fc=(1,0.9,0.9))
    )
    plt.annotate(
        x[max19] + str(p19[max19]), 
        xy = (max19, p19[max19]), 
        bbox = dict(fc=(1,0.9,0.9))
    )
    plt.annotate(
        x[max20] + str(p20[max20]), 
        xy = (max20, p20[max20]), 
        bbox = dict(fc=(1,0.9,0.9))
    )
    name = 'purchase'
    plt.savefig(name)
    return 


def delay_time(delay, x):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.grid()
    plt.title('2018-2020年度各区县馆无编目数据图书平均滞后周期')
    plt.xticks(range(len(x)), x, rotation = 45)
    plt.ylabel('无编目数据图书平均滞后周期（月）')
    plt.xlabel('区县图书馆')
    # plt.legend(loc='best')
    xx = range(len(x))
    plt.plot(xx, delay, marker = 'o', markersize = 2)
    plt.axhline(3, color = 'r')
    for xxy in zip(xx, delay):
        plt.annotate(
            str(xxy[1]),
            xy = xxy,
            bbox = dict(fc=(1,0.9,0.9))
        )
    name = 'delay'
    plt.savefig(name)
    return 


if __name__ == '__main__':
    national = [
        5,
        70,
        85,
        20,
        80,
        50,
        85,
        40,
        40,
        40,
        30,
        100,
    ]
    native = [
        94,
        10,
        14,
        79,
        0,
        50,
        14,
        50,
        40,
        40,
        40,
        0,
    ]
    null = [
        1,
        20,
        1,
        1,
        20,
        1,
        1,
        10,
        20,
        20,
        30,
        0,
    ]
    p18 = [
        22299,
        76721,
        50234,
        50369,
        682,
        275,
        16381,
        56261,
        16934,
        0,
        41631,
        33474,
    ]
    p19 = [
        24528,
        28174,
        21897,
        15263,
        1500,
        2588,
        19133,
        23960,
        26385,
        0,
        58390,
        23005,
    ]
    p20 = [
        0,
        14875,
        12365,
        27157,
        0,
        3186,
        43311,
        33822,
        38390,
        44433,
        20068,
        18744,
    ]
    delay = [
        2,
        3,
        4,
        2,
        3,
        6,
        4,
        3,
        24,
        18,
        9,
        0.5,
    ]
    x = [
        '和平馆',
        '河西馆',
        '河东馆',
        '红桥馆',
        '河北馆',
        '津南馆',
        '西青馆',
        '北辰馆',
        '东丽馆',
        '宁河馆',
        '宝坻馆',
        '蓟州馆',
    ]

    vis_national(national, native, null, x)
    book_purchase(p18, p19, p20, x)
    delay_time(delay, x)