import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import os
import re

globals()['interface'] = True
globals()['pic1'] = True
if globals().get("interface") is not None:
    import interface
else:
    global interface


def text_writer(**kwargs):
    pass
    # print(''.join(["{}:{}\n".format(i, kwargs[i]) for i in kwargs.keys()]))
    # print("K = {}md".format(random.uniform(1, 40)))
    # print("D = {}m".format(random.randint(10, 200)))


def log_plot(df: pd.DataFrame, **kwargs):
    plt.cla()
    plt.grid(True)
    plt.scatter([np.log10(float(i)) for i in df[df.columns[0]]], [np.log10(float(i)) for i in df[df.columns[1]]],
                c='b', s=20, marker='s')
    plt.scatter([np.log10(float(i)) for i in df[df.columns[2]]], [np.log10(float(i)) for i in df[df.columns[3]]],
                c='r', s=20, marker='o')
    plt.xlabel("Time[gr]", fontsize=16)
    plt.ylabel("Pressure difference[psi]", fontsize=16)
    if globals()['pic1'] is True:
        plt.savefig(r'./bin/fig2.png')
    else:
        plt.savefig(r'./bin/fig1.png')
    text_writer(**kwargs)


def text_inner(path, **kwargs):
    path = ''.join(path.split('\n')[:])
    path = ''.join(path.split(' ')[:])
    df = pd.read_csv(path, sep=' ')
    df = df.drop(0, axis=0)
    df = df.drop(df.shape[0], axis=0)
    if not re.match(r'\(Radius\)', path) is not None:
        kwargs["boundary type"] = "radius"
    elif not re.match(r'\(Singal_fault\)', path) is not None:
        kwargs["boundary type"] = "radius"
    elif not re.match(r'\(Infinite\)', path) is not None:
        kwargs["boundary type"] = "radius"
    if not re.match(r'Infinite_Conductivity_fracture', path) is not None:
        kwargs["well type"] = "Infinite Conductivity Fracture"
    elif not re.match(r'Finite_Conductivity_fracture', path) is not None:
        kwargs["well type"] = "Finite Conductivity Fracture"
    elif not re.match(r'Finite_Radius', path) is not None:
        kwargs["well type"] = "finite radius"
    kwargs["typical"] = ["Analytical model", "\n" 
                        "Wellbore=Constant", "Well=Vertical", "Reservoir=Homogeneous"]
    log_plot(df)
