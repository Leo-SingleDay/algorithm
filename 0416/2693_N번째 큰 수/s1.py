import sys
sys.stdin = open('input.txt')

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


for T in range(1, int(input())+1):
    num_arr = list(map(int,input().split()))
    bubble_sort(num_arr)
    print(num_arr[2])


