from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.validate import validate_data

df = extract_data()

df = transform_data(df)

df = validate_data(df)

print(df.head())