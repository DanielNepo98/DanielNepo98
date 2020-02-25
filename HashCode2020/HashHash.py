#   Google Hash Code, February 20th 2020
#   Team  Direnubis Hashcode Implementation
#   Daniel Nepomechie & David Hill

import collections

# Read Book IDs from a library, return as tuple for insertion into dict.
# First 3 vals are library traits!
def readIDs(line, booktypes, signupdays, booksperday):
    idlist = [booktypes, signupdays, booksperday]
    for item in line:
        item = int(item)
        idlist.append(item)
    return tuple(idlist)

# Read input ints from file
def readinput(filename, bookdict, libdict):
    input = open(filename, "r")
    B = -1; L = -1; D = -1;
    # Read first line, assign values
    line = str.split(input.readline())
    i = 0
    for item in line:
        item = int(item)
        # Number of unique books
        if i == 0:
            B = item
        # Number of Libraries
        elif i == 1:
            L = item
        # Number of Days
        else:
            D = item
        i += 1
    params = [B, L, D]

    # Read second line, assign book scores
    line = str.split(input.readline())
    bookid = 0
    for score in line:
        score = int(score)
        bookdict[bookid] = score
        bookid += 1

    N = -1; T = -1; M = -1;
    # Read library entries
    for libid in range(L):
        line = str.split(input.readline())
        i = 0
        for item in line:
            item = int(item)
            # Number of book species present
            if i == 0:
                N = item
            # Time; Days it takes to sign up
            elif i == 1:
                T = item
            # Number of books that can be shipped/scanned/returned per day
            else:
                M = item
            i += 1

        # Begin reading IDs, function will return tuple for given lib
        line = str.split(input.readline())
        libdict[libid] = readIDs(line, N, T, M)

    # Close file
    input.close()
    return params

# Input list of book IDs as tuple from libdict,
# return list of IDs in order from most to least desirable
def scoreeval(bookids, bookdict, scanned):
    # Create list of tuples consisting of ID and score. Sort by score value
    scorelist = []
    for i in range(len(bookids)-3):
        # Remember: First 3 values in tuples are lib properties
        bookid = bookids[i+3]
        # Distinguishes if book has been scanned before adding score!
        if bookid not in scanned.values():
            score = bookdict[bookid]
            scorelist.append((bookid, score))
        # Scores can't be negative. If scanned, mark as -1
        else:
            scorelist.append((-1, -1))

    # Sort tuples by score, highest first
    scorelist = sorted(scorelist, key=lambda t: t[1], reverse=True)
    print("Scorelist: ", scorelist)
    # List of Book IDs, ordered from highest to lowest score
    bookorder = collections.deque()
    for i in scorelist:
        if i[1] != -1:
            bookorder.append(i[0])
        else:
            break
    print("Bookorder: ", bookorder)
    return bookorder

#   Determine score per day for EVERY library that has not yet been signed up. Will call when a signup is completed
#   Returns list of IDs, highest fitness first
def libseval(numlibraries, libdict, bookdict, scanned):
    # List of tuples: (ID, Library's FitnessScore)
    libfitness = []

    # For each library, look at every book in tuple (value in libdict)
    # Determine scores from book IDs, determine score/day for library
    for libid in range(numlibraries):
        # Check to see lib has been signed up
        if libid not in scanned.keys():
            totalscore = 0
            # Note: booktypes at present doesn't change, even if book has already been stored.
            booktypes = len(libdict[libid])-3
            signupdays = libdict[libid][1]
            scansperday = libdict[libid][2]
            for i in range(booktypes):
                # Remember: First 3 values in tuples are lib properties. Using this measure allows dynamism
                bookid = libdict[libid][i+3]
                # Checks to see if book has been scanned already
                if bookid not in scanned.values():
                    totalscore += bookdict[bookid]

            # Fitness function
            totaltransferdays = signupdays + (booktypes / scansperday)
            scoreperday = totalscore / totaltransferdays
            libfitness.append((libid, scoreperday))
        else:
            # If libid has been signed up,
            libfitness.append((libid, -1))

    # Sort tuples by score, highest first
    libfitness = sorted(libfitness, key=lambda t: t[1], reverse=True)
    # List of library IDs, ordered from highest to lowest fitness functions
    liborder = collections.deque()
    for i in libfitness:
        if i[1] != -1:
            liborder.append(i[0])
        else:
            break
    print("Liborder: ", liborder)
    return liborder


# Formatted Output
def printout(scanned):
    print("==Output==")
    # Line # of libraries to sign up
    numscanned = len(scanned.keys())
    print(numscanned)

    # Subseuqently, describe each library _in the order that you want them to start the signup process_.
    # 	First line: ID of library), K (# of books to be scanned from Y)
    # 	Second: IDs of books _in order that they are scanned_
    for i in range(numscanned):
        targetlib = scanned.popitem()
        targetlibid = int(targetlib[0])
        targetlibnumvalues = len(targetlib[1])
        print(targetlibid, ' ', targetlibnumvalues)
        for i in range(targetlibnumvalues):
            print(targetlib[1][i], end=' ')
        print()

def Main():
    # Hash table: Keys book IDs, value score
    bookdict = {}
    # Hash table: Keys lib ID, value tuple of book properties + IDs
    # libdict value format: [booktypes, signupdays, booksperday, IDs]
    libdict = {}

    # Fill books and library, return global params
    params = readinput("a_example.txt", bookdict, libdict)
    numbooktypes = params[0]
    numlibraries = params[1]
    totaldays = params[2]

    # Items that have been scanned Keys are libraries that have been signed up, values are books scanned from library
    scanned = collections.OrderedDict()
    # Will contain list of most -> least desirable library IDs
    signuporder = collections.deque()
    signuporder = libseval(numlibraries, libdict, bookdict, scanned)
    # Will contain order of books: Pops from 0th index
    bookorder = collections.deque()
    # ID of library that is being signed up; -1 indicates none
    signing = -1
    # Date signing process complete
    signcomplete = -1

    # Day cycle - turn into function later maybe?
    for day in range(totaldays):
        # Checks for signup process activity. -1 if not in progress, otherwise ID of library
        if signing == -1 and len(signuporder) != 0:
            signuporder = libseval(numlibraries, libdict, bookdict, scanned)
            signing = signuporder.popleft()
            signupdays = libdict[signing][1]
            signcomplete = day + signupdays
        if day == signcomplete:
            scanned[signing] = ()
            signing = -1

        # Book scanning process - scans from signedup libraries
        # Note: scanned values are tuple. Temporary transformation to list to be modified
        for scanninglib in scanned.keys():
            booksperday = libdict[scanninglib][2]
            bookids = libdict[scanninglib]
            # Returns indexes of most desirable books. scoreeval checks for and prevents duplication
            bookorder = scoreeval(bookids, bookdict, scanned)
            if len(bookorder) >= 1:
                bookstoadd = list(scanned[scanninglib])
                for i in range(booksperday):
                    bookstoadd.append(bookorder.popleft())
                    # UPDATE ORIGINAL BOOKIDS; DETRACT FROM LIBDICT TUPLE
                    libdict[scanninglib] = tuple(bookorder)
                scanned[scanninglib] = tuple(bookstoadd)
                print(tuple(bookstoadd))
                print(libdict[scanninglib])

    printout(scanned)

if __name__ == '__main__':
        Main()