#!/usr/bin/python3
output = ""
for les in range(97, 123):
    output = chr(les)
    if output == 'q' or output == 'e':
        continue
    print("{}".format(output), end='')
