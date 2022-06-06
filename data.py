import pandas as pd

def getData(files):
    """Get the data of the CSV file

    Args:
        files (string): A string of the CSV file name

    Returns:
        DataFrame: Returns the DataFrame
    """
    return pd.read_csv(files)

def countData(dataFrame):
    """Gets a total count of data including the titles

    Args:
        DataFrame (DataFrame): The dataframe that you want counted.

    Returns:
        int: returns an integer of the count
    """
    return dataFrame.shape[0]

def getNumericRows(df, dict="Profit (in millions)"):
    """gets the new dataframe that has numeric values

    Args:
        df (DataFrame): The dataframe from the file provided

    Returns:
        DataFrame: _description_
    """
    df[dict] = pd.to_numeric(df[dict], errors="coerce")
    df = df.dropna(axis=0, subset=dict)
    df = df.reset_index()
    return df

def writeJson(df, jsonfile):
    """writes to a new JSON file that from the provided DataFrame

    Args:
        df (DataFrame): The DataFrame that is changed into a json file.
        jsonfile (str): File name of the JSON file

    Returns:
        DataFrame: Returns the json DataFrame
    """
    json = df.to_json(jsonfile, orient="records", lines=True)
    return pd.read_json(jsonfile, lines=True)

def sortData(df, dict="Profit (in millions)", top=20):
    """Sorts the data

    Args:
        df (DataFrame): The DataFrame you want sorted
        dict (str, optional): The column you want to be sorted. Defaults to "Profit (in millions)".
        top (int, optional): The number of rows you want returned. Defaults to 20.

    Returns:
        DataFrame: Returns the sorted DataFrame with the amount of rows specified
    """
    df = df.sort_values(by=[dict], ascending=False)
    df = df.reset_index()
    df = df.drop(columns=["level_0", "index"])
    return df.head(top)