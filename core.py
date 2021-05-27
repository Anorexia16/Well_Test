from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy import stats as st
import pandas as pd
import numpy as np
import random

if Axes3D:
    pass


class Node:
    def __init__(self, x, y, z, c):
        self.x = x
        self.y = y
        self.z = z
        self.c = c

    @classmethod
    def dots_sets(cls, x, y, z, c, n, dis):
        return [Node(x * random.uniform(1 - dis, 1 + dis), y * random.uniform(1 - dis, 1 + dis),
                     z * random.uniform(1 - dis, 1 + dis), c) for _ in range(n)]


def plot_rec(ax: plt.Axes, x, y, width, height, backcolor, edgecolor, text=None):
    a, b, c, d = (x - width / 2, y + height / 2), (x + width / 2, y + height / 2), \
                 (x - width / 2, y - height / 2), (x + width / 2, y - height / 2)
    ax.plot(np.linspace(a[0], b[0], 100), np.linspace(a[1], b[1], 100), c=edgecolor)
    ax.plot(np.linspace(a[0], c[0], 100), np.linspace(a[1], c[1], 100), c=edgecolor)
    ax.plot(np.linspace(c[0], d[0], 100), np.linspace(c[1], d[1], 100), c=edgecolor)
    ax.plot(np.linspace(b[0], d[0], 100), np.linspace(b[1], d[1], 100), c=edgecolor)
    ax.fill_between([x - width / 2, x + width / 2], y - height / 2, y + height / 2,
                    facecolor=backcolor, alpha=0.7)
    if text is not None:
        ax.text(x - width / 3, y, text, fontsize=12)
    plt.show()


def plot_cube(ax, center, long):
    vertex = [(center[0] - pow(-1, i) * long / 2, center[1] - pow(-1, int(i / 2)) * long / 2,
               center[2] - pow(-1, int(i / 4)) * long / 2) for i in range(8)]
    edge_sets = [(0, 1, 3, 2), (4, 5, 7, 6), (0, 2, 6, 4), (1, 3, 7, 5), (0, 1, 5, 4), (2, 3, 7, 6)]
    faces = [[vertex[vert_id] for vert_id in edge] for edge in edge_sets]
    x, y, z = zip(*vertex)
    ax.scatter(x, y, z, c='darkblue')
    ax.add_collection3d(Poly3DCollection(faces, facecolors='snow', linewidths=1, alpha=0.3))
    ax.add_collection3d(Line3DCollection(faces, colors='k', linewidths=0.5, linestyles=':'))


def plot_norm(ax: plt.Axes, xl: float, xr: float, arr: float, c: str):
    ax.set_xlim(xl, xr)
    ax.set_ylim(-0.04, 0.6)
    x = np.linspace(xl, xr, 1000)
    y = st.norm.pdf((x-arr)/((xr-xl)/6))
    ax.plot(x, y, c=c)
    ax.fill_between(np.linspace(xl, xr, 1000), 0, y, facecolor=c, edgecolor=None, alpha=0.7)
    height = max(y)
    ax.plot((xl, arr), (0, 0), color='#000435')
    ax.plot((arr, arr), (0, height), color='#000435')
    ax.plot((arr, xr), (height, height), color='#000435')


def plot_poly6(ax: plt.Axes, x, y, dist, c):
    length = 2*dist/np.sqrt(3)
    dot = ((x - dist, y - length/2), (x, y - length), (x+dist, y-length/2),
           (x + dist, y + length/2), (x, y + length), (x-dist, y+length/2))
    [ax.plot([dot[i][0], dot[(i+1) % 6][0]], [dot[i][1], dot[(i+1) % 6][1]], c='royalblue', alpha=0.3) for i in range(6)]
    ax.fill_between(np.linspace(x-dist, x, 1000),
                    y - length/2 - (np.linspace(0, dist, 1000) / np.sqrt(3)),
                    y + length/2 + (np.linspace(0, dist, 1000) / np.sqrt(3)),
                    facecolor=c, edgecolor=None, alpha=0.45)
    ax.fill_between(np.linspace(x, x + dist, 1000),
                    y - length + (np.linspace(0, dist, 1000) / np.sqrt(3)),
                    y + length - (np.linspace(0, dist, 1000) / np.sqrt(3)),
                    facecolor=c, edgecolor=None, alpha=0.45)


def prove1():
    fig = plt.figure(figsize=(18, 12))
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.ion()
    plt.pause(4)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    df = pd.read_csv(r'./source/Finite_Radius(Infinite)/sample72.txt', header=0, sep=' ')
    df = df.drop(0, axis=0)
    df = df.drop(df.shape[0], axis=0)
    na = np.array([*[df[df.columns[i]] for i in range(4)]]).astype('float64').T
    plt.style.use('ggplot')
    show = True
    # phase1
    ax1 = fig.add_subplot(221)
    ax1.set_xticklabels(['', "1E-3", "0.01", "0.1", "1", "10", "100"])
    ax1.set_yticklabels(['', '0.3', '1', '3', '10', '30', '100', '300', '1E3', '3E3'])
    ax2 = fig.add_subplot(223)
    ax3 = fig.add_subplot(122, projection='3d')
    ax2.grid(False)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.set_xticklabels(['' for _ in range(len(ax2.get_xticks()))])
    ax2.set_yticklabels(['' for _ in range(len(ax2.get_yticks()))])
    ax2.spines['top'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.set_title('Decision Tree Algorithm ---- CART')
    ax3.set_xlim((0.6, 0.8))
    ax3.set_ylim((0.7, 0.9))
    ax3.set_zlim((0.5, 0.8))
    ax3.grid()
    ax3.set_xticks(range(6))
    ax3.set_yticks(range(6))
    ax3.set_zticks(range(6))
    ax3.set_xticklabels(["{:.2f}".format(0.6 * (0.2 * i) + 0.8 * (1 - 0.2 * i)) for i in range(6)])
    ax3.set_yticklabels(["{:.2f}".format(0.7 * (1 - 0.2 * i) + 0.9 * (0.2 * i)) for i in range(6)])
    ax3.set_zticklabels(["{:.2f}".format(0.5 * (1 - 0.2 * i) + 0.8 * (0.2 * i)) for i in range(6)])
    for i in range(12):
        ax1.cla()
        ax1.grid(True)
        ax1.scatter(np.log10(na[:, 0]), np.log10(na[:, 1]), c='#01f9c6', s=10, marker='x', alpha=0.4)
        ax1.scatter(np.log10(na[:, 2]), np.log10(na[:, 3]), c='#de0c62', s=10, marker='o', alpha=0.4)
        show = 1 - show
        if show:
            ax1.scatter(np.log10(na[33, 2]), np.log10(na[33, 3]), c='g', s=40)
            ax1.scatter(np.log10(na[40, 2]), np.log10(na[40, 3]), c='g', s=40)
            ax1.scatter(np.log10(na[57, 2]), np.log10(na[57, 3]), c='g', s=40)
        ax1.set_xlabel("Time[gr]", fontsize=16)
        ax1.set_xticklabels(['', "1E-3", "0.01", "0.1", "1", "10", "100"])
        ax1.set_yticklabels(['', '0.3', '1', '3', '10', '30', '100', '300', '1E3', '3E3'])
        ax1.set_ylabel("Pressure difference[psi]", fontsize=16)
        plt.pause(0.1)
        plt.show()
    plt.pause(6)
    # phase2
    x1, y1 = np.log10(na[33, 2]), np.log10(na[33, 3])
    x2, y2 = np.log10(na[40, 2]), np.log10(na[40, 3])
    x3, y3 = np.log10(na[57, 2]), np.log10(na[57, 3])
    xar = (x1 + x2 + x3) / 3
    yar = (y1 + y2 + y3) / 3
    step = 10
    for i in range(step + 1):
        ax1.cla()
        ax1.grid(True)
        ax1.set_xlabel("Time[gr]", fontsize=16)
        ax1.set_ylabel("Pressure difference[psi]", fontsize=16)
        ax1.text(xar * 1.05, yar * 1.05, "拐点数：2 驻点数：1\n另一条线的关键点数为0", fontsize=14)
        ax1.scatter(np.log10(na[:, 0]), np.log10(na[:, 1]), c='#01f9c6', s=10, marker='x', alpha=0.4)
        ax1.scatter(np.log10(na[:, 2]), np.log10(na[:, 3]), c='#de0c62', s=10, marker='o', alpha=0.4)
        ax1.scatter(i * xar / step + (1 - i / step) * x1, i * yar / step + (1 - i / step) * y1, c='m', s=30)
        ax1.scatter(i * xar / step + (1 - i / step) * x2, i * yar / step + (1 - i / step) * y2, c='g', s=30)
        ax1.scatter(i * xar / step + (1 - i / step) * x3, i * yar / step + (1 - i / step) * y3, c='m', s=30)
        ax1.set_xticklabels(['', "1E-3", "0.01", "0.1", "1", "10", "100"])
        ax1.set_yticklabels(['', '0.3', '1', '3', '10', '30', '100', '300', '1E3', '3E3'])
        plt.pause(0.03)
        plt.show()
    plt.pause(6)
    # phase3:
    for i in range(13):
        ax2.cla()
        ax2.grid(False)
        ax2.spines['top'].set_visible(False)
        ax2.spines['bottom'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.set_xticks([])
        ax2.set_yticks([])
        ax2.set_title('Decision Tree Algorithm ---- CART')
        ax2.text(0.4, 0.85, s='直线1 拐点数量', fontsize=12)
        [plot_rec(ax2, 0.2 + 0.2 * j, 0.75, 0.2, 0.15,
                  '#ff073a' if (i < 2 and i == j) or (i >= 2 and j == 2 and i % 2 == 0) else '#04d9ff',
                  '#5606e9', '      ' + str(j)) for j in range(4)]
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        plt.pause(0.15)
        plt.show()
    for i in range(11):
        ax2.cla()
        ax2.grid(False)
        ax2.spines['top'].set_visible(False)
        ax2.spines['bottom'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.set_title('Decision Tree Algorithm ---- CART')
        ax2.set_xticks([])
        ax2.set_yticks([])
        ax2.text(0.4, 0.85, s='直线1 拐点数量', fontsize=12)
        [plot_rec(ax2, 0.2 + 0.2 * j, 0.75, 0.2, 0.15,
                  '#ff073a' if j == 2 else '#04d9ff',
                  '#5606e9', '      ' + str(j)) for j in range(4)]
        ax2.text(0.4, 0.57, s='直线1 驻点数量', fontsize=12)
        ax2.arrow(0.6, 0.65, -0.15, -0.1, fc='#014d4e', ec='#014d4e', width=0.005)
        [plot_rec(ax2, 0.1 + 0.8 / 6 + 0.8 * j / 3, 0.45, 0.8 / 3, 0.15,
                  '#ff073a' if (i < 1 and i == j) or (i >= 1 and j == 1 and i % 2 == 1) else '#04d9ff',
                  '#5606e9', '      ' + str(j)) for j in range(3)]
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        plt.pause(0.15)
        plt.show()
    for i in range(9):
        ax2.cla()
        ax2.grid(False)
        ax2.spines['top'].set_visible(False)
        ax2.spines['bottom'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.set_xticks([])
        ax2.set_yticks([])
        ax2.set_title('Decision Tree Algorithm ---- CART')
        ax2.text(0.4, 0.85, s='直线1 拐点数量', fontsize=12)
        [plot_rec(ax2, 0.2 + 0.2 * j, 0.75, 0.2, 0.15,
                  '#ff073a' if j == 2 else '#04d9ff',
                  '#5606e9', '      ' + str(j)) for j in range(4)]
        ax2.text(0.4, 0.57, s='直线1 驻点数量', fontsize=12)
        ax2.arrow(0.6, 0.65, -0.15, -0.1, fc='#014d4e', ec='#014d4e', width=0.005)
        [plot_rec(ax2, 0.1 + 0.8 / 6 + 0.8 * j / 3, 0.45, 0.8 / 3, 0.15,
                  '#ff073a' if j == 1 else '#04d9ff',
                  '#5606e9', '      ' + str(j)) for j in range(3)]
        ax2.text(0.4, 0.27, s='直线2 关键点数', fontsize=12)
        ax2.arrow(0.47, 0.35, -0.2, -0.1, fc='#014d4e', ec='#014d4e', width=0.005)
        [plot_rec(ax2, 0.2 + 0.2 * j, 0.15, 0.2, 0.15,
                  '#ff073a' if j == 0 and i % 2 == 0 else '#04d9ff',
                  '#5606e9', '      ' + str(j)) for j in range(4)]
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        plt.pause(0.15)
        plt.show()

    plt.pause(6)
    # phase 4:
    sets1 = Node.dots_sets(0.56 * 5, 0.64 * 5, 0.68 * 5, 'royalblue', 20, 0.4)
    sets2 = Node.dots_sets(0.53 * 5, 0.612 * 5, 0.68 * 5, 'royalblue', 50, 0.2)
    sets5 = Node.dots_sets(0.55 * 5, 0.622 * 5, 0.71 * 5, 'royalblue', 12, 0.1)
    sets6 = Node.dots_sets(0.59 * 5, 0.72 * 5, 0.68 * 5, 'royalblue', 12, 0.3)
    sets7 = Node.dots_sets(0.23 * 5, 0.33 * 5, 0.32 * 5, 'fuchsia', 8, 0.25)
    sets8 = Node.dots_sets(0.09 * 5, 0.287 * 5, 0.26 * 5, 'fuchsia', 12, 0.2)
    sets9 = Node.dots_sets(0.86 * 5, 0.876 * 5, 0.73 * 5, 'lime', 17, 0.2)
    sets3 = Node.dots_sets(0.14 * 5, 0.2 * 5, 0.3 * 5, 'fuchsia', 61, 0.3)
    sets4 = Node.dots_sets(0.9 * 5, 0.9 * 5, 0.7 * 5, 'lime', 45, 0.1)
    for i in range(7):
        ax3.cla()
        ax3.grid()
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets1]
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets2]
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets3]
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets4]
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets5]
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets6]
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets7]
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets8]
        [ax3.scatter(i.x, i.y, i.z, c=i.c, marker='o', alpha=0.4) for i in sets9]
        ax3.set_xlim((0.6, 0.8))
        ax3.set_ylim((0.7, 0.9))
        ax3.set_zlim((0.5, 0.8))
        ax3.set_xticks(range(6))
        ax3.set_yticks(range(6))
        ax3.set_zticks(range(6))
        plot_cube(ax3, (0.16 * 5, 0.3 * 5, 0.3 * 5), 1.2 * (1 + (6 - i) / 20))
        plot_cube(ax3, (0.88 * 5, 0.89 * 5, 0.72 * 5), 1.4 * (1 + (6 - i) / 20))
        plot_cube(ax3, (0.55 * 5, 0.62 * 5, 0.7 * 5), 2 * (1 + (6 - i) / 20))
        ax3.set_xticklabels(["{:.2f}".format(0.6 * (0.2 * i) + 0.8 * (1 - 0.2 * i)) for i in range(6)])
        ax3.set_yticklabels(["{:.2f}".format(0.7 * (1 - 0.2 * i) + 0.9 * (0.2 * i)) for i in range(6)])
        ax3.set_zticklabels(["{:.2f}".format(0.5 * (1 - 0.2 * i) + 0.8 * (0.2 * i)) for i in range(6)])
        plt.pause(0.02)
        plt.show()
    plt.pause(np.inf)


def prove2():
    fig = plt.figure(figsize=(18, 12))
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.ion()
    plt.pause(4)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    df = pd.read_csv(r'./source/Finite_Radius(Infinite)/sample72.txt', header=0, sep=' ')
    df = df.drop(0, axis=0)
    df = df.drop(df.shape[0], axis=0)
    na = np.array([*[df[df.columns[i]] for i in range(4)]]).astype('float64').T
    plt.style.use('ggplot')
    ax1 = fig.add_subplot(322)
    ax2 = fig.add_subplot(324)
    ax3 = fig.add_subplot(326)
    ax4 = fig.add_subplot(221)
    ax5 = fig.add_subplot(223)
    ax4.plot(np.log10(na[:, 0]), np.log10(na[:, 1]), 'None')
    ax4.plot(np.log10(na[:, 2]), np.log10(na[:, 3]), 'None')
    xl, yl = ax4.get_xlim(), ax4.get_ylim()
    plt.show()
    for i in range(10):
        ax1.cla()
        ax2.cla()
        ax3.cla()
        ax4.cla()
        ax5.cla()
        ax1.set_xlabel('k(md)')
        ax1.set_ylabel('distribution')
        plot_norm(ax1, 0, 40, 13.6, '#2ee8bb')
        ax2.set_xlabel('D(m)')
        ax2.set_ylabel('distribution')
        plot_norm(ax2, 0, 100, 47.3, '#fe46a5')
        ax3.set_xlabel('N(stb/d)')
        ax3.set_ylabel('distribution')
        plot_norm(ax3, 10, 1080, 694, '#65fe06')
        ax4.cla()
        ax4.set_xticklabels(['', "1E-3", "0.01", "0.1", "1", "10", "100"])
        ax4.set_yticklabels(['', '0.3', '1', '3', '10', '30', '100', '300', '1E3', '3E3'])
        ax4.set_xlim(xl)
        ax4.set_ylim(yl)
        ax4.plot(np.log10(na[:, 0][:int(na.shape[0] * (i + 1) / 10)]),
                 np.log10(na[:, 1][:int(na.shape[0] * (i + 1) / 10)]), c='m')
        ax4.plot(np.log10(na[:, 2][:int(na.shape[0] * (i + 1) / 10)]),
                 np.log10(na[:, 3][:int(na.shape[0] * (i + 1) / 10)]), c='orange')
        ax4.set_xlabel("Time[gr]", fontsize=16)
        ax4.set_xticklabels(['', "1E-3", "0.01", "0.1", "1", "10", "100"])
        ax4.set_yticklabels(['', '0.3', '1', '3', '10', '30', '100', '300', '1E3', '3E3'])
        ax4.set_ylabel("Pressure difference[psi]", fontsize=16)
        plot_poly6(ax5, -0.15, 1.72, 0.36, '#a9f971')
        plot_poly6(ax5, 0.45, 1.9, 0.27, '#ff0490')
        plot_poly6(ax5, 1.4, 1.9, 0.33, '#fdee73')
        ax5.set_title('Approaching Algorithm: Inverse Vichte --- Gradient Descent', fontsize=12)
        ax5.plot(np.log10(na[:, 0]), np.log10(na[:, 1]), 'm:')
        ax5.plot(np.log10(na[:, 2]), np.log10(na[:, 3]), c='orange', linestyle=':')
        ax5.set_xlim(*ax4.get_xlim())
        ax5.set_ylim(*ax4.get_ylim())
        ax5.set_xticks(ax4.get_xticks())
        ax5.set_yticks(ax4.get_yticks())
        ax5.set_xticklabels(ax4.get_xticklabels())
        ax5.set_yticklabels(ax4.get_yticklabels())
        ax5.set_xlabel(ax4.get_xlabel())
        ax5.set_ylabel(ax4.get_ylabel())
        plt.pause(0.05)
        plt.show()
    plt.pause(10)
    situation = [[21.7, 47.3, 694, -0.15, 1.7, 0.36, 0.45, 1.96, 0.27, 1.42, 1.9, 0.33],
                 [21.7, 67.3, 694, -0.13, 1.83, 0.336, 0.57, 1.99, 0.26, 1.46, 1.86, 0.32],
                 [21.7, 67.3, 540, -0.13, 1.83, 0.34, 0.56, 2.02, 0.253, 1.46, 1.91, 0.32],
                 [18.7, 67.3, 540, -0.12, 1.86, 0.28, 0.54, 2.05, 0.25, 1.52, 1.84, 0.31],
                 [18.7, 57.3, 540, -0.13, 1.94, 0.25, 0.54, 2.09, 0.24, 1.52, 1.84, 0.31],
                 [18.7, 57.3, 570, -0.12, 1.94, 0.22, 0.54, 2.13, 0.2, 1.58, 1.79, 0.29],
                 [20, 57.3, 570, -0.11, 1.97, 0.13, 0.57, 2.17, 0.14, 1.63, 1.73, 0.19],
                 [20, 60.0, 570, -0.105, 2.01, 0.1, 0.57, 2.22, 0.11, 1.67, 1.67, 0.13],
                 [20, 60.0, 600, -0.094, 2.1, 0.07, 0.58, 2.26, 0.08, 1.7, 1.72, 0.08]]
    for i in range(9):
        ax1.cla()
        ax2.cla()
        ax3.cla()
        ax5.cla()
        ax1.set_xlabel('k(md)')
        ax1.set_ylabel('distribution')
        plot_norm(ax1, 0, 40, situation[i][0], '#2ee8bb')
        ax2.set_xlabel('D(m)')
        ax2.set_ylabel('distribution')
        plot_norm(ax2, 0, 100, situation[i][1], '#fe46a5')
        ax3.set_xlabel('N(stb/d)')
        ax3.set_ylabel('distribution')
        plot_norm(ax3, 10, 1080, situation[i][2], '#65fe06')
        plot_poly6(ax5, situation[i][3], situation[i][4], situation[i][5], '#a9f971')
        plot_poly6(ax5, situation[i][6], situation[i][7], situation[i][8], '#ff0490')
        plot_poly6(ax5, situation[i][9], situation[i][10], situation[i][11], '#fdee73')
        ax5.plot(np.log10(na[:, 0]), np.log10(na[:, 1]), 'm:')
        ax5.plot(np.log10(na[:, 2]), np.log10(na[:, 3]), c='orange', linestyle=':')
        ax5.set_xlim(*ax4.get_xlim())
        ax5.set_ylim(*ax4.get_ylim())
        ax5.set_xticks(ax4.get_xticks())
        ax5.set_yticks(ax4.get_yticks())
        ax5.set_title('Approaching Algorithm: Inverse Vichte --- Gradient Descent', fontsize=12)
        ax5.set_xticklabels(ax4.get_xticklabels())
        ax5.set_yticklabels(ax4.get_yticklabels())
        ax5.set_xlabel(ax4.get_xlabel())
        ax5.set_ylabel(ax4.get_ylabel())
        plt.pause(0.8)
        plt.show()

    plt.pause(np.inf)
