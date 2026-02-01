import pandas as pd


def load_data(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filepath_or_buffer=filename)
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
    row = df.loc[df['Absolute Magnitude'].idxmax()]
    return str(row['Name']), float(row['Absolute Magnitude'])


def closest_to_earth(df: pd.DataFrame) -> tuple[str, float]:
    row = df.loc[df['Miss Dist.(kilometers)'].idxmin()]
    return str(row['Name']), float(row['Miss Dist.(kilometers)'])


if __name__ == '__main__':
    df1 = load_data('nasa.csv')
    df1 = mask_data(df1)
    print(data_details(df1))
    print(max_absolute_magnitude(df1))
    print(closest_to_earth(df1))