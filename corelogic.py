import requests
import json
import dotenv
import os
dotenv.load_dotenv()


# Get the access token
def get_access_token():
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    corelogic_auth_url = 'https://api-sbox.corelogic.asia/access/as/token.oauth2' 
    response = requests.post(corelogic_auth_url, data=data)
    access_token = response.json()['access_token']
    return access_token

# Get the propertyid from the address
def get_property_id_from_address(address):
    access_token = get_access_token()
    corelogic_base_url = 'https://api-uat.corelogic.asia/sandbox/search/au/matcher/address'
    q = corelogic_base_url + '?q=' + address
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.get(q, headers=headers)
    print(response.json())
    property_id = response.json()['matchDetails']['propertyId']
    return property_id

def get_property_details_from_property_id(property_id):
    access_token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    corelogic_base_url = 'https://api-sbox.corelogic.asia/property-details/'
    url_w_id = f'{corelogic_base_url}/au/properties/{property_id}/'

    endpoints = [
        "developmentApplication",
        "location",
        "sales",
        "sales/last",
        #"images",
        #"images/default",
        "legal",
        "site",
        "attributes/additional",
        "occupancy",
        "statisticReferences",
        "features",
        "otm/campaign/sales",
        "otm/campaign/rent",
        "contacts"
    ]

    results = {}
    for endpoint in endpoints:
        url = url_w_id + endpoint
        response = requests.get(url, headers=headers)
        
        try:
            data = response.json()
            if 'errors' in data:
                print(f"❌ No data for {endpoint}: {data['errors']}")
            else:
                print(f"✅ Data found for {endpoint}")
                results[endpoint] = data
        except json.JSONDecodeError:
            print(f"❌ Failed to parse JSON from {endpoint}")
    
    return results


my_address = '2 Albert Avenue Broadbeach QLD 4218'
my_address = '15 Peppermint Place Grafton NSW 2460'
property_id_of_my_address = get_property_id_from_address(my_address)
print(property_id_of_my_address)

