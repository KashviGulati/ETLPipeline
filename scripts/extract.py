import pandas as pd

def extract_data():

    file_path = "data/sales_data.csv"

    df = pd.read_csv(file_path)

    print("Data extracted successfully")

    return df