"""
Partes de código extraidas de: 
https://github.com/satwikkansal/python_blockchain_app
"""

from hashlib import sha256
import json
from multiprocessing import Process, Pipe
import os

class NoBlock:
    def __init__(self, seed, nonce=0):
        self.seed = seed
        self.nonce = nonce

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest() #Devuelve el hash del bloque

def proof_of_work(block):
    """
    Function that tries different values of nonce to get a hash
    that satisfies our difficulty criteria.
    """
    difficulty = 4

    computed_hash = block.compute_hash()
    while not computed_hash.startswith('0' * difficulty):
        block.nonce += 1
        computed_hash = block.compute_hash()

    return computed_hash, block.nonce



def mining(pipe):
    b = NoBlock(seed='La semilla que quiera', nonce=0)
    h = b.compute_hash()
    new_hash = proof_of_work(b)
    nonce = new_hash[1]
    nonce_str = str(nonce)

    pipe.send(f'El nonce encontrado es: {nonce_str}\nLo encontro el hijo: {process.name}')
    pipe.close()

if __name__ == '__main__':
    p, c = Pipe()
    processes = [Process(target=mining, args=(c,)) for _ in range(10)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    response = p.recv()
    print(response)