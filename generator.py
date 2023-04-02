import random

with open("number.txt", "a") as f:
    while True:
        f.write(str(random.randint(1000000, 1000000000)))

# you can terminate the script by pressing Ctrl+C
