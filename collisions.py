import hashlib
import random
​
def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff
​
def how_many_before_collision(buckets, loops):
    for i in range(loops):
        tries = 0
        tried = set()
​
        while True:
            random_key = random.random()
​
            index = hash_function(random_key) % buckets
​
            if index not in tried:
                tried.add(index)
                tries += 1
​
            else:
                break
​
        print(f"{buckets} buckets, {tries} hashes before collision, ({tries / buckets * 100}% full)")
​
how_many_before_collision(32768, 10)