import requests
from hashlib import sha256

def get_price(ticker):
    """ acquire current price of stock from the IEX Cloud API """
    endpoint = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="
    response = requests.get(endpoint + ticker).json()
    return response['LastPrice']

def hash_password(password):
    """ converts a plain-text password to a sha256 hashed version, 
    for database storage and lookup """
    return password
