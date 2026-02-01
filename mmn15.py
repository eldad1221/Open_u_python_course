import pandas as pd


def load_data(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    return df


def mask_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['Close Approach Date'] > '2000-00-00']
    return df


def data_details(df: pd.DataFrame) -> tuple[int, int, list]:
    df.drop('Neo Reference ID', axis=1, inplace=True)
    df.drop('Orbiting Body', axis=1, inplace=True)
    df.drop('Equinox', axis=1, inplace=True)
    return len(df), len(df.columns), df.columns.tolist()


def max_absolute_magnitude(df: pd.DataFrame) ->  tuple[str, float]:
    row = df.loc[df['max_absolute_magnitude'].idxmax()]
    return row['Name'], float(row['Absolute Magnitude'])

