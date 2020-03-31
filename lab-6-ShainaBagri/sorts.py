import random
import time

def selection_sort(alist):
    start_time = time.time()
    i = 0
    comparisons = 0
    while i<len(alist)-1:
        maxInd = 0
        j = 1
        while j<len(alist)-i:
            if alist[j]>alist[maxInd]:
                maxInd = j
            j += 1
            alist[len(alist)-1-i], alist[maxInd] = alist[maxInd], alist[len(alist)-1-i]
            comparisons += 1
        i += 1
    stop_time = time.time()
    #print("time: ", stop_time - start_time) #determines time of operation
    return comparisons

def insertion_sort(alist):
    start_time = time.time()
    if(len(alist)<2):
        stop_time = time.time()
        #print("time: ", stop_time - start_time) #determines time of operation
        return 0
    i = 1
    comparisons = 0
    while i<len(alist):
        j = i
        while j>0 and alist[j]<alist[j-1]:
            alist[j], alist[j-1] = alist[j-1], alist[j]
            comparisons += 1
            j -= 1
        i += 1
        #accounts for if alist[j]>alist[j-1] is what terminates inner while loop
        if j!=0:
            comparisons += 1
    stop_time = time.time()
    #print("time: ", stop_time - start_time) #determines time of operation
    return comparisons

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

