import input_part
from math import ceil
totalPoint = 0
###############################################
# Python program for implementation of MergeSort
def mergeSort(arr,ind_arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves
        ind_L = ind_arr[:mid]
        ind_R = ind_arr[mid:]

        mergeSort(L,ind_L)  # Sorting the first half
        mergeSort(R,ind_R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                ind_arr[k] = ind_L[i]
                i += 1
            else:
                arr[k] = R[j]
                ind_arr[k] = ind_R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            ind_arr[k] = ind_L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            ind_arr[k] = ind_R[j]
            j += 1
            k += 1

        return arr,ind_arr




class World:

    def __init__(self,libs=[],books=[] , num_days = 0):
        self.libs = libs
        self.usedLibs = []
        self.books = books
        self.lifetime = num_days
        self.passed_day = 0
        self.liblist = []
        self.libbook = []
        self.libbook2 = []
        self.usedBooks = set()

    def advantageCalculator(self):
        self.LibPoints = []
        num = -1
        for library in self.libs:
            num+=1
            if library in self.usedLibs:
                self.LibPoints.append(-1)
                self.libbook2.append([-1])
                #print("PASSED")
                continue

            library.books = list(set(library.books).difference(self.usedBooks))
            library.number_books = len(library.books)

            if len(library.books) == 0:
                self.libbook2.append([-1])
                self.LibPoints.append(-1)
                #print("PASSED")
                continue
            if self.lifetime-self.passed_day <= 0:
                return True

            workingDay = self.lifetime - library.signup_time - self.passed_day
            if workingDay <=0:
                self.libbook2.append([-1])
                self.LibPoints.append(-1)
                #print("PASSED")
                continue

            scanableDay = ceil((library.number_books)/(library.scan_per_day))
            #print(workingDay, scanableDay)
            if (workingDay >= scanableDay):
                totalScore = 0
                for book in library.books:
                    #print("B",book)
                    totalScore += self.books[book].score
                    self.libbook.append(book)
                #print("TOTAL", totalScore)

                library.workingDay = scanableDay

            else:

                indecies = []
                scores = []

                #print(library.books)
                for book in library.books:
                    indecies.append(book)
                    scores.append(self.books[book].score)



                scores, indecies = mergeSort(scores,indecies)
                ##print(indecies)
                #print("MERGE")
                #print(scores)
                #print("KAAN")
                #print(indecies)
                #library.books = indecies
                totalScore = 0
                for i in range(workingDay*library.scan_per_day):
                    totalScore += scores[-i-1]
                    self.libbook.append(indecies[-i-1])

                #print("MERGE SCORE: ",totalScore)

                library.workingDay = workingDay
            #print("PASSED",self.passed_day)
            self.LibPoints.append(totalScore)
            self.liblist.append(num)
            self.libbook2.append(self.libbook)
            self.libbook = []
            #print(self.liblist)
        #print(self.LibPoints)

        return self.LibPoints

    def nextLib(self):
        global totalPoint
        #print(len(self.usedLibs),len(self.libs))

        #print(self.LibPoints)
        max_value = max(self.LibPoints)
        if max_value == -1:
            return True
        max_index = self.LibPoints.index(max_value)
        totalPoint += max_value
        self.passed_day += self.libs[max_index].signup_time
        #print(self.libbook2[max_index])

        self.usedBooks.update(self.libbook2[max_index])
        #print(self.usedBooks)
        self.libs[max_index].books = self.libbook2[max_index]
        #print(self.libs[max_index].books)
        self.libs[max_index].number_books = len(self.libbook2[max_index])
        self.libbook = []
        self.libbook2 = []
        #print("ULib",self.usedLibs)
        self.usedLibs.append(self.libs[max_index])
        #print(self.libs[max_index])
        #print("ULib",self.usedLibs)



        return self.liblist[max_index]
        #return max_index

    def createOutput(self,filename):

        filename = "out_"+filename
        #print(self.liblist)
        #print("K",self.libbook[0])
        file = open(filename, 'w')
        str2 = str(len(self.usedLibs)) + "\n"
        for i in range(len(self.usedLibs)):
            str2+=str(self.usedLibs[i].lib_id)+" "+str(self.usedLibs[i].number_books)+"\n"
            for j in self.usedLibs[i].books:
                str2 += str(j)+" "
            str2 += "\n"

        file.write(str2)
        file.close()





















###############################################


filename = "d_tough_choices.txt"

Input = input_part.read_file(filename)
NumberOfBooks, NumberOfLibraries, NumberOfDays, BookScores, LibInformations = input_part.parse_input(Input)

Libraries = input_part.LibParser(LibInformations,NumberOfLibraries)

Books = input_part.BookParser(BookScores,NumberOfBooks)


###############################################


Mission = World(Libraries, Books, NumberOfDays)
#print(Mission.liblist)
#print(Mission.LibPoints)
#scores, indecies = mergeSort(Mission.LibPoints,Mission.liblist)
#print(nextLibIndex)
#print(nextLibIndex)

for i in range(NumberOfLibraries):
    flag = Mission.advantageCalculator()
    if flag == True:
        break
    nextLibIndex = Mission.nextLib()
    print(nextLibIndex)
    #print(i)
    #print(i," ",Mission.LibPoints,nextLibIndex)

    if(nextLibIndex == True):
        break


print("finish")
print("Max Point", totalPoint)
Mission.createOutput(filename)

