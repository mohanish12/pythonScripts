def pivot_library(listOfTuples):
    bookTitle = []
    bookISBN = []
    bookAuthor = []
    for tpl in listOfTuples:
        bookISBN.append(tpl[2])
        bookTitle.append(tpl[0])
        bookAuthor.append(tpl[1])
    rtrnValue = {}
    p = 0
    for i in bookISBN:
        rtrnValue[i] = (bookTitle[p], bookAuthor[p])
        p = p + 1

    return (rtrnValue)

books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"), ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
print(pivot_library(books))

