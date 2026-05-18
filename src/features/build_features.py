import pandas as pd


def create_time_features(df):

    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Week"] = df["Date"].dt.isocalendar().week

    return df

def create_lag_features(df):

    df = df.copy()

    df["Lag_1"] = (
        df.groupby("Store")["Weekly_Sales"]
        .shift(1)
    )

    df["Lag_2"] = (
        df.groupby("Store")["Weekly_Sales"]
        .shift(2)
    )

    df["Lag_4"] = (
        df.groupby("Store")["Weekly_Sales"]
        .shift(4)
    )

    return df

def create_rolling_features(df):
    df = df.copy()

    df["Rolling_Mean_4"] = (
        df.groupby("Store")["Weekly_Sales"]
        .transform(
            lambda x: x.rolling(window=4).mean()
        )
    )

    df["Rolling_Std_4"] = (
        df.groupby("Store")["Weekly_Sales"]
        .transform(
            lambda x: x.rolling(window=4).std()
        )
    )

    return df

def clean_missing_values(df):

    df = df.copy()

    df = df.dropna()

    return df
