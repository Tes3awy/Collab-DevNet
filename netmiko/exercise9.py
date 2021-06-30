# Send same show commands to all devices
# Read devices from an Excel file

import pandas as pd

from netmiko import ConnectHandler

# Read Excel file
excel_file = pd.read_excel(
    io="Voice-Gateways-Info.xlsx", sheet_name=0, engine="openpyxl"
)

# Converts Excel file to data frame
df = pd.DataFrame(excel_file)

# Select Col A and convert it to list
hostnames = df.iloc[:, 0].tolist()
# Select Col B and convert it to list
ips = df.iloc[:, 1].tolist()

# Routers to SSH into
routers = []

for ip, hostname in zip(ips, hostnames):
    routers.append(
        {
            "devices_type": "cisco_ios",
            "ip": ip,
            "username": "developer",
            "password": "C1sco12345",
            "session_log": f"{hostname}-session.log",
        }
    )


# Iterate over each router
for router in routers:
    # Create an SSH connection instance
    with ConnectHandler(**router) as net_connect:
        # Parse show commands for each router
        output = net_connect.send_config_set(
            config_commands=["show running-config", "show version", "show inventory"],
            enter_config_mode=False,
            delay_factor=2,  # Wait 200 seconds to let commands take time
        )

    with open(file=f'{router["ip"]}.txt', mode="w") as outfile:
        outfile.write(output.lstrip())

print("Done")
