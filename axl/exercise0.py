# Get all users from the CUCM

from ciscoaxl import axl

cucm = "10.10.20.1"
username = "administrator"
password = "ciscopsdt"
version = "12.5"

ucm = axl(cucm=cucm, username=username, password=password, cucm_version=version)

ucm_users = ucm.get_users()

print(ucm_users)

print("Done")
