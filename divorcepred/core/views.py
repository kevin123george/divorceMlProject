from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler


def test(self):
    df = pd.read_excel("/home/sayone/PycharmProjects/divorcepred/divorce.xlsx")
    k = df.drop(['Class'], 1)
    x = k
    y = df['Class']
    file1 = open('/home/sayone/PycharmProjects/divorcepred/dis.txt', 'r')
    Lines = file1.readlines()
    model = linear_model.LinearRegression()
    model.fit(x, y)
    ans = []
    for line in Lines:
        print(line)
        n = int(input("enter on a scale 0 to 4    "))
        if n>4:
            n = int(4)
        if n<0:
            n = int(0)
        ans.append(n)
    print(ans)
    print(len(ans))
    print("probability")
    print(model.predict([ans]))
