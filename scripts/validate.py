def validate_data(df):

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        raise Exception("Missing values detected in dataset")

    # Check for duplicate records
    if df.duplicated().sum() > 0:
        raise Exception("Duplicate records found")

    # Check for negative price or quantity
    if (df["price"] < 0).any() or (df["quantity"] < 0).any():
        raise Exception("Invalid negative values detected")

    print("Data validation passed")

    return df