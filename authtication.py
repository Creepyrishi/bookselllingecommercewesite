import requests
from hashlib import sha256
from airtable import Airtable
import env
import random
import string


AIRTABLE_API_KEY = env.airtableApi()
AIRTABLE_BASE_ID = env.airtablebase()
AIRTABLE_TABLE_NAME = 'users'

# Initialize the Airtable client
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, api_key=AIRTABLE_API_KEY)

#function to check if Email is already in use or not
def checkEmailIsThere(mail):
    record = airtable.get_all(fields=['mail'])[0]['fields']['mail']
    if mail in record:
        return True
    else:
        return False

def signup(firstname, lastname, email, password):
    if not checkEmailIsThere(email):
            
        identifier  = ''.join(random.choice(string.ascii_lowercase) for _ in range(12))
        hash = sha256(password.encode()).hexdigest()
        user = {
        'identifier': identifier,
        'firstName': firstname,
        'lastName': lastname,
        'Hash': hash,
        'mail' : email
    }
        try:
            airtable.insert(user)
            return 200
        except:
            return 503
    else:
        return 409



def login():
    pass