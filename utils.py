import pandas as pd


def load_data():
    titanic = pd.read_csv("data/titanic.csv")
    titanic = titanic[titanic["sex"] == "male"]
    return titanic
