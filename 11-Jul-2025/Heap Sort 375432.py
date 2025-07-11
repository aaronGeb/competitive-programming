# Problem: Heap Sort - https://practice.geeksforgeeks.org/problems/heap-sort/1

class Solution:
    def heapSort(self, arr):
        #code here
        def heapfiy(arr,n,i):
            max_elm = i
            left = 2*i +1
            right = 2*i + 2
            if left <n and arr[left] > arr[max_elm]:
                max_elm = left
            if right <n and arr[right] > arr[max_elm]:
                max_elm = right
            if max_elm !=i:
                arr[i], arr[max_elm] = arr[max_elm], arr[i]
                heapfiy(arr,n,max_elm)
        n = len(arr)
        for i in range(n//2-1,-1,-1):
            heapfiy(arr,n,i)
        for i in range(n-1,0,-1):
            arr[i], arr[0] = arr[0], arrr[i]
            heapify(arr,i,0)
            