import csv
import pandas as pd 

df = pd.read_csv("C129 pro\output.csv")


    



del df["lum"]
del df["name"]
del df["distance"]
del df["mass"]
del df["radii"]

df.to_csv("P130/main2.csv")