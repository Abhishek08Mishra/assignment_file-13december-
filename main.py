from random import randint,choices
import csv
import pandas as pd

stocks=[
    {"Name": "NIMB", "price":randint(1000,10000)},
    {"Name": "NIFRA", "price":randint(1000,10000)},
    {"Name": "NABIL", "price":randint(1000,10000)},
    {"Name": "HRL", "price":randint(1000,10000)},
    {"Name": "SCB", "price":randint(1000,10000)},
    {"Name": "GBIME", "price":randint(1000,10000)},
    {"Name": "NRIC", "price":randint(1000,10000)},
    {"Name": "EBL", "price":randint(1000,10000)},
    {"Name": "CIT", "price":randint(1000,10000)},
    {"Name": "NTC", "price":randint(1000,10000)},
]

headers=["Name", "price"]

with open ("stocks.csv","w",newline="") as csvfile:

    writer=csv.DictWriter(csvfile,fieldnames=headers)

    writer.writeheader()

    writer.writerows(stocks)


#reading stocks.csv file using pandas module
df = pd.read_csv("stocks.csv")
# print(df)

df["can buy"] = df["price"].apply(lambda x: "yes" if x > 5000 else "no")

print("\nUpdated DataFrame with 'can buy' column:\n", df)

df.to_csv("output_csv", index=False)