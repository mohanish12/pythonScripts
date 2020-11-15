def write_book_info(fileToCreate,listOfTuples):
    f = open(fileToCreate, "w")
    bookISBN = []
    bookAuthor = []
    bookTitle = []

    for tpl in listOfTuples:
        bookISBN.append(tpl[2])
        bookAuthor.append(tpl[1])
        bookTitle.append(tpl[0])
    p = 0
    for i in bookISBN:
        f.write(i + ":" + " " + bookTitle[p] + " " +  "by" + " " + bookAuthor[p] + "\n")
        p = p + 1

books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"), ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
write_book_info("test22.txt", books )