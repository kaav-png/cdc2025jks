import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os



data = list()

#formatting the dataset
with open('Pop_Culture.csv','r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        data.append(row)

#converting to dataframe
data_df = pd.DataFrame(data)

#naming columns
data_df.columns = ['review_id','fav_heroe','fav_villain',"fav_film","fav_soundtrack", "fav_spaceship", "fav_planet", "fav_robot"]

#making x and y and preprocessing data
from sklearn.preprocessing import OneHotEncoder

x = data_df[["fav_film", "fav_soundtrack", "fav_spaceship", "fav_planet", "fav_robot"]]
encoded = OneHotEncoder()
x_mod = encoded.fit_transform(x)
y = data_df["fav_heroe"]

#splitting dataset and training
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_mod, y, test_size = 0.2, random_state=60)

#testing data
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

mL = DecisionTreeClassifier(max_depth=18, random_state=42)
mL.fit(x_train, y_train)

y_pred = mL.predict(x_test)
#print(accuracy_score(y_test, y_pred))

# change dashes based on what the user input is
user_input = pd.DataFrame([{
    "fav_film": ["Episode VI - Return of the Jedi"],
    "fav_soundtrack": ["Imperial March"],
    "fav_spaceship": ["Millennium Falcon"],
    "fav_planet": ["Endor"],
    "fav_robot": ["R2-D2"] 
    }])

#this ranks the probabilities of matches based on user responses
user_mod = encoded.fit_transform(user_input)
prediction = mL.predict(user_mod)

probability = (mL.predict_proba(user_input) * 100)
match = mL.classes_
match = match

sample_index = 0
sample_probs = probability[0]

ranking = pd.DataFrame({ 
    "Match": match,
    "Probability" : sample_probs
}).sort_values("Probability", ascending=False)

print(ranking)

#from sklearn.neighbors import KNeighborsClassifier

#knn = KNeighborsClassifier(n_neighbors=10)
#knn.fit(x_train, y_train)

#print(knn.score(x_test, y_test))

input_array = user_input.to_numpy()
ranking_array = ranking.to_numpy()

plt.pie(input_array)
plt.show()