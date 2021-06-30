# Read an Excel file to create new users

import pandas as pd
from ciscoaxl import axl

# Read the Excel file
excel_file = pd.read_excel(
    io="Users.xlsx",
    sheet_name=0,
    engine="openpyxl",
    usecols="A:C",
)
# Convert data to a DataFrame
df = pd.DataFrame(excel_file)

# Rename the columns to match the key required by the CUCM
data = {
    "users": df.rename(
        columns={
            "USER ID": "userid",
            "First Name": "firstName",
            "Last Name": "lastName",
        }
    ).to_dict(orient="records")
}

users = data["users"]

# Credentials
cucm = {
    "cucm": "10.10.20.1",
    "username": "administrator",
    "password": "ciscopsdt",
    "cucm_version": "12.5",
}

# Create a connection instance with the CUCM
ucm = axl(**cucm)

# Add each user
for user in users:
    output = ucm.add_user(**user)
    print(output["return"])

print("Done")
