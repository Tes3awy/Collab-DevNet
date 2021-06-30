# Export routers show version command output to an Excel file
import xlsxwriter

from netmiko import ConnectHandler

# Routers to SSH into
routers = [
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "verbose": True,
    },
    {
        "device_type": "cisco_ios",
        "ip": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 8181,
        "verbose": True,
    },
]

# Create an Excel file
workbook = xlsxwriter.Workbook(filename="Voice-Gateways-Info.xlsx")
# Add worksheet
worksheet = workbook.add_worksheet("Voice Gateway Routers Info")
# Custom formats
worksheet.autofilter("A1:K1")
worksheet.freeze_panes(1, 1)

# The header line
header_line = {
    "A1": "Hostname",  # 1
    "B1": "MGMT IP Address",  # 2
    "C1": "Serial Number",  # 3
    "D1": "MAC Address",  # 4
    "E1": "Part Number",  # 5
    "F1": "Software Version",  # 6
    "G1": "Running Image",  # 7
    "H1": "Rommon",  # 8
    "I1": "Last Reload Reason",  # 9
    "J1": "Restarted At",  # 10
    "K1": "Up Time",  # 11
    "L1": "Config Register",  # 12
}

header_line_frmt = workbook.add_format(
    {"bold": True, "align": "center", "valign": "vcenter"}
)

# Write header line
for cell, value in header_line.items():
    worksheet.write(cell, value, header_line_frmt)

# Iterate over each router
for router in routers:
    # Create an SSH connection instance for each router
    with ConnectHandler(**router) as net_connect:
        output = net_connect.send_command(
            command_string="show version", use_textfsm=True
        )

    # Initial value for row and col
    row = 1
    col = 0

    # Iterate over each value in the output
    for value in output:
        worksheet.write(row, col + 0, value["hostname"])
        # Notice router["ip"], as it's accessible from the parent loop
        worksheet.write(row, col + 1, router["ip"])  # NOTICE router["ip"]
        worksheet.write(
            row, col + 2, value["serial"][0]
        )  # [0] Because it's a list of 1 string
        try:
            worksheet.write(
                row, col + 3, value["mac"][0]
            )  # [0] Because it's a list of 1 string
        except IndexError:
            # CSR routers don't have MAC Address
            worksheet.write(row, col + 3, "N/A")
        worksheet.write(
            row, col + 4, value["hardware"][0]
        )  # [0] Because it's a list of 1 string
        worksheet.write(row, col + 5, value["version"])
        worksheet.write(row, col + 6, value["running_image"])
        worksheet.write(row, col + 7, value["rommon"])
        worksheet.write(row, col + 8, value["reload_reason"])
        worksheet.write(row, col + 9, value["restarted"])
        worksheet.write(row, col + 10, value["uptime"])
        worksheet.write(row, col + 11, value["config_register"])
        # Jump to next row
        row += 1

# Close the workbook (Save)
workbook.close()

print("Done")
