class Square:
    def __init__(self, squarearray):
        self.squarearray = squarearray
        self.side = len(squarearray)
        self.numterms = self.side ** 2
        self.magic = int(self.side * (self.side ** 2 + 1) / 2)

        self.terms = {}
        self.unusedterms = {}
        self.repeatterms = {}

        self.rowsums = [0] * self.side
        self.colsums = [0] * self.side
        self.diagsums = [0] * 2

        self.diagpaths = [[], []]
        for i in range(self.side):
            self.diagpaths[0].append((i, i))
            self.diagpaths[1].append((i, self.side - 1 - i))

    def __call__(self):
        return self.squarearray

    def getterms(self):
        # Range is left but not right inclusive, hence+1
        for i in range(1, self.numterms + 1):
            self.unusedterms[i] = 1

        # Determine occurrence of unused and repeated terms
        rowindex = 0
        for row in self.squarearray:
            colindex = 0
            # Record item from matrix
            for item in row:
                # If new, remove from dict of unused and record loc
                if item not in self.terms.keys():
                    del self.unusedterms[item]
                    # Initialized as tuple of tuples - for future appends
                    self.terms[item] = ((rowindex, colindex),)
                # If term is repeated:
                else:
                    # Converts tuple to list for easy append
                    self.repeatterms[item] = self.terms[item]
                    temp = list(self.repeatterms[item])
                    temp.append((rowindex, colindex))
                    self.repeatterms[item] = tuple(temp)
                    self.terms[item] = tuple(temp)



                # Update sums
                self.colsums[colindex] += item
                self.rowsums[rowindex] += item

                colindex += 1
            rowindex += 1


    def updatesums(self):
        self.rowsums = [0] * self.side
        self.colsums = [0] * self.side
        self.diagsums = [0] * 2

        rowindex = 0
        for row in self.squarearray:
            colindex = 0
            for item in row:
                self.colsums[colindex] += item
                self.rowsums[rowindex] += item
                colindex += 1
            rowindex += 1

        for i in range(self.side):
            self.diagsums[0] += self.squarearray[i][i]
            self.diagsums[1] += self.squarearray[i][self.side - 1 - i]

        return {'rowsums':tuple(self.rowsums), 'colsums':tuple(self.colsums), 'diagsums':tuple(self.diagsums)}


    def printinfo(self):
        print("\nTerms: " + str(self.terms))
        print("Repeats: " + str(self.repeatterms))
        print("Unused: " + str(self.unusedterms))

        for row in self.squarearray:
            for item in row:
                print(item, end=' ')
            print()

        print("Rowsums: " + str(self.rowsums))
        print("Colsums: " + str(self.colsums))
        print("Diagsums: " + str(self.diagsums))
        print("Diagpaths: " + str(self.diagpaths))

    # Determines areas containing repeated terms
    def touched(self):
        touched = {'row': (), 'col': (), 'diag': ()}

        for key in self.repeatterms.keys():
            for val in self.repeatterms[key]:
                if val in self.diagpaths[0]:
                    temp = list(touched['diag'])
                    temp.append(0)
                    touched['diag'] = tuple(temp)
                elif val in self.diagpaths[1]:
                    temp = list(touched['diag'])
                    temp.append(1)
                    touched['diag'] = tuple(temp)

                temp = list(touched['row'])
                temp.append(val[0])
                touched['row'] = tuple(temp)

                temp = list(touched['col'])
                temp.append(val[1])
                touched['col'] = tuple(temp)

        return(touched)
