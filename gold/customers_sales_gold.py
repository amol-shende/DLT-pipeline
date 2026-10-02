import dlt
from pyspark.sql.functions import sum as _sum


#  gold - layer
def create_gold_table():
    @dlt.table(
        name = 'gold_customers_sales',
        comment = 'Aggregated layer of customer sales'
    )
    def gold_customer_sales():
        return(
            dlt.read('silver_orders_customers')
            .groupBy('customer_id','customer_name')
            .agg(
                _sum('order_amount').alias('total_sales')
            )
        )
