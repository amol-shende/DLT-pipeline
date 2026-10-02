import dlt

# order-cutomer view
def create_orders_customers_view():
    @dlt.view(
        name = 'orders_customers_view',
        comment = 'view of orders and customers data'
    )
    def orders_customers_view():
        df_orders = dlt.read('bronze_orders')
        df_customers = dlt.read('bronze_customers')
        return (df_orders.join(df_customers, df_orders.customer_id == df_customers.customer_id, 'inner')
                    .select(
                    df_orders.order_id,
                    df_orders.customer_id,
                    df_customers.customer_name,
                    df_orders.order_date,
                    df_orders.order_amount
                ))
