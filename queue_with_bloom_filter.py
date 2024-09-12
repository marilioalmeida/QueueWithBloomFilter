from collections import deque
from bloom_filter import BloomFilter  # Importing the BloomFilter class

class QueueWithBloomFilter:
    def __init__(self, bloom_filter_size=1000, hash_count=5):
        self.queue = deque()
        self.bloom_filter = BloomFilter(bloom_filter_size, hash_count)

    def enqueue(self, item):
        if not self.bloom_filter.check(item):
            self.queue.append(item)
            self.bloom_filter.add(item)
            print(f"Enqueued: {item}")
        else:
            print(f"Duplicate item ignored: {item}")

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)
