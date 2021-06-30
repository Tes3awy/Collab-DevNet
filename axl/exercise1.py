# Export Users and Phones to JSON files

import json

from ciscoaxl import axl
from zeep.helpers import serialize_object

# Credentials
cucm = "10.10.20.1"
username = "administrator"
password = "ciscopsdt"
version = "12.5"

# Create a connection instance with the CUCM
ucm = axl(cucm=cucm, username=username, password=password, cucm_version=version)

# Change the zeep.LPhone to dictionary
ucm_phones = serialize_object(obj=ucm.get_phones(), target_cls=dict)
ucm_users = serialize_object(obj=ucm.get_users(), target_cls=dict)

# Export UCM Phones to a JSON file
with open("ucm-phones-12.5.json", "w") as outfile:
    json.dump(ucm_phones, outfile, indent=4, sort_keys=True)

# Export UCM Users to a JSON file
with open("ucm-users-12.5.json", "w") as outfile:
    json.dump(ucm_users, outfile, indent=4, sort_keys=True)

print("Done")
