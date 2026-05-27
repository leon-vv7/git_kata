import pandas as pd


def load_data():
    titanic = pd.read_csv("data/titanic.csv")
    titanic = titanic[titanic["sex"] == "male"]
    return titanic


def clean_data(df):
    """
    Clean a Pandas DataFrame by dropping rows with missing values
    and converting all categorical (object) columns to lowercase.

    Parameters:
        df (pd.DataFrame): The input DataFrame to clean.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df = df.dropna()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.lower()
    return df
