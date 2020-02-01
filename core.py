import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from keras.utils import plot_model
scale = StandardScaler()

df = pd.read_excel("divorce.xlsx")
k = df.drop(['Class'], 1)
print(k)
for col in df.columns:
    print(col)
# x = df[['Atr1', 'Atr2']]
x = k;
y = df['Class']

# print(x)
# print(y)
# print(type(df))

file1 = open('dis.txt', 'r')
Lines = file1.readlines()
model = linear_model.LinearRegression()
model2 = linear_model.LogisticRegression()
model.fit(x, y)
model2.fit(x, y)
print(type(model2))
# plot_model(model, to_file='model.png')
print(model.coef_)
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
print(model2.predict([ans]))
# print(model.predict([[4, 4, 3, 2, 4, 0, 0, 4, 4, 2, 4, 3, 2, 3, 2, 4, 2, 2, 3, 4, 4, 3, 3, 3, 3, 4, 3, 3, 4, 4, 3, 0, 2,
#                       1, 1, 1, 0, 0, 3, 0, 1, 0, 3, 0, 0, 0, 2, 2, 0, 0, 0, 2, 1, 2]]))


print(k.corr(method="pearson")[:1])
