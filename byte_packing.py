import struct

# Resources
# https://www.geeksforgeeks.org/struct-module-python/
# https://docs.python.org/3/library/struct.html
# https://code.activestate.com/recipes/510399-byte-to-hex-and-hex-to-byte-string-conversion/

# Convert integer to bytes
n = 8192
n_bytes = n.to_bytes(2, 'big')
nb_array = bytearray(n_bytes)

nb_array     # => bytearray(b' \x00)
nb_array[0]  # => 32
nb_array[1]  # => 0

# Convert bytes to hex
nb0 = hex(nb_array[0])

# Packing
struct.pack('hhhh', nb_array[0], nb_array[1])
