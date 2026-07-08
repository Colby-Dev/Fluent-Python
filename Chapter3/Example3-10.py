from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)

print(d_proxy)

# Creates an error
d_proxy[2] = 'B'

