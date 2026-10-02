from bronze.orders_bronze import create_bronze_orders
from bronze.customers_bronze import create_bronze_customers
from views.join_view import create_orders_customers_view
from silver.orders_customers_silver import create_silver_table
from gold.customers_sales_gold import create_gold_table


# call function to register DLT tables
create_bronze_orders()
create_bronze_customers()
create_orders_customers_view()
create_silver_table()
create_gold_table()
