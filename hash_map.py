class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True

        return False
    


    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError("Key not found")

    def remove(self, key):
        pass


    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass

    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
