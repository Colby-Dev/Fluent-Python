def break_line():
    print('\n')

## Example 2 - 1

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

## Example 2 - 2

codes = [ord(symbol) for symbol in symbols]
print(codes)

# Example 2 - 3

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

# Example 2 - 4

print("\n---- EX 2-4 ----\n")

colors = ['black','white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(f'This shows the list of tuples: \n{tshirts}')

print(f'\nNow this prints the tuples themselves: \n')
for color in colors: 
    for size in sizes:
        print((color, size))

#Example 2 - 5
print("\n---- EX 2-5 ----\n")
symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

#Example 2 - 6
print("\n---- EX 2-6 ----\n")
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} , {s}' for c in colors for s in sizes):
    print(tshirt)

#Example 2 -7 
print("\n---- EX 2-7 ----\n")
lax_cords = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

break_line()

for country, _ in traveler_ids:
    print(country)

#Example 3

x = "ABC"
codes = [ord(x) for x in x]

codes = [last := ord(c) for c in x]
print(last)


#Example 4

a = (1, 2, [3, 4])
b = (1, 2, [3, 4])
# a == b is true here but since the 3rd item is a mutable one it can change making it false: 
b[-1].append(100)

# To find fixed values like tuples use the hash function to determine if they are truly immutable:

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

c = (1,2,(3,4))
d = (1,2,[3,4])

fixed(c) # --> Returns True
fixed(d) # --> Returns False 

