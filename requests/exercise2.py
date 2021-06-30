import json

import xmltodict

import requests
from requests.auth import HTTPBasicAuth
from requests.packages import urllib3

urllib3.disable_warnings()  # Disable the SSL warning

# Credentials
base_url = "https://10.10.20.1"
username = "administrator"
password = "ciscopsdt"
verify = False

phones = ["BOTUSER011", "CSFUSER001", "TABUSER006"]  # Only 3 devices

# Iterate over phones
for phone in phones:
    payload = f"""
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/12.5">
    <soapenv:Header/>
    <soapenv:Body>
        <ns:getPhone sequence="?">
            <name>{phone}</name>
        </ns:getPhone>
    </soapenv:Body>
    </soapenv:Envelope>
    """
    # POST: Get Pool names for devices!!!
    # Notice POST while it's supposed to be GET
    response = requests.post(
        url=f"{base_url}/axl/",  # Don't remove the last /
        auth=HTTPBasicAuth(username, password),
        data=payload,
        verify=verify,
    )

    # Parse XML to JSON
    json_res = xmltodict.parse(xml_input=response.text)

    # Get to the specified element
    phone_res = json_res["soapenv:Envelope"]["soapenv:Body"]["ns:getPhoneResponse"][
        "return"
    ]["phone"]

    # Export response to a JSON file
    with open(file=f"{phone}-response.json", mode="w") as outfile:
        json.dump(obj=phone_res, fp=outfile, indent=4, sort_keys=True)

    print(f'{phone} phone is in `{phone_res["devicePoolName"]["#text"]}` pool.')
