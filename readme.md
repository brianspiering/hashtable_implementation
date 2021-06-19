Hash table implementation
======

This is a (hopefully) straightforward implementation of a hash table, using djb2 hashing function, in Python.

The goal of this code is an understandable example for people learning computer science fundamentals. Thus, the code does not have complete functionality, does not handle many edge cases, and is not heavily optimized.

Usage
-----

```python
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
```