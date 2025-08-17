with open('file/data.txt') as f:
    # for line in f:
    #     print(line)
    # print(f.read())
    print(f.read(10))  # Read the first 10 characters
    f.seek(20)  # Move the cursor to the 20th character
    print(f.read(10))  # Read the next 10 characters