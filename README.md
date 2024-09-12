# Bloom Filter Queue Project

This project demonstrates how to use a Bloom Filter for efficiently managing a queue while avoiding duplicate entries. The project contains two key components:

1. **Bloom Filter**: A probabilistic data structure used to efficiently test whether an element is present in a set.
2. **Queue with Bloom Filter**: A queue implementation that utilizes the Bloom Filter to avoid adding duplicate elements to the queue.


### 1. `bloom_filter.py`

This file defines the `BloomFilter` class, which implements a Bloom Filter to track whether an element has been added to the set.

#### Methods:
- `add(item)`: Adds an item to the Bloom Filter.
- `check(item)`: Checks if an item is possibly in the Bloom Filter.

### 2. `queue_with_bloom_filter.py`

This file defines the `QueueWithBloomFilter` class, which implements a queue that uses the Bloom Filter to prevent duplicate entries from being enqueued.

#### Methods:
- `enqueue(item)`: Adds an item to the queue if it's not a duplicate.
- `dequeue()`: Removes and returns the front item from the queue.
- `size()`: Returns the current size of the queue.

### 3. `main.py`

This file demonstrates how to use the `QueueWithBloomFilter` class. It enqueues items into the queue and prevents duplicate items using the Bloom Filter.

## How to Use

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd QueueWithBloomFilter
    ```

2. Run the `main.py` file:
    ```bash
    python main.py
    ```

This will demonstrate adding items to the queue and preventing duplicates using the Bloom Filter.

## Example Output

```bash
Enqueued: apple
Enqueued: banana
Enqueued: orange
Duplicate item ignored: apple
Duplicate item ignored: banana
Enqueued: grape
Dequeued: apple
Dequeued: banana
Queue size: 2
