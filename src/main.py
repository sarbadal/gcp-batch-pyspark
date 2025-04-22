from pyspark.sql import SparkSession
import gcsfs

from utils.utils import full_name, alphanumeric_id, make_folder_name
from load_data.load_sample_data import load_sales_data

BUCKET_NAME = "gcp-batch-demo"
FOLDER_NAME = make_folder_name("result")
OUTPUT_PATH = f"gs://{BUCKET_NAME}/{FOLDER_NAME}.csv"


def main() -> None:
    
    spark = SparkSession.builder.appName("ETL Example").getOrCreate()
    col_id = "id"
    columns = [
        col_id, 
        "transaction_id", 
        "customer_name", 
        "product", 
        "quantity", 
        "price", 
        "total_amount", 
        "date"
    ]
    df = load_sales_data(spark)
    df = df.withColumn(col_id, alphanumeric_id())
    df = df.select(*columns)
    df = df.toPandas()
    
    fs = gcsfs.GCSFileSystem()
    with fs.open(OUTPUT_PATH, 'w') as f:
        df.to_csv(f, index=False)

    spark.stop()


if __name__ == "__main__":
    main()
