import hashlib
import time
import json

"""
DESCRIPTION:
This is a prototype of a blockchain based voting system.
"""

def create_hash(index, previous_hash, timestamp, vote_for):
    return hashlib.sha256(f"{index}{previous_hash}{timestamp}{vote_for}".encode()).hexdigest()

def create_genesis_block():
    return {
        "index": 0,
        "previous_hash": "0",
        "timestamp": time.time(),
        "vote_for": "Genesis Vote",
        "hash": create_hash(0, "0", time.time(), "Genesis Vote")
    }

def create_new_block(previous_block, vote_for):
    return {
        "index": previous_block['index'] + 1,
        "previous_hash": previous_block['hash'],
        "timestamp": time.time(),
        "vote_for": vote_for,
        "hash": create_hash(previous_block['index'] + 1, previous_block['hash'], time.time(), vote_for)
    }







