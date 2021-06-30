# Create a Connection Instance Exercise

from netmiko import ConnectHandler

# Router to SSH into
router = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "",  # Optional (Defaults to empty, Enable secret)
    "port": 22,  # Optional (Defaults to 22 for SSH)
    "verbose": True,  # Optional (Default False)
    "session_log": "csr-ex0.log",  # Optional (No default value)
    "global_delay_factor": 2,  # Optional (Defaults to 1)
    "fast_cli": False,  # Optional (Ignores timeouts set by Netmiko for each command)
    "conn_timeout": 15,  # Optional (Sets connection timeout)
    # There are more `items`, you can check the documentation
}

# Create an SSH connection instance (Traditional Method)
net_connect = ConnectHandler(**router)
output = net_connect.send_command(command_string="show version")
net_connect.disconnect()  # Explicit call of disconnect function

print(output)
print("Done")
