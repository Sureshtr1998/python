# Linear Search

pos = -1

def search(lst, n):
    i=0
    while i < len(lst):
        if n == lst[i]:
            globals()['pos'] = i
            return True
        i += 1
    return False


arr = [5,8,4,6,9,2]
n = 6

if search(arr, n):
    print("Found at {}".format(pos))
else:
    print("Not Found")
# print(arr.index(9))

# Binary Search

# Values must be sorted for binary search

position = -1

def searchBin(lst, n):
    l=0
    u= len(lst)-1

    while l<=u:
        mid = (l+u)//2 # // gives integer

        if lst[mid] == n:
            globals()['position'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid+1
            else:
                u = mid-1

    return False

# Bubble sort


def sort(nums):
    for i in range(len(nums)-1,0,-1): # we are going backwards
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


bs = [5,3,8,6,7,2]

sort(bs)
print(bs)



# Selection sort



def selectionSort(nums):
    for i in range(len(nums)-1):
        minPos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minPos]:
                minPos = j

        nums[i], nums[minPos] = nums[minPos], nums[i]
        print(nums,"Selection Sorting...")

ss = [5,3,8,6,7,2]

selectionSort(ss)
print(ss)
