import requests
from hashlib import sha256

def get_price(ticker):
    endpoint = ""
    response = requests.get(endpoint + ticker)
    response = response.json()
    return response['LastPrice']

def hash_password(password):
    """ converts a pleain-text password to a sha256 hashed output,
    for database storage and comparison """
    hasher = sha256()
    hasher.update(password.encode())
    return hasher.hexdigest()

if __name__ == "__main__":
    print(hash_password('password'))
    print(get_price('ibm'))
