import pandas as pd
import random


def noise(i):
    flag = 0
    _fre = [1, -2, 1, -1, 2, -1]
    _s = i
    for j in range(1, len(i)):
        _s[j] = _s[j] + (0.02 * _fre[flag]) * _s[j-1]
        flag = (flag+1) % 6
    return _s


def tur(df: pd.DataFrame):
    r = random.randint(-200, 200)
    for i in range(df.shape[0]):
        df.iloc[i][1] *= (1+r/10000)
        df.iloc[i][3] *= (1+r/10000)
    return df
