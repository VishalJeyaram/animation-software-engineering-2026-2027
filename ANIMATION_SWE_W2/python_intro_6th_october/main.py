import os


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

# Catching errors
def count_3():
    for x in range(-10,10):
        try:
            print(10/x)
        except ZeroDivisionError:
            print("Error!!!!")

# To read and print text files
# Use 'cat > file.txt' in the command prompt to make a new file on local folder
def read_text_files():
    try:
        with open("file.txt", "r") as f:
            text = f.read()
            print(text)
    except FileNotFoundError:
        print("no file found!")

# To write into text files
def write_text_files():
    f = open("file.txt", "w")
    for x in range(10,101):
        f.write(f"{str(x)}\n")
    f.close()

# To print the name of the current working directory
def print_cwd():
    cwd = os.getcwd()
    print(f"Current Directory is: {cwd}")
    ls = os.listdir(".")
    for index, fileName in enumerate(ls, start=1):
        if fileName[0] != ".":
            print(f"{index}: {fileName}")

# Removing/Deleting a file
def delete_file(name):
    try:
        os.remove(name)
    except FileNotFoundError:
        print("File not found!\n")

def main():
    # Using count
    # gen = count()
    # print(next(gen)) # Pops back in, x = 1
    # print(next(gen)) # Pops back in, x = 2

    # Using
    #gen = count_2()
    #for x in gen: # Akin to calling next() on the count_2() function as gen = count()
    #    print(x)

    # Using count_3
    #count_3()

    # Opening text files
    #read_text_files()

    # Writing to text files
    write_text_files()

    # Printing current working directory
    print_cwd()

    # Deleting a file
    delete_file("file.txt")

if __name__ == "__main__":
    main()
