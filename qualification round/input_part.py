class Library:
    def __init__(self, lib_id = 0, number_books = 0, signup_time = 0, ship_per_day = 0, books = []):
        self.lib_id = lib_id
        self.number_books = number_books
        self.signup_time = signup_time
        self.scan_per_day = ship_per_day
        self.books = books
        self.workingDay = 0


class Book:
    def __init__(self,id = 0,score = 0):
        self.id = id
        self.score = score


def read_file(filename):
    f = open(filename, "r")
    return f.read()

def parse_input(input):
    lines= input.splitlines()
    firstLine = list(map(int,lines[0].split()))
    secondLine = list(map(int,lines[1].split()))
    #print(lines)
    return firstLine[0],firstLine[1],firstLine[2],secondLine,lines[2:]


def LibParser(lib_info, num_lib):
    Libraries = []
    for i in range(num_lib):
        firsLine = list(map(int,lib_info[2*i].split()))
        secondLine = list(map(int,lib_info[2*i+1].split()))
        newLibrary = Library(i,firsLine[0],firsLine[1],firsLine[2],secondLine)
        Libraries.append(newLibrary)

    return Libraries


def BookParser(book_info,num_book):

    Books = []
    for i in range(num_book):
        newBook = Book(i,book_info[i])
        Books.append(newBook)

    return Books

#
# filename = "a_example.txt"
#
# Input = read_file(filename)
# NumberOfBooks, NumberOfLibraries, NumberOfDays, BookScores, LibInformations = parse_input(Input)
#
# print(NumberOfBooks)
# print(NumberOfLibraries)
# print(NumberOfDays)
# print(BookScores)
# print(LibInformations)
#
# Libraries = LibParser(LibInformations,NumberOfLibraries)
# print(Libraries)
#
# Books = BookParser(BookScores,NumberOfBooks)
#
# for i in Libraries:
#     print(i.lib_id,i.number_books,i.signup_time,i.ship_per_day,i.books)
#
# for i in Books:
#     print(i.id,i.point)