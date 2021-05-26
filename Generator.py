import pandas as pd


def ifi():
    path = r'./source/Infinite_Conductivity_fracture(Infinite)/1080.txt'
    df = pd.read_csv(path, header=0, sep=' ')
    for i in range(10, 1080, 10):
        f = open('/'.join(path.split('/')[:-1])+"/"+str(i)+".txt", 'w+')
        f.write(' '.join(list(df.columns))+'\n')
        f.write(' '.join(list(df.iloc[0][:4]))+'\n')
        for j in range(1, df.shape[0]):
            f.write("{:.21f}".format(float(df.iloc[j][0])))
            f.write(" ")
            f.write("{:.17f}".format(float(df.iloc[j][1])*i/1080))
            f.write(" ")
            f.write("{:.21f}".format(float(df.iloc[j][2])))
            f.write(" ")
            f.write("{:.17f}".format(float(df.iloc[j][3])*i/1080))
            f.write("\n")
        f.write("\n")
        f.close()


def fi():
    path = r'./source/Infinite_Conductivity_fracture(Singal_fault)/1080.txt'
    df = pd.read_csv(path, header=0, sep=' ')
    for i in range(10, 1080, 10):
        f = open('/'.join(path.split('/')[:-1])+"/"+str(i)+".txt", 'w+')
        f.write(' '.join(list(df.columns))+'\n')
        f.write(' '.join(list(df.iloc[0][:4]))+'\n')
        for j in range(1, df.shape[0]):
            f.write("{:.21f}".format(float(df.iloc[j][0])))
            f.write(" ")
            f.write("{:.17f}".format(float(df.iloc[j][1])*i/1080))
            f.write(" ")
            f.write("{:.21f}".format(float(df.iloc[j][2])))
            f.write(" ")
            f.write("{:.17f}".format(float(df.iloc[j][3])*i/1080))
            f.write("\n")
        f.write("\n")
        f.close()
