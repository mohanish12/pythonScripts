def to_upper_copy(file1, file2):
    write = open(file1, "w")
    read = open(file2, "r")
    for str in read:
        write.write(str.upper())


to_upper_copy("test1", "test2")