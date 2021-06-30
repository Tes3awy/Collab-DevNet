# Read an Excel file to update the new users

import pandas as pd
from ciscoaxl import axl

# Read the Excel file
excel_file = pd.read_excel(
    io="Users.xlsx",
    sheet_name=0,
    engine="openpyxl",
    usecols="A,D",
)
# Convert data to a DataFrame
df = pd.DataFrame(excel_file)

usrs = df.rename(
    columns={
        "USER ID": "userid",
        "Email Address": "mailid",
    }
).to_dict(orient="records")

data = {"users": usrs}

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

# Update each user
for user in users:
    output = ucm.update_user(**user)
    updated_user = ucm.get_user(user["userid"])
    print(
        f'{user["mailid"]} was added to {updated_user["firstName"]} {updated_user["lastName"]} successfully.'
    )

print("Done")
