# Export users and phones in two differet sheets
# in the same Excel file

import xlsxwriter
from ciscoaxl import axl

# Credentials
cucm = {
    "cucm": "10.10.20.1",
    "username": "administrator",
    "password": "ciscopsdt",
    "cucm_version": "12.5",
}

# Create a connection instance with the CUCM
ucm = axl(**cucm)

# Get all IP Phones on the UCM
ucm_phones = ucm.get_phones(
    tagfilter={
        "name": "",
        "product": "",
        "devicePoolName": "",
        "protocol": "",
        "description": "",
        "locationName": "",
        "uuid": "",
    }
)

# Get all Users on the UCM
ucm_users = ucm.get_users(
    tagfilter={
        "userid": "",
        "firstName": "",
        "lastName": "",
        "telephoneNumber": "",
        "mailid": "",
        "uuid": "",
    }
)

# Create an Excel file (Traditional Method)
workbook = xlsxwriter.Workbook(filename="UCM-Phones-and-Users-12.5.xlsx")
# Create a sheet for IP Phones within the Excel file
worksheet1 = workbook.add_worksheet("IP Phones")
# Create a sheet for Users within the Excel file
worksheet2 = workbook.add_worksheet("Users")
# Auto filters
worksheet1.autofilter("A1:G1")  # Phones Sheet
worksheet2.autofilter("A1:F1")  # Users Sheet

# The Phones header line
phones_header = {
    "A1": "IP Phone Name",
    "B1": "Product Category",
    "C1": "Device Pool Name",
    "D1": "Protocol",
    "E1": "Description",
    "F1": "Location Name",
    "G1": "UUID",
}

# The Users header line
users_header = {
    "A1": "User ID",
    "B1": "First Name",
    "C1": "Last Name",
    "D1": "Telephone Number",
    "E1": "Mail ID",
    "F1": "UUID",
}

# Format for the header lines
header_frmt = workbook.add_format(
    {"bold": True, "align": "center", "valign": "vcenter"}
)

# Write the phones header line
for cell, value in phones_header.items():
    worksheet1.write(cell, value, header_frmt)

# Write the users header line
for cell, value in users_header.items():
    worksheet2.write(cell, value, header_frmt)

# Initial values for row1 and col1 for sheet 1
row1 = 1
col1 = 0
# Initial values for row2 and col2 for sheet 2
row2 = 1
col2 = 0

# Iterate over all phones in the UCM
# And write data in the corresponding cell
for phone in ucm_phones:
    worksheet1.write(row1, col1 + 0, phone["name"])
    worksheet1.write(row1, col1 + 1, phone["product"])
    worksheet1.write(row1, col1 + 2, phone["devicePoolName"]["_value_1"])
    worksheet1.write(row1, col1 + 3, phone["protocol"])
    worksheet1.write(row1, col1 + 4, phone["description"])
    worksheet1.write(row1, col1 + 5, phone["locationName"]["_value_1"])
    worksheet1.write(row1, col1 + 6, phone["uuid"])

    # Jump to next row
    row1 += 1

# Iterate over all Users in the UCM
# And write data in the corresponding cell
for user in ucm_users:
    worksheet2.write(row2, col2 + 0, user["userid"])
    worksheet2.write(row2, col2 + 1, user["firstName"])
    worksheet2.write(row2, col2 + 2, user["lastName"])
    worksheet2.write(row2, col2 + 3, user["telephoneNumber"])
    worksheet2.write(row2, col2 + 4, user["mailid"])
    worksheet2.write(row2, col2 + 5, user["uuid"])

    # Jump to next row
    row2 += 1

# Close the workbook
workbook.close()

print("Done")
