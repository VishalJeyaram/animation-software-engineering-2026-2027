# Simple counting function
def count() -> int:
    x = 0
    while True:
        x += 1
        yield x # Exits current iteration and keeps it on pause

# More advanced counting function
def count_2() -> int:
    for x in range(0,100):
        yield x


def main():

    # Using count
    # gen = count()
    # print(next(gen)) # Pops back in, x = 1
    # print(next(gen)) # Pops back in, x = 2

    # Using
    gen = count_2()
    for x in gen: # Akin to calling next() on the count_2() function as gen = count()
        print(x)

if __name__ == "__main__":
    main()
