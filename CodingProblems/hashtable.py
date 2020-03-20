# Creating a hash table using only arrays

import hashlib
from hashlib import sha256

input = [('monk','bear'),('plecistocene',8000),('myopic',2202)]
tablesize = 2048
hashtable = [None] * (tablesize)

# For fun, though impractical: 
# Calling update on sha256 concats into a digest. Not practical here unless recast sha256()
# hashfunction = sha256()

#sha256() requires byte string. str.encode() provides bytes. hexdigest() gives hex val
# Update puts result into the hashfunction digest, which could be most conveniently recalled with hexdigest()
# hash = lambda key, size : hashfunction.update(str(key).encode())

# hashfunction returns index of target in hashtable. ascii should be semirandom
# % tablelen ensures that there are no collisions if inputlen<tablelen!
# If lots of input, should include way to turn values at indices into lists to prevent impact from collisions.
hashfunction = lambda key, size : sum([ord(char) for char in key]) % size

for pair in input:
  # First value in pair tuple is the key
  hash = hashfunction(pair[0], tablesize)
  hashtable[hash] = pair[1]
  print("Hash: "+str(hash)+" Value: "+str(hashtable[hash]))
