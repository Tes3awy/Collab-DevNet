# Create a Connection Instance to
# the CUCM Server

from netmiko import ConnectHandler

# CUCM to SSH into
cucm = {
    "device_type": "terminal_server",  # Notice terminal_server
    "ip": "10.10.20.1",
    "username": "cisco",
    "password": "ciscopsdt",
    "verbose": True,
    "session_log": "cucm-ex6.log",
    "fast_cli": False,
    "conn_timeout": 15,
}

# Create an SSH connection instance (Traditional Method)
with ConnectHandler(**cucm) as net_connect:
    # use_textfsm is not supported for terminal_server
    output = net_connect.send_command(
        command_string="show version active", except_string="admin:"
    )

print(output)
print("Done")
