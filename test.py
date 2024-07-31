import requests


url = 'https://blcvsz.smartaira.net/v12_0/serviceTicket'

payload = {
    "username": "ssomal@vsz",
    "password": "rYr8aq84g2kRMtdhWb",
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, json=payload, headers=headers)

print(response)