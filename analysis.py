import pandas as pd

data = {"місто": ["Київ", "Львів", "Одеса"], "sales":}
df = pd.DataFrame(data)

print("Продажі по містах (відхилена версія коду):")
print(df)

print("Середнє значення:", df["sales"].mean())
