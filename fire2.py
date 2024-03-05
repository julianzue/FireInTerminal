import os
import time

data = [
    [6, 8, 10, 7, 10, 6, 8, 10, 7, 2],
    [7, 12, 9, 10, 12, 7, 12, 9, 10, 1],
    [5, 7, 8, 6, 7, 8, 7, 8, 6, 2],
    [2, 5, 9, 5, 4, 10, 5, 9, 5, 4],
    [5, 7, 10, 6, 5, 6, 7, 10, 6, 5],
    [3, 4, 5, 3, 7, 3, 4, 5, 3, 1]
]

while True:
    os.system("clear")

    for part in data:

        maximum = max(part)

        space = 15 - maximum

        for i in range(space):
            print("")

        lines = ["","","","","","","","","",""]

        for i in range(maximum):

            for index, line in enumerate(part):
                if line >= maximum - i:
                    lines[index] = "#"
                else:
                    lines[index] = " "

            print("".join(lines))

        time.sleep(0.5)
        os.system("clear")