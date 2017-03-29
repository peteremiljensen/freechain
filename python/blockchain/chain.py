import sys
import threading

from blockchain.loaf import *
from blockchain.block import *

#   _____ _           _
#  /  __ \ |         (_)
#  | /  \/ |__   __ _ _ _ __
#  | |   | '_ \ / _` | | '_ \
#  | \__/\ | | | (_| | | | | |
#   \____/_| |_|\__,_|_|_| |_|
#

class Chain():
    def __init__(self):
        genesis_block = Block.create_block_from_dict(
            {'loafs': [], 'nounce': 7868515,
             'previous_block_hash': '-1', 'height': 0,
             'timestamp': '2017-03-29 11:28:48.355664',
             'hash': '0000001f0dc797d2c8034ff1e7dde91b2881230e60397d24f36ddea7ea09b1cd'})
        self._chain = [genesis_block]
        self._chain_lock = threading.RLock()

    def add_block(self, block):
        with self._chain_lock:
            if block.validate() and \
               self._chain[-1].get_hash() == block.get_previous_block_hash() \
               and len(self._chain) == block.get_height():
                self._chain.append(block)
                return True
            else:
                return False

    def get_block(self, height):
        with self._chain_lock:
            return self._chain[height]

    def get_length(self):
        with self._chain_lock:
            return len(self._chain)

    def mine_block(self, loafs):
        height = self.get_length()
        previous_block_hash = self._chain[-1].get_hash()
        timestamp = str(datetime.datetime.now())
        nounce = 0
        block = None
        while True:
            block = Block(loafs, height, previous_block_hash, timestamp, nounce)
            if block.get_hash()[:5] == '00000':
                return block
            nounce += 1

    def json(self):
        return json.dumps(self._chain,
                          sort_keys=True,
                          cls=BlockEncoder).encode('utf-8')
