from airtable import Airtable
import env

# Replace these with your own Airtable API key and base ID
AIRTABLE_API_KEY = env.airtableApi()
AIRTABLE_BASE_ID = env.airtablebase()


AIRTABLE_TABLE_NAME = 'books'

# Initialize the Airtable client
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, api_key=AIRTABLE_API_KEY)

def getid(id):
    record = airtable.get(id)
    return record

def newBooks():
    # Fetch only the top 20 records from the table with specific columns ('name', 'price', 'img')
    records = airtable.get_all(max_records=20, fields=['name', 'price', 'image'],  sort=[('added', 'asc')])

    # Process the records
    data = []
    for record in records:
        # Extract the 'name', 'price', and 'img' fields from each record and add them to the data list
        fields = record['fields']
        name = fields.get('name')
        price = fields.get('price')
        img = fields.get('image')
        bookid = record['id']
        data.append({'name': name, 'price': price, 'img': img, 'bookid': bookid})

    return data

def newBooks():
    # Fetch only the top 20 records from the table with specific columns ('name', 'price', 'img')
    records = airtable.get_all(max_records=20, fields=['name', 'price', 'image'],  sort=[('added', 'desc')])

    # Process the records
    data = []
    for record in records:
        # Extract the 'name', 'price', and 'img' fields from each record and add them to the data list
        fields = record['fields']
        name = fields.get('name')
        price = fields.get('price')
        img = fields.get('image')
        bookid = record['id']
        data.append({'name': name, 'price': price, 'img': img, 'id': bookid})

    return data

def hotBooks():
    # Fetch only the top 20 records from the table with specific columns ('name', 'price', 'img')
    records = airtable.get_all(fields=['name', 'price', 'image'],  sort=[('sold', 'asc')])

    # Process the records
    data = []
    for record in records:
        # Extract the 'name', 'price', and 'img' fields from each record and add them to the data list
        fields = record['fields']
        name = fields.get('name')
        price = fields.get('price')
        img = fields.get('image')
        bookid = record['id']
        data.append({'name': name, 'price': price, 'img': img, 'id': bookid})

    return data

def search(name):
    # Fetch all records from the table
    records = airtable.get_all()

    # Process the records
    data = []
    for record in records:
        # Extract the fields from each record
        fields = record['fields']
        print(record)
        # Check if the field value (e.g., 'Name') contains the specified name as a substring
        if name.upper() in fields['name'].upper():
            data.append(fields)

    return data
