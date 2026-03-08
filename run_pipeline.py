from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.validate import validate_data
from scripts.load import load_data
from scripts.upload_to_s3 import upload_to_s3


def run_pipeline():

    try:
        print("Starting ETL pipeline...")

        df = extract_data()

        df = transform_data(df)

        df = validate_data(df)

        load_data(df)

        upload_to_s3(
            "data/sales_data.csv",
            "kashvi-etl-data-pipeline",
            "sales_data.csv"
        )

        print("ETL pipeline executed successfully")

    except Exception as e:
        print("Pipeline failed:", e)


if __name__ == "__main__":
    run_pipeline()