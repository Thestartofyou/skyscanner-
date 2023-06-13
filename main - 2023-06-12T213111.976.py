import requests
import json
from datetime import datetime, timedelta

# Skyscanner API credentials
API_KEY = 'YOUR_SKYSCANNER_API_KEY'

# Set the origin airport code
origin = 'YOUR_ORIGIN_AIRPORT_CODE'

# Set the departure date (start from today)
departure_date = datetime.now().date()

# Set the return date (two weeks from the departure date)
return_date = departure_date + timedelta(days=14)

# Set the market and currency codes
market = 'YOUR_MARKET_CODE'
currency = 'YOUR_CURRENCY_CODE'

# API endpoint URL for browsing quotes
url = f'https://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/{market}/{currency}/{origin}/anywhere/{departure_date}/{return_date}'

# Set the request headers
headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0',
    'X-RapidAPI-Key': API_KEY
}

# Send the API request
response = requests.get(url, headers=headers)

# Parse the response JSON
data = json.loads(response.text)

# Extract the cheapest quotes
quotes = data['Quotes']

if len(quotes) > 0:
    # Sort the quotes by price (ascending order)
    sorted_quotes = sorted(quotes, key=lambda x: x['MinPrice'])

    # Display the cheapest quotes
    for quote in sorted_quotes:
        destination = quote['OutboundLeg']['DestinationId']
        price = quote['MinPrice']
        print(f"Destination: {destination}, Price: {price}")
else:
    print("No flight quotes found.")
