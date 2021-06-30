# Create a Connection Instance
from pprint import pprint

from netmiko import ConnectHandler

# Router to SSH into
router = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "session_log": "csr-ex1.log",  # Optional (No default value)
}

# Create an SSH connection instance (Context Manager Method)
with ConnectHandler(**router) as net_connect:
    # Parse show version command result for each router
    output = net_connect.send_command(command_string="show version", use_textfsm=True)

pprint(output)  # Using PrettyPrint

print("Done")
