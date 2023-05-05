"""
Partes de código extraidas de: 
https://github.com/satwikkansal/python_blockchain_app
"""

from hashlib import sha256
import json
import os, signal

fifo_hash = '/tmp/my_fifo.'

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
    difficulty = 6

    computed_hash = block.compute_hash()
    while not computed_hash.startswith('0' * difficulty):
        block.nonce += 1
        computed_hash = block.compute_hash()

    return computed_hash, block.nonce
    
def handle_signal(signum, frame):
    print("Señal recibida.")

    with open(fifo_hash, 'r') as fifo:
        nonce = fifo.read()

        print(nonce)
        exit(0)


for i in range(2):
    pid = os.fork()
    if pid == 0:
        print(f'{os.getpid()} hijo DE {os.getppid()}')
        record = os.getpid()

        b = NoBlock(seed='La semilla que quiera', nonce=0)
        h = b.compute_hash()
        new_hash = proof_of_work(b)
        nonce = new_hash[1]
        nonce_str = str(nonce)

        os.kill(os.getppid(), signal.SIGUSR1)

        fifo = open(fifo_hash, 'w')
        fifo.write(f'El nonce encontrado es: {nonce_str}\nLo encontro: {record}')
        fifo.close()

        exit()
        

signal.signal(signal.SIGUSR1, handle_signal)
os.wait()