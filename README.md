ETL pipeline using DLT.

Tasks performed at: Bronze Layer: 1. Extraction of raw orders data into bronze schema (streaming). 2. Extraction of raw customers data into bronze schema(materialized view).

Staging(view): 1. creating a view by joining both orders and customers data.

Silver Layer: 1. Filtering data from staging layer.

Gold Layer: 1. Aggregating(total sales per customer) data from silver layer.
