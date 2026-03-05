import pandas as pd

def transform_data(df):

    # remove duplicate rows
    df = df.drop_duplicates()

    # convert order_date to datetime format
    df["order_date"] = pd.to_datetime(df["order_date"])

    # create a new column total_price
    df["total_price"] = df["quantity"] * df["price"]

    print("Data transformation completed")

    return df