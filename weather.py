import boto3
import requests
import os
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description='get weather for your zip code and country')
parser.add_argument('zip', help='ZIP code')
parser.add_argument('--country', help='Country code lowercase, default is "ua"', default='ua')

args = parser.parse_args()

api_key = os.getenv("OWM_API_KEY")

if not api_key:
    print("Ooops, no OWM_API_KEY!")
    sys.exit(1)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

req = requests.get(url)

if req.status_code!=200:
    print(f"Error: {req.status_code}")
    sys.exit(1)

print(req.json())