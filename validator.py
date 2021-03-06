from .singleton import Singleton

@Singleton
class Validator():
    def __init__(self):
        self._loaf_validator  = lambda l:  True
        self._block_validator = lambda b:  True
        self._branching       = lambda c1, c2:  c1

    def attach_loaf_validator(self, function):
        self._loaf_validator = function

    def attach_block_validator(self, function):
        self._block_validator = function

    def attach_branching(self, function):
        self._branching = function

    def validate_loaf(self, loaf):
        return self._loaf_validator(loaf)

    def validate_block(self, block):
        return self._block_validator(block)

    def branching(self, chain1, chain2):
        return self._branching(chain1, chain2)
