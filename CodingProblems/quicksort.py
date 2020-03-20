import math

def printarr(inputarr):
    for i in range(len(inputarr)):
        print(inputarr[i], end=' ')
    print()

def quicksort(wholearr, startdex, endex):
    # Determines appropriate midpoint between start and end
    # Receives leftmost of partition; smallest unsorted index
    index = medpartition(wholearr, startdex, endex)

    print("\nIndex: "+str(index))
    print("newstartdex: "+str(startdex))


    if startdex < index-1:
        quicksort(wholearr, startdex, index-1)
        print("Left sorted\n")

    # Sort right half
    if endex > index:
        quicksort(wholearr, index, endex)
        print("Right sorted\n")


def medpartition(wholearr, leftdex, rightdex):
    # Pivot picked to be roughly median
    pivotindex = math.floor((leftdex + rightdex) / 2)
    pivot = wholearr[pivotindex]
    print("Pivot: "+str(pivot)+" Startdex: "+str(leftdex)+" Endex: "+str(rightdex))


    # while inside partition
    while leftdex <= rightdex:
        # Iterate through arr until find element on left that should be to right of pivot
        # Record index
        while wholearr[leftdex] < pivot:
            leftdex += 1

        # Iterate through arr from right until find element that should be to left of pivot
        while wholearr[rightdex] > pivot:
            rightdex -= 1

        # Swap the discovered elements, move indices towards center
        if leftdex <= rightdex:
            # Print swap info
            printarr(wholearr)
            print("swap")
            print("leftdex: "+str(leftdex)+" rightdex: "+str(rightdex))

            temp = wholearr[leftdex]
            wholearr[leftdex] = wholearr[rightdex]
            wholearr[rightdex] = temp
            leftdex += 1
            rightdex -= 1
            # View swapped array
            printarr(wholearr)

        # Return leftdex - left bound. Lets right bound remain the end of the array.
        return leftdex



if __name__ == '__main__':
    samplearr = [6,1,4,3,2,1,0]
    samplearr = [0,5,4,3,2,6,0]
    samplelen = len(samplearr)
    print("Sample: ")
    printarr(samplearr)
    print("___________")

    quickarr = samplearr
    quicksort(samplearr, 0, samplelen-1)
    print("\nQuicksorted:")
    printarr(quickarr)
