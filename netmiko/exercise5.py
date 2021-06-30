# Export running configuration of each router to a text file
from datetime import date

from netmiko import ConnectHandler

today = date.today()

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
        # Grab hostname of each router with show version
        hostname = net_connect.send_command(
            command_string="show version", use_textfsm=True
        )[0]["hostname"]
        # Grab show running-config command result for each router
        run_cfg = net_connect.send_command(command_string="show running-config")

    # Export running-config of each router to a text file
    cfg_fname = f"{hostname}_{today}.txt"
    with open(file=f"{cfg_fname}", mode="w") as outfile:
        outfile.write(run_cfg.lstrip())

    print(f"Exported {router['ip']}'s running configuration to {cfg_fname}.")

print("Done")
