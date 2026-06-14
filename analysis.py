import pandas as pd

data = {
    "cyti": ["Kyiv", "Lviv", "Odesa"], "sales":
    }
df = pd.DataFrame(data)

print("Продажі по містах (тимчасова версія):")
print(df)

print("Середнє значення:", df["sales"].mean())
