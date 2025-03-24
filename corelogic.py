import requests
import json
import dotenv
import os
dotenv.load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

# Get the access token
def get_access_token(client_id, client_secret):
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    corelogic_auth_url = 'https://api-sbox.corelogic.asia/access/as/token.oauth2' 
    response = requests.post(corelogic_auth_url, data=data)
    access_token = response.json()['access_token']
    return access_token

# Get the address
def 
address_base_url = 'https://api-uat.corelogic.asia/sandbox/search/au/matcher/address'
q = '?q=15%20Hawkesbury%20Place%20Dubbo%20NSW%202830'
url = corelogic_base_url + q

