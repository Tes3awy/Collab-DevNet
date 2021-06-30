from ciscoaxl import axl

# Credentials
cucm = {
    "cucm": "10.10.20.1",
    "username": "administrator",
    "password": "ciscopsdt",
    "cucm_version": "12.5",
}

# Create a connection instance with the CUCM
ucm = axl(**cucm)

# Get all IP Phones on the UCM
ucm_phones = ucm.get_phones()

# Print all phone names
for phone in ucm_phones:
    # You can use dot notation as well (phone.name instead of phone["name"])
    print(phone["name"])

print("Done")
