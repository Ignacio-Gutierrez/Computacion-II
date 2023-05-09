"""
Partes de código extraidas de: 
https://github.com/satwikkansal/python_blockchain_app
"""

from hashlib import sha256
import json
from multiprocessing import Process, Pipe
import os, signal

r, w = os.pipe()

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
    difficulty = 3

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
    
    try:
        pipe.send(f'El nonce encontrado es: {nonce_str}\nLo encontro: {os.getpid()}')
        pipe.close()
    except:
        print(f'Soy {os.getpid()}, llegue tarde :(')

    os.kill(os.getppid(), signal.SIGUSR1)

def handle_signal(signum, frame):
    print(f'Señal {signum} recibida.')

    response = p.recv()

    print(response)
    exit()
    
signal.signal(signal.SIGUSR1, handle_signal)

for i in range(10):
    p, c = Pipe()
    process = Process(target=mining, args=(c,))
    process.start()
    process.join()