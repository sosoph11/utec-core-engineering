#!/usr/bin/env python3
output = ""
for c in range(ord('a'), ord('z') + 1):
    if chr(c) != 'e' and chr(c) != 'q':
        output += chr(c)
print(output)
