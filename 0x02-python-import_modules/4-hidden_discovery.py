#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = [name for name in dir(hidden_4) if name[:2] != "__"]
    names.sort()
    for i in names:
        print(i)
