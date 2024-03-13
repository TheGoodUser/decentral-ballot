import pickle
import json


with open("./Polling_Records/encrypted_blockchain.bin", "rb") as file:
    while True:
        try:
            print(json.dumps(pickle.load(file), indent=4))
        except EOFError:
            break










