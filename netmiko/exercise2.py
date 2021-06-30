# Create a Connection Instance for multiple devices
from pprint import pprint

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

# Iterate over each router
for router in routers:
    # Create an SSH connection instance
    with ConnectHandler(**router) as net_connect:
        # Parse show version command result for each router
        output = net_connect.send_command(
            command_string="show version", use_textfsm=True
        )

    pprint(output)  # Using PrettyPrint

print("Done")
