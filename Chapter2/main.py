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

#Example 2-8
print("\n---- EX 2-8 ----\n")
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

print(f'{"":15} | {"Latitude":>9} | {"Longitude":>9}')
for name, _, _, (lat, lon) in metro_areas:
    if lon <= 0:
        print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

#Example 2-9
print("\n---- EX 2-9 ----\n")
def handle_command(self, message):
    match message: 
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
        case ['NECK', angle]:
            self.rotate_neck(angle)
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
        case _:
            raise InvalidCommand(message)

#Example 2-10
print("\n---- EX 2-10 ----\n")
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

print(f'{"":15} | {"Lat":>9} | {"Long":>9} |')
for record in metro_areas:
    match record:
        case [name, _, _, (lat, long)] if long <=0:
            print(f'{name:15} | {lat:9.4f} | {long:9.4f} |')

#Example 2-11, Matching patterns without match/case
def evaluate(exp, env) -> any:
    "Evaluate an expression in an environment." 
    if isinstance(exp, Symbol):
        return env[exp]
    # ... lines omitted
    elif exp[0] == 'quote':
        (_, x) = exp
        return x

    elif exp[0] =='if':
        (_, test, consquence, alternative) = exp
        if evaluate(test, env):
            return evaluate(consquence, env)
        else:
            return evaluate(alternative, env)

    elif exp[0] == 'lambda':
        (_, parms, *body) = exp
        return Procedure(parms, body, env)

    elif exp[0] == 'define':
        (_, name, value_exp) = exp
        env[name] = evaluate(value_exp, env)
        # ... more lines omitted

# Example 2-13 Line items from a flat file
print('\n---- EX2 13 ----\n')
def EX213():
    invoice = """ 1909 Pimoroni PiBrella           $17.50     3     $52.50
                  1489 6mm Tactile Switch x20      $4.95      2     $9.90 """
    
    UNIT_PRICE = slice(40, 52)
    DESCRIPTION = slice(6, 40)
    line_items = invoice.split('\n')[2:]
    for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])

EX213()

print('\n---- EX2 14 ----\n')
def EX214():
    board = [['_'] * 3 for i in range(3)]
    print(board)

    board[1][2] = 'X'
    print(board)

#Example 3

print("\n---- EX 3 ----\n")
x = "ABC"
codes = [ord(x) for x in x]

codes = [last := ord(c) for c in x]
print(last)


#Example 4
print("\n---- EX 4 ----\n")
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

# Example 5
print("\n---- EX 5 ----\n")
lax_cords = (33.9425, -118.408056)
latitude, longitude = lax_cords # unpacking

# Another example of unpacking is swapping the values of variables with out using a temp var:
# Using the * operand in front of the variable grabs the excess items from arguments
a, b, *rest = range(5)
print(a, b, rest)

# It can be used in any order but must be used with only one variable in a declaration
a, *body, b = range(3)
print(a, body, b)

# Example 6
def fun(a, b, c, d, *test):
    print("\n---- EX6 ----\n")
    return a, b, c, d, *test

fun(*[1,2], 3, *range(4,7))

# Example 7
def example7():
     print("\n---- EX7 ---- \n")
     l = [10,20,30,40,50,60]
     print(l[:2]) #split at 2
     print(l[2:]) #split after 2
     print(l[:3]) #split at 3
     print(l[3:]) #split after 3

# Example 8
def example8(): 

    print("\n---- EX8 ---- \n")
    s = 'bicycle'
    print(s[::3]) # skips 3
    print(s[::-1]) # reverse string
    print(s[::-2]) # reverse by 2 chars

# Example 9
def example9(): 
    print("\n---- EX9 ---- \n")
    l = list(range(10))
    print(l)
    break_line()

    l[2:5] = [20,30]
    print(l)
    break_line()

    del l[5:7]
    print(l)
    break_line()

example9()


# Example 10 
def example10():
    print("\n---- EX10 ----\n")
    fruits = ['grapes','banana', 'apple']
    x = sorted(fruits) 
    reversed_x = sorted(fruits, reverse=True)
    desc_order_reversed_x = sorted(fruits, reverse=True, key=len)
    print(x)
    print(reversed_x)
    print(desc_order_reversed_x)

example10()
