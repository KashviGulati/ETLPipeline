from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.validate import validate_data
from scripts.load import load_data

df = extract_data()

df = transform_data(df)

df = validate_data(df)

load_data(df)

print("ETL pipeline executed successfully")