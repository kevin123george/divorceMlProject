import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
df = pd.read_csv("featuresdf.csv")
for k in df.columns:
    print (k)

print ("------------------------------------")
accet = pd.read_csv("top50.csv")
for j in accet.columns:
    print(j)
# print(df)
#
# a = song_data.drop(['Unnamed: 0', 'Popularity','Track.Name','Artist.Name','Genre'], 1)
# print(a)
# b = song_data['Popularity']
# songmodel = linear_model.LinearRegression()
# songmodel.fit(a, b)
# print(songmodel.predict([[117, 55, 76, -6, 8, 75, 191, 4, 3]]))


