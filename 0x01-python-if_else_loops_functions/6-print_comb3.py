#!/usr/bin/python3
for a in range(8):
    for b in range(a + 1, 10):
        if a == b:
            continue
        print(f"{a}{b}", end=", ")
print(89)
