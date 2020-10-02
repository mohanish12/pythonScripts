def ListFiles(dir):
    for file in dir:
        print(file)
    for folder in dir:
        ListFiles(folder)

ListFiles("C:/Users/Mohanish")