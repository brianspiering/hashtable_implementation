#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test impelementation of custom hash table and djb2 hashing function.
"""

import unittest

from hashtable import *


class TestDjb2(unittest.TestCase):

    def test_djb2_hash_function(self):
        self.assertEqual(djb2_hash_function(""),      5381)
        self.assertEqual(djb2_hash_function(" "),   177605)
        self.assertEqual(djb2_hash_function("a"),   177670)
        self.assertEqual(djb2_hash_function("1"),   177622)
        self.assertEqual(djb2_hash_function("🙂"),  306151)
        self.assertEqual(djb2_hash_function("a1"), 5863159)
        # Large unconstrained value
        self.assertEqual(djb2_hash_function("Hello, world!"), 296297508217584311834286)
        # Collisions 
        self.assertEqual(djb2_hash_function("xy"), 5863990)
        self.assertEqual(djb2_hash_function("yX"), 5863990)
        self.assertEqual(djb2_hash_function("z7"), 5863990)

class TestHashTable(unittest.TestCase):
    
    def test_put(self):
        ht = HashTable(hash_function=djb2_hash_function, size=13)
        self.assertEqual(type(ht.table), list)       # Implemented as a list
        self.assertEqual(len(ht.table), 13)          # Expected size
        self.assertEqual(type(ht.table[1]), list)    # A list-of-lists
        self.assertTrue(not any(ht.table))           # Empty list-of-lists
        key, value = "apples", 3
        ht.put(key, value)
        self.assertEqual(ht.table[1], [('apples', 3)]) # Exact location based on size and hash function

    def test_get(self):
        ht = HashTable(hash_function=djb2_hash_function, size=13)
        key, value = "apples", 3
        ht.put(key, value)
        self.assertEqual(ht.get(key), value)           # Retrieve value
        self.assertEqual(ht.get("oranges"), "'oranges' not found in hash table.") # Handle missing key

    def test_delete_without_collisions(self):
        ht = HashTable(hash_function=djb2_hash_function, size=13)
        key, value = "apples", 3
        ht.put(key, value)
        ht.delete(key)
        self.assertTrue(not any(ht.table))           # Retrieve value
        
    def test_collisions(self):
        ht = HashTable()
        key, value = "oranges", 4
        ht.put(key, value)
        key, value = "pears", 1
        ht.put(key, value)
        self.assertEqual(ht.table[5], [('oranges', 4), ('pears', 1)]) # Exact location based on size and hash function
        self.assertEqual(ht.get("oranges"), 4)
        self.assertEqual(ht.get("pears"),   1)

    def test_delete_with_collisions(self):
        
        # First collision value
        ht = HashTable(hash_function=djb2_hash_function, size=13)
        key, value = "oranges", 4
        ht.put(key, value)
        key, value = "pears", 1
        ht.put(key, value)
        ht.delete("oranges")
        self.assertEqual(ht.table[5], [('pears', 1)]) # Exact location based on size and hash function
        
        # Second collision value
        ht = HashTable(hash_function=djb2_hash_function, size=13)
        key, value = "oranges", 4
        ht.put(key, value)
        key, value = "pears", 1
        ht.put(key, value)
        ht.delete("pears")
        self.assertEqual(ht.table[5], [('oranges', 4)]) # Exact location based on size and hash function

if __name__ == '__main__':
    unittest.main()