
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")

query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue,
       AVG(price) AS avg_price
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)
conn.close()

print("Sales Summary:")
print(df)

plt.figure()
plt.bar(df['product'], df['revenue'])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()
