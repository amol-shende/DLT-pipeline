import dlt 
from pyspark.sql.functions import col

# silver layer - order customer
def create_silver_table():
    @dlt.table(
        name = 'silver_orders_customers',
        comment = 'silver layer of orders and customers data'
    )
    def silver_orders_customers():
        return (
            dlt.read('orders_customers_view')
            .filter(col('order_amount').isNotNull())
        )
