def square(arr):
    for i in range(len(arr)):
        print(arr[i]**2,end="\t")
arr=list(map(int,input().split()))
square(arr)

