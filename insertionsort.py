'''
Developed by Vinicius Figueiredo - github.com/mvcf10
Python version used: 3.9.7

This implementation of Insertion Sort algorithm is receive a list of numbers and
return this list sorted. 

For more information about Insergion Sort algorithm I recomend the book Introduction
to Algorithms 4th Edition by Cormen, Leiserson, Rivest and Stein.

'''
def insertionsort(a):
    n = len(a)
    for i in range(n):
        key = a[i]
        j = i - 1
        while (j > -1) & (a[j] > key):
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key
        print("Loop #"+ str(i) + ": the result is a=" + str(a))
    
    return a

a = [5,2,4,6,1,3]
result = insertionsort(a)
print("The list sorted is: " + str(a))

