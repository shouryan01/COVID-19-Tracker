import requests

response = requests.get('https://api.covidnow.com/v1/local/geocoding?address=Central%20Park%2C%20New%20York%20City')

print(response.status_code)
print(response.headers)
print(response.text)