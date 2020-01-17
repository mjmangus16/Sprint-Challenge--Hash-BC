import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    # Create a starting point for your proof to start guessing with. This is where you can gain some ground against other people mining.
    # By increasing your starting point and increasing the amount the proof is increased by for each guess, you are moving ahead at a faster pace
    print("Searching for next proof")
    proof = 2187869690
    #  TODO: Your code here

    # Pass the last proof in to check that the proof is valid based on the requirements. 
    # We keep increasing the proof until we find one that works.
    while valid_proof(last_proof, proof) is False:
        proof += 1111

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    # TODO: Your code here!
    
    # The last hash comes in as an int. We need to convert it to a string and encode it so that we can hash it.
    # We need the hashed version of the proof because that is what we are matching against
    last_proof = f'{last_hash}'.encode()
    last_proof_hash = hashlib.sha256(last_proof).hexdigest()

    # Our proof is passed in as an int and needs to be converted to a string and encoded so we can hash it.
    guess = f'{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    
    # We return the True or False based on the sliced hashes based on the requirements of the proof
    return guess_hash[:6] == last_proof_hash[-6:]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"
        # node = "https://lambda-coin-test-1.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
