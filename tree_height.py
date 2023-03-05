# python3
import time
import sys
import threading
import numpy


def compute_height(sakne, liste):
    # Write this function
    # Your code here
    if not liste[sakne]:
        return 1
    else:
        return 1 + max ([compute_height(berns, liste) for berns in liste[sakne]])
    

#1
def main():
    
    # implement input form keyboard and from files
    TEST= input()
    decis = input()
    # print()
    if decis == "F":
        file= input()
        t1 = time.time()
        if "a" in file:
            return
        with open(f"./test/{file}", mode="r") as file:
            n=int(file.readline())
            parents = list(map(int, file.readline().split(" ")))
        liste = [[] for i in range(n)]
        for i in range(n):
            if int(parents[i]) == -1:
                sakne = i
            else:
                liste[parents[i]].append(i)

        #print(compute_height(sakne, liste))
        t2 = time.time()
        #print(t2 - t1)
        #print()
        
    elif decis == "I":
        n = int(input())
        parents = input()
        t1 = time.time()
        split_parents = list(map(int, parents.split(" ")))
        
        liste = [[] for i in range(n)]
        for i in range(n):
            if split_parents[i] == -1:
                sakne = i
            else:
                liste[split_parents[i]].append(i)
        
        #print(compute_height(sakne, liste))
        #print()
        t2 = time.time()
        #print(t2 - t1)
    else:
        return
    print(compute_height(sakne, liste))
        # Lala
    # Printing answer, write your code here'
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))