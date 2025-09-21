import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.datasets import load_iris

data = list()


with open('Pop_Culture.csv','r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        data.append(row)


data_df = pd.DataFrame(data)
data_df.columns = ['review_id','fav_heroe','fav_villain',"fav_film","fav_soundtrack", "fav_spaceship", "fav_planet", "fav_robot"]
#print(data_df)
x = data_df[["fav_film", "fav_soundtrack", "fav_spaceship", "fav_planet", "fav_robot"]]
y = data_df[["fav_heroe"]]

knn = KNeighborsClassifier(n_neighbors=5)

knn.fot(x,y)

