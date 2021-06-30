# Send same config to all devices and save config

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

cfg_file = "config-ex7.txt"

# Iterate over each router
for router in routers:
    # Create an SSH connection instance
    with ConnectHandler(**router) as net_connect:
        # Send configuration from a file
        output = net_connect.send_config_from_file(config_file=cfg_file)

        output += net_connect.save_config()  # Notice += operator

    print(output)

print("Done")
