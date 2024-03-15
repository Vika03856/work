import pandas as pd
import json

# Load Excel to DataFrame
path_excel = 'db.xlsx'
df = pd.read_excel(path_excel, engine='openpyxl')
# print(df)

# Convert DataFrame to JSON
j_string = df.to_json(orient='records', indent=4)
# print(j_string)

data = json.loads(j_string)
i = 0
for o in data:
    print(o)
    i = i + 1
    o["id"] = i
    # o.update({"id": "red"})
print(data)