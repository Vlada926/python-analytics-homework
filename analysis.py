import pandas as pd

data = {
    "cyti": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 950, 500]
  }
df = pd.DataFrame(data)

average_sales = df["sales"].mean()
print("Середнє значення:", average_sales)
print("Це середній рівень продажів за трьох міст")
