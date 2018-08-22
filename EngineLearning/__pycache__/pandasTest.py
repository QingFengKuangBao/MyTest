import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 线状图  plt.plot


def tes_plot():
    x = np.linspace(-np.pi*4, np.pi*4, 100)
    y = np.sin(x)

    # 设置x轴的刻度
    plt.xticks(np.arange(-np.pi*4, np.pi*5, np.pi*2),
               [r"$-4π$", r"$-2π$", r"$0$", r"$2π$", r"$4π$"])
    # plt.yticks([0.2,0.7,0.9],["不及格 0.2","及格0.7","优秀0.9"])

    # 获取边框
    ax = plt.gca()
    # 设置上右边的边框为不显示
    ax.spines['right'].set_color("none")
    ax.spines['top'].set_color("none")

    # 将x y轴与下 左边框绑定
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    # 移动 x y 轴 的位置
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    # 设置 XY 轴的名称
    # plt.xlabel("x轴")
    # plt.ylabel("Y轴")

    plt.plot(x, y, "r-", label="sinX")

    # 以点的形式显示
    # plt.scatter(x, y,label="sinX")

    # 图例legend   label图例的名称
    # y2=np.cos(x)
    # plt.plot(x, y2,"g-",label="cosX")
    # # legend显示图例 legend(handles=,labels=,loc='best')
    plt.legend()

    # 添加注解 annotate  text
    x0 = np.pi
    y0 = np.sin(x0)
    plt.scatter(x0, y0)
    plt.annotate("$(π,0)$", xy=(x0, y0), xycoords="data",
                 xytext=(+5, +5), textcoords="offset points", fontsize=12)
    plt.text(3, 1, "这是sinX", fontsize=15)

    # 对label的样式进行修改 facecolor整体颜色   edgecolor边框颜色   alpha透明度
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(10)
        label.set_bbox(dict(facecolor='black', edgecolor="None", alpha=0.2))

    plt.show()


# 散点图  plt.scatter
def test_scatter():
    n = 102
    x = np.random.rand(n)
    y = np.random.rand(n)
    cValue = ['r', 'y', 'g']
    # cValue=np.random.rand(n)
    plt.scatter(x, y, c=cValue, edgecolors="None", s=70, alpha=0.6)
    plt.show()


# 柱状图  plt.bar
def test_bar():
    n = 10
    x = np.arange(1, n+1)
    y = np.random.rand(n)
    y1 = -y
    ax = plt.gca()
    # 设置上右边的边框为空
    ax.spines['right'].set_color("none")
    ax.spines['top'].set_color("none")

    # bar 柱状图
    plt.bar(x, y, edgecolor="red", alpha=0.6)
    plt.bar(x, y1, facecolor='red', alpha=0.6)
    plt.xticks(x)
    for X, Y in zip(x, y):
        plt.text(X, Y+0.02, "%.2f" % (Y), ha="center", va="bottom")
    for X, Y in zip(x, y1):
        plt.text(X, Y-0.02, "%.2f" % (Y), ha="center", va="top")
    plt.show()


# 等高线实例   plt.contour   contourf
def test_meshgrid():
    def f(x, y):
        return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

    n = 400
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)

    # 生成网格点
    X, Y = np.meshgrid(x, y)
    print(X.shape)
    print(Y.shape)
    print(f(X,Y).shape)
    # plt.xticks(())
    # plt.yticks(())

    # 填充颜色
    plt.contourf(X, Y, f(X, Y), 15, alpha=0.7, cmap=plt.cm.get_cmap("rainbow"))

    # 线条
    C = plt.contour(X, Y, f(X, Y), 15, colors="black", linewidths=0.5)

    # 添加标签数字
    plt.clabel(C, inline=True, fontsize=10)

    plt.show()

# imshow  colorbar
def test_img():
    i = np.array([0.313660827978, 0.365348418405, 0.423733120134,
                  0.365348418405, 0.439599930621, 0.525083754405,
                  0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)
    # img操作
    plt.imshow(i, interpolation="none", cmap="hot", origin="upper", aspect=1)

    # 图例 colorbar
    plt.colorbar()

    plt.xticks(())
    plt.yticks(())
    plt.show()


# 3D  plot_surface  ax = Axes3D(fig)
from mpl_toolkits.mplot3d import Axes3D
def test_3d():
    fig = plt.figure()
    ax = Axes3D(fig)
    # XY轴
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2+2*Y**2)
    # Z轴
    Z = np.sin(R)
    # 画出3d plot_surface
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap(
        "rainbow"), edgecolor="black", linewidths=0.5)

    ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap="rainbow")

    ax.set_zlim(-2, 2)
    plt.show()

# 子图 subplot


