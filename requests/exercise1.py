import xml.etree.ElementTree as ET

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

    # Make XML accessible
    xml_res = ET.fromstring(response.content)

    print(f'{phone} phone is in `{xml_res.find(".//devicePoolName").text}` pool.')
