from queue_with_bloom_filter import QueueWithBloomFilter

# Example usage
queue = QueueWithBloomFilter()

# Enqueue elements
queue.enqueue("apple")
queue.enqueue("banana")
queue.enqueue("orange")

# Trying to enqueue duplicates
queue.enqueue("apple")  # Duplicate, will be ignored
queue.enqueue("banana")  # Duplicate, will be ignored

# Enqueue a new element
queue.enqueue("grape")

# Dequeue elements
print("Dequeued:", queue.dequeue())  # Dequeued: apple
print("Dequeued:", queue.dequeue())  # Dequeued: banana
print("Queue size:", queue.size())   # Queue size: 2
