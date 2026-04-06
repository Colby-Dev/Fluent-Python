## Example 2 - 1

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

## Example 2 - 2

codes = [ord(symbol) for symbol in symbols]
print(codes)