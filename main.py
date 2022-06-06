from data import *
import pandas as pd

def main():

    csvfile = "profits.csv"
    jsonfile = "data2.json"
    
    df = getData(csvfile)

    # Total amount of rows of data not including first row
    print("The total amount of data is " + str(countData(df)) + "(not including titles)")

    # # Total amount of rows of data that is not numeric.
    df = getNumericRows(df)
    print("The total amount of data is " + str(countData(df)) + "(not including titles)")
    # print("The total amount of data that has numeric profit is " + str(countNumericProfitData(csvfile)))

    # # List the top 20 companies after writing to a json file
    # df = df.sort_values(by=["Profit (in millions)"], ascending=False)
    dfJson = writeJson(df, jsonfile)
    topRows = sortData(dfJson)
    print(topRows)

    return 0

if __name__ == '__main__':
    main()