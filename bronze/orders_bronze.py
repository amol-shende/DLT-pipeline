import dlt
from pyspark.sql import SparkSession

spark = SparkSession.getActiveSession()

# streaming orders data
def create_bronze_orders():
    @dlt.table(
        name = 'bronze_orders',
        comment = 'streaming ingestion of orders data'
    )
    def bronze_orders():
        return spark.readStream.table('raw_data.orders_schema.orders')
