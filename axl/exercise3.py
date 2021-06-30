# Export all Phones to an Excel file

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
ucm_phones = ucm.get_phones()

# Create an Excel file
with xlsxwriter.Workbook("UCM-Phones-12.5.xlsx") as workbook:
    # Create a sheet within the Excel file
    worksheet = workbook.add_worksheet("IP Phones")
    # Auto filters
    worksheet.autofilter("A1:D1")
    worksheet.freeze_panes(1, 1)

    # The header line
    header_line = {
        "A1": "SEP Phone Name",
        "B1": "Product Type",
        "C1": "Protocol",
        "D1": "UUID",
    }

    # Format for the header line
    header_frmt = workbook.add_format(
        {"bold": True, "align": "center", "valign": "vcenter"}
    )

    # Write the header line
    for cell, value in header_line.items():
        worksheet.write(cell, value, header_frmt)

    # Initial values for row and col
    row = 1
    col = 0

    # Iterate over SEP phones in the UCM
    # And write data in the corresponding cell
    for phone in ucm_phones:
        if "SEP" in phone["name"]:  # Or if phone["name"].startswith("SEP", 0, 3):
            worksheet.write(row, col + 0, phone["name"])
            worksheet.write(row, col + 1, phone["product"])
            worksheet.write(row, col + 2, phone["protocol"])
            worksheet.write(row, col + 3, phone["uuid"])

            # Jump to next row
            row += 1

print("Done")
