import math

def printarr(inputarr):
    for i in range(len(inputarr)):
        print(inputarr[i], end=' ')
    print()

def merge(wholearr, startindex, midindex, endindex):
    llen = midindex - startindex + 1
    # consider len7: mid=0+6/2 = 3; 4th element. 3-0 = 3; should be 1 longer!
    # left side always longer if uneven due to indexing
    #consider len6: mid=0+5/2 = 2. Should be +1! real leftlen is 3

    rlen = endindex - midindex
    #continuing len7: 6-3 = 3
    #continuing len6: 6-3 = 3. Correct

    #slicing unreliable due to typing, but notation helpful. Recall night right-inclusive
    #leftarr = wholearr[startindex:midindex+1]
    #rightarr = wholearr[midindex+1:endindex+1]
    leftarr = [0]*llen
    rightarr = [0]*rlen
    for i in range(llen):
        leftarr[i] = wholearr[startindex+i]
    for i in range(rlen):
        rightarr[i] = wholearr[midindex+1+i]

    print("left: ", end='')
    printarr(leftarr)
    print("right: ", end='')
    printarr(rightarr)

    lindex = 0
    rindex = 0

    # merge has sorted everything prior to the started point (or will be sorted before merge)
    sortdex = startindex
    # iterates through left and right arrays. If left smaller than right, put, else, right put into whole
    while lindex < llen and rindex < rlen:
        if leftarr[lindex] <= rightarr[rindex]:
            wholearr[sortdex] = leftarr[lindex]
            lindex += 1
        else:
            wholearr[sortdex] = rightarr[rindex]
            rindex += 1
        sortdex += 1

    # Conditions for if the the two arrays aren't the same size:
    while lindex < llen:
        wholearr[sortdex] = leftarr[lindex]
        lindex += 1
        sortdex += 1

    while rindex < rlen:
        wholearr[sortdex] = rightarr[rindex]
        rindex += 1
        sortdex += 1
    #View array
    printarr(wholearr)


def mergesort(wholearr, startindex, endindex):
    # condition fails when start and end indcies are the same; min of analysis arr size 2
    if startindex < endindex:
        midindex = math.floor((startindex + endindex) / 2)
        # Floor ensures will still be middle value.
        # endindex is len-1. Consider len 6: 0+5/2 = 2.5-> index 2. len7 6/2 = 3
        # Therefore right side will always be smaller if uneven. Righthalf mid+1 necessary start

        # left and right inclusive
        mergesort(wholearr, startindex, midindex)
        mergesort(wholearr, midindex+1, endindex)

        merge(wholearr, startindex, midindex, endindex)
        print("Merge done\n")


if __name__ == '__main__':
    samplearr = [5,4,3,2,1,0]
    samplelen = len(samplearr)
    print("Sample:")
    printarr(samplearr)

    mergearr = samplearr
    mergesort(mergearr, 0, samplelen-1)
    print("Mergesorted:")
    printarr(mergearr)