def test_subplot():
    plt.figure()
    # 一个figur画四副图
    # plt.subplot(2,2,1)
    # plt.plot([0,2],[0,2])
    # plt.subplot(2,2,2)
    # plt.plot([0,2],[0,2])
    # plt.subplot(2,2,3)
    # plt.plot([0,2],[0,2])
    # plt.subplot(2,2,4)
    # plt.plot([0,2],[0,2])

    # 第一幅占一整行
    plt.subplot(2, 1, 1)
    plt.plot([0, 2], [0, 2])
    # 第二行画两幅
    plt.subplot(2, 2, 3)
    plt.plot([0, 2], [0, 2])
    plt.subplot(2, 2, 4)
    plt.plot([0, 2], [0, 2])

    plt.show()


def test_subplot2grid():
    plt.figure()
    # shape figure如何进行分割  loc起始位置   colspan rowspan占多少行列 默认为1
    ax1 = plt.subplot2grid(shape=(3, 3), loc=(0, 0), colspan=3, rowspan=1)
    ax1.plot([0, 2], [0, 2])
    ax1.set_title("ax01")
    ax2 = plt.subplot2grid(shape=(3, 3), loc=(1, 0), colspan=2, rowspan=1)
    ax3 = plt.subplot2grid(shape=(3, 3), loc=(1, 2), colspan=1, rowspan=2)
    ax4 = plt.subplot2grid(shape=(3, 3), loc=(2, 0))
    ax5 = plt.subplot2grid(shape=(3, 3), loc=(2, 1))
    plt.show()


import matplotlib.gridspec as gridspec


def test_gridspec():
    plt.figure()
    gs = gridspec.GridSpec(3, 3)
    ax1 = plt.subplot(gs[0, :])
    ax2 = plt.subplot(gs[1, :2])
    ax3 = plt.subplot(gs[1:, 2])
    ax4 = plt.subplot(gs[2, 0])
    ax5 = plt.subplot(gs[2, 1])
    plt.show()


def test_subplots():
    # ax是一个2x2的二维数组
    fg, ax = plt.subplots(2, 2, sharex=True, sharey=False)
    for a in ax:
        for a0 in a:
            a0.plot([0, 1], [0, 1])
    plt.show()


# 图中图 通过定位来确定图的位置
def test_addaxes():
    fig = plt.figure()
    x = [1, 2, 3, 4, 5]
    y = [1, 8, 5, 9, 4]

    # 确定所画图的位置
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax1 = fig.add_axes([left, bottom, width, height])
    ax1.plot(x, y, 'r')
    ax1.set_title("indside")

    # 方法1
    left, bottom, width, height = 0.12, 0.7, 0.15, 0.15
    ax2 = fig.add_axes([left, bottom, width, height])
    ax2.plot(x, y, 'b')
    ax2.set_title("indside01")

    # 方法2
    left, bottom, width, height = 0.7, 0.15, 0.15, 0.15
    plt.axes([left, bottom, width, height])
    plt.plot(x, y, 'y')
    plt.title("indside02")

    plt.show()


# 双y轴
def test_twins():
    x = np.arange(1, 10, 0.2)
    y1 = x**2
    y2 = np.sin(x)

    fig, ax1 = plt.subplots()

    # ax2为ax1的X镜像
    ax2 = ax1.twinx()

    ax1.plot(x, y1, "r-")
    ax2.plot(x, y2, "g-")
    ax1.set_xlabel("X轴")
    ax1.set_ylabel("Y", color="r")
    ax2.set_ylabel("Y2", color="g")

    plt.show()


# 动画
from matplotlib import animation


def test_animation():
    fig, ax = plt.subplots()
    x = np.arange(0, np.pi*2, 0.2)
    line, = ax.plot(x, np.sin(x))

    # 图像如何变化的方法  i=[1,frames]
    def annimat(i):
        line.set_ydata(np.sin(x+i/30))
        return line,

    # 图像初始的样式
    def init():
        line.set_ydata(np.sin(x))
        return line,

    ani = animation.FuncAnimation(
        fig, func=annimat, frames=200, init_func=init, interval=10)

    plt.show()


def draw_ball(r=2,center= [2,2,2]):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Make data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)

    # 
    x = 5 * np.outer(np.cos(u), np.sin(v))+5
    y = 5 * np.outer(np.sin(u), np.sin(v))+5
    z = 5 * np.outer(np.ones(np.size(u)), np.cos(v))+5
    # x**2+y**2+z**2是一个固定的值
    print((x-5)**2+(y-5)**2+(z-5)**2)
    # Plot the surface
    ax.plot_surface(x, y, z, cmap="rainbow")
    ax.contourf(x, y, z, zdir="z", offset=0, cmap="rainbow")

    plt.show()






if __name__ == "__main__":
    # tes_plot()
    # test_scatter()
    # test_bar()
    # test_img()
    test_meshgrid()
    # test_3d()

    # 子图
    # test_subplot()
    # test_subplot2grid()
    # test_gridspec()
    # test_subplots()
    # 图中图
    # test_addaxes()
    # 双Y轴
    # test_twins()

    # test_animation()
    # draw_ball()
    pass
