import pandas as pd
import os

#os.chdir("/home/mario/sorgenti/git/training/ml00/2 - Datasets e data preprocessing")
os.chdir("C:/sorgenti/git/training/ml00/2 - Datasets e data preprocessing")

iris = pd.read_csv("data/iris.csv")
iris.head() #mostra le prime 5 entry del dataset
#iris.head(10) #mostra le prima 10 entry del dataset
#iris.tail() #mostra le ultime 5 entry del dataset

print(iris.head())
