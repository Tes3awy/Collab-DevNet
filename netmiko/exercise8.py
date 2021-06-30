# Send same show commands to all devices

from netmiko import ConnectHandler

# Routers to SSH into
routers = [
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "session_log": "sandbox-session.log",
        "verbose": True,
    },
    {
        "device_type": "cisco_ios",
        "ip": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "session_log": "sandbox-mgmt-session.log",
        "port": 8181,
        "verbose": True,
    },
]

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
