# Show how to parse System Info
# to dict and export and Excel file

import json
from datetime import datetime

import xlsxwriter
import xmltodict

import requests
from requests.exceptions import ConnectionError
from requests.packages import urllib3

urllib3.disable_warnings()  # Disable the SSL warning

ips = ["192.168.1.192", "192.168.1.55"]  # One of these IPs is incorrect

with xlsxwriter.Workbook(filename="System-Info.xlsx") as workbook:
    for ip in ips:
        try:
            # GET request
            response = requests.get(
                url=f"https://{ip}:8445/finesse/api/SystemInfo", verify=False
            )

            # Create a worksheet if connection is successful
            worksheet = workbook.add_worksheet(ip)
            worksheet.autofilter("A1:E1")
            worksheet.freeze_panes(1, 1)

            # Convert XML to dict
            dict_response = dict(xmltodict.parse(xml_input=response.text))

            # Export to JSON file (Comment out if not needed)
            with open(file="dict-response.json", mode="w") as outfile:
                json.dump(obj=dict_response["SystemInfo"], fp=outfile, indent=4)

            header = {
                "A1": "Primary Node",  # 1
                "B1": "Secondary Node",  # 2
                "C1": "Deployment Type",  # 3
                "D1": "XMPP Domain",  # 4
                "E1": "License",  # 5
                "F1": "Status",  # 6
                "G1": "Last Success",  # 7
            }

            # Write header line
            for cell, value in header.items():
                worksheet.write(cell, value)

            # Initial value for row and col
            row = 1
            col = 0

            # Place each value in the corresponding cell
            # according to the static header
            for key, value in dict_response.items():
                worksheet.write(row, col + 0, value["primaryNode"]["host"])  # 1
                worksheet.write(row, col + 1, value["secondaryNode"]["host"])  # 2
                worksheet.write(row, col + 2, value["deploymentType"])  # 3
                worksheet.write(row, col + 3, value["xmppDomain"])  # 4
                worksheet.write(row, col + 4, value["license"])  # 5
                worksheet.write(row, col + 5, value["status"])  # 6
                last_success = datetime.fromtimestamp(
                    int(value["lastSuccessCTIHeartbeatTime"][0:10])
                )
                worksheet.write(
                    row, col + 6, last_success.strftime("%Y-%m-%d %H:%M:%S")
                )  # 7

                # Jump to next row
                row += 1
        except ConnectionError:
            print(f"Connection Error: Please check {ip}!")


print("Done")
