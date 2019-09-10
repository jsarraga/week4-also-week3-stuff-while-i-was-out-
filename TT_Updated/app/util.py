import requests
from hashlib import sha256

USEFAKE = False
FAKESTOCK = 'STOCK'

def get_price(ticker):
    """ acquire current price of stock from the IEX Cloud API """
    if USEFAKE and ticker == FAKESTOCK:
        return 3.50
    endpoint = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="
    response = requests.get(endpoint + ticker).json()
    return response['LastPrice']

def hash_password(password):
    """ converts a plain-text password to a sha256 hashed version, 
    for database storage and lookup """
    hasher = sha256()
    hasher.update(password.encode())
    return hasher.hexdigest()


if __name__ == "__main__":
    print(get_price('ibm'))
    print(hash_password("Password"))
