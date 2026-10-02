import dlt
from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession()

# customers - Materialized view
def create_bronze_customers():
    @dlt.table(
        name = 'bronze_customers',
        comment = 'batch ingestion of customers data'
    )
    def bronze_customers():
        return spark.read.table('raw_data.customers_schema.customers')
