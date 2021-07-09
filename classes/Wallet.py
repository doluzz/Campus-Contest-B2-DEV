import uuid
import json

class Wallet:
    unique_id = ""
    balance = 0
    history = []

def generate_unique_id():
    unique_id = str(uuid.uuid4())
    return unique_id

def add_balance(addBal):
    Wallet().balance = Wallet().balance + addBal

def sub_balance(subBal):
    Wallet().balance = Wallet().balance - subBal

def send():
    pass

def save():
    data = Wallet().balance
    with open("content/wallets/" + generate_unique_id() + ".json" ,"w") as st:
        json.dump(data, st)

def load(file):
    with open('content/wallets/' + file) as f:
        d = json.load(f)
        print(d)

load()
