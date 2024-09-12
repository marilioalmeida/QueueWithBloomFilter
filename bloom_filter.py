import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
    
    def _hashes(self, item):
        hashes = []
        for i in range(self.hash_count):
            hash_result = int(hashlib.sha256((item + str(i)).encode('utf-8')).hexdigest(), 16)
            hashes.append(hash_result % self.size)
        return hashes

    def add(self, item):
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1

    def check(self, item):
        for hash_val in self._hashes(item):
            if self.bit_array[hash_val] == 0:
                return False
        return True
