#!/usr/bin/env python3
print(*(chr(i) for i in range(97, 123) if i not in (101, 113)), sep="")
