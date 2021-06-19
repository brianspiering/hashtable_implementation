#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementation of a hashtable and djb2 hashing function.

>>> from hashtable import HashTable
>>> ht = HashTable()
>>> ht.put(key='apples', value=3)
>>> ht.get('apples')
3

>>> ht.delete('apples')
>>> ht.get('apples')
"'apples' not found in hash table."

>>> from hashtable import djb2_hash_function
>>> djb2_hash_function('apples')
6953322243466
"""

from typing import Any


def djb2_hash_function(string: str) -> int:
    """Implementation of djb2 string hashing function.

    For simplicity, there are two optimization not included:
    1. Replace 33 constant with bit shift optimization
        hash_value = (( hash_value << 5) + hash_value) + ord(char)

    2. Bit mask is to constrain the hash_value to 32 bit integers
       return hash_value & 0xffffffff
    """

    # Empirically selected value that results in fewer collisions and better avalanching.
    hash_value = 5381

    for char in string:
        # 33 is another empirically selected value.
        hash_value = (hash_value * 33) + ord(char)

    return hash_value


class HashTable:

    def __init__(self, hash_function: callable=djb2_hash_function, size: int=13) -> None:
        """Setup instance of hashtable.

        hash_function is default is djb2. Any hash function could work.

        size is thenumber of entries in hash table. 
        Should be a large-ish prime numbers to minimize collisions.
        """
        self.size = size
        self.hash_function = hash_function
        self.table = [[] for _ in range(size)]  # List of lists to allow for collision chaining.

    def delete(self, key: int) -> None:
        """Remove values from table by looking in key location and iterating through all items."""
        for i, (k, v) in enumerate(self.table[self.index(key)]):
            if k == key:
                self.table[self.index(k)].pop(i)

    def get(self, key: int) -> str:
        """Given key, see if a value is present."""
        for k, v in self.table[self.index(key)]:
            if k == key:
                return v
        return f"'{key}' not found in hash table."

    def index(self, value: str) -> int:
        """For a given value, find index for entry in hash table."""
        return self.hash_function(value) % self.size

    def put(self, key: str, value: Any) -> None:
        """Store key, value pairs based on hashed value of key."""
        self.table[self.index(key)].append((key, value))
