import pandas as pd

def getData(files):
    """Get the data of the CSV file

    Args:
        files (string): A string of the CSV file name

    Returns:
        List: returns the list separated by commas
    """
    # with open(files, newline='') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar="|")
    #     newList = []
    #     count = 0
    #     temp = " "
    #     for row in spamreader:
    #         temp = " ".join(row)
    #         if count == 0:
    #             count += 1
    #         else:
    #             newList.append(temp)
    #             count += 1
    #     return newList
    return pd.read_csv(files)

def countData(dataFrame):
    """Gets a total count of data including the titles

    Args:
        files (str): String of the csv file location

    Returns:
        int: returns an integer of the count
    """
    return dataFrame.shape[0]

def getNumericRows(df):
    df["Profit (in millions)"] = pd.to_numeric(df["Profit (in millions)"], errors="coerce")
    df = df.dropna(axis=0, subset="Profit (in millions)")
    df = df.reset_index()
    return df

def writeJson(df, jsonfile):
    json = df.to_json(jsonfile, orient="records", lines=True)
    return pd.read_json(jsonfile, lines=True)

def sortData(df):
    df = df.sort_values(by=["Profit (in millions)"], ascending=False)
    df = df.reset_index()
    df = df.drop(columns=["level_0", "index"])
    return df.head(20)