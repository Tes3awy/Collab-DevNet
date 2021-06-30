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
        "secret": "",
        "port": 22,
        "verbose": True,
        "session_log": "ex4-iosxe-latest.log",
    },
    {
        "device_type": "cisco_ios",
        "ip": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "secret": "",
        "port": 8181,
        "verbose": True,
        "session_log": "ex4-xe-mgmt.log",
    },
]

# Create an Excel file
with xlsxwriter.Workbook(filename="Voice-Gateways-Inventory.xlsx") as workbook:

    # The header line
    header_line = {
        "A1": "Module Name",  # 1
        "B1": "Serial Number",  # 2
        "C1": "Product ID",  # 3
        "D1": "VID",  # 4
        "E1": "Description",  # 5
    }

    header_line_frmt = workbook.add_format(
        {"bold": True, "align": "center", "valign": "vcenter"}
    )

    # Iterate over each router
    for router in routers:
        # Create an SSH connection instance for each router
        with ConnectHandler(**router) as net_connect:
            hostname = net_connect.send_command(
                command_string="show version", use_textfsm=True
            )[0]["hostname"]
            inventory = net_connect.send_command(
                command_string="show inventory", use_textfsm=True
            )

        # Create a sheet with the hostname of each router
        worksheet = workbook.add_worksheet(f'{router["ip"]} inventory')
        worksheet.autofilter("A1:E1")  # Auto filter for each sheet
        worksheet.freeze_panes(1, 1)  # Freeze panes for each sheet

        # Write header line
        for cell, value in header_line.items():
            worksheet.write(cell, value, header_line_frmt)

        # Initial value for row and col
        row = 1
        col = 0

        # Iterate over the all interfaces
        for item in inventory:
            worksheet.write(row, col + 0, item["name"])  # 1
            worksheet.write(row, col + 1, item["sn"])  # 2
            worksheet.write(row, col + 2, item["pid"])  # 3
            worksheet.write(row, col + 3, item["vid"])  # 4
            worksheet.write(row, col + 4, item["descr"])  # 5

            # Jump to next row
            row += 1

    # Notice workbook.close() is removed

print("Done")
