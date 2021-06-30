import xml.etree.ElementTree as ET

import requests
from requests.auth import HTTPBasicAuth
from requests.packages import urllib3

urllib3.disable_warnings()  # Disable the SSL warning

# Credentials
base_url = "https://192.168.1.1:8443"
username = "cisco"
password = "ciscopsdt"
verify = False

payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/12.5">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:getCCMVersion>
      </ns:getCCMVersion>
   </soapenv:Body>
</soapenv:Envelope>
"""

# POST: Get CUCM Version!!!
# Notice POST while it's supposed to be GET
response = requests.post(
    url=f"{base_url}/axl/",  # Don't remove the last /
    auth=HTTPBasicAuth(username, password),
    data=payload,
    verify=verify,
)

xmlDoc = ET.fromstring(response.content)

print(f'CUCM Version is: {xmlDoc.find(".//version").text}')
