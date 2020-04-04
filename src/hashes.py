# in python, strings are objects - they have metadata. We use b before the string to indicate that we want it to be a byte array.
n = 1
key = b"my_value"
key2 = "string1".encode()
key3 = "lunchtime"

for i in range(n):
    print(hash(key))

# the above code 'salts' the string. Every time we run it in python, it runs a different, psuedo-random seed. This is good for security but can make debugging hard. 

# for understanding hash tables, we're not really worried about those issues; we're hashing to be able to use a table, not for security.

#build table:

#hash the key, use a modulus
index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8

print(index)
print(index2)
print(index3)
