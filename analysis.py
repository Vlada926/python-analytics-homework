import pandas as pd

data = {
    "city": ["Kyiv", "Lviv", "Odesa"], "sales":
  }
df = pd.DataFrame(data)

print("Продажі по містах:")
print(df)

print("Середнє значення:", df["sales"].mean())
