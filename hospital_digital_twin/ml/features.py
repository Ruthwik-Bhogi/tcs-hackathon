import pandas as pd

def create_features(df):
    df = df.copy()

    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    df["dayofweek"] = pd.to_datetime(df["timestamp"]).dt.dayofweek

    df["total_load"] = df["er"] + df["icu"] + df["general"]

    df["rolling_er"] = df["er"].rolling(3).mean().fillna(0)
    df["rolling_total"] = df["total_load"].rolling(3).mean().fillna(0)

    return df
