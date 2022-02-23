# Geeks for Geeks - medium

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, i, n):
        # code here
        # self.heapUp(arr,i,n)
        self.heapDown(arr,i,n)
         
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2, -1 , -1):
            self.heapify(arr, i, n)
        # print(arr,"arr")
        
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        #code here
        t = n-1
        while t >= 0:
            self.remove(arr,0,t)
            t -= 1
        # print(arr,"sorted")
        
            
        
    def heapUp(self,arr, i , n):
        parent = self.parent(i)
        right = self.rightChild(parent)
        if right >= n:  # the new element is added as left child
            if arr[parent] < arr[i]:
                self.swap(arr,i,parent)
                
        else:  # if the new element is added as right element
            left = self.leftChild(parent)
            largest = left
            if arr[right] > arr[largest]:
                largest = right
            if arr[parent] < arr[largest]:
                self.swap(arr,parent,largest)
        if parent >= 0:
            self.heapUp(arr,parent,n)
            
            
            
        
        # iterative 
        # while i >= 0:
        #     parent = self.parent(i)
        #     right = self.rightChild(parent)
        #     if right >= len(arr):
        #         if arr[parent] > arr[i]:
        #             arr[i], arr[parent] = arr[parent], arr[i]
        #     else:
        #         left = self.leftChild(parent)
        #         if arr[right] < arr[left]:
        #             arr[right], arr[parent] = arr[parent], arr[right]
        #         else:
        #             arr[left], arr[parent] = arr[parent], arr[left]
        #     i = self.parent(i)
            
    def heapDown(self,arr, i, n):
        parent = i
        left = self.leftChild(i)
        right = self.rightChild(i)
        
        if left >= n:
            return
        if right >= n:  # if the parent has only left child
            if arr[parent] < arr[left]:
                self.swap(arr,left,parent)
        else:
            largest = left
            if arr[right] > arr[largest]:
                largest = right
            if arr[parent] < arr[largest]:
                self.swap(arr,parent,largest)
                self.heapDown(arr,largest,n)
            
            
        
        # iterative approach
        # while i >= len(arr):
        #     left = self.leftChild(i)
        #     right = self.rightChild(i)
        #     if left >= len(arr):
        #         return
        #     if right >= len(arr):
        #         if arr[left] > arr[i]:
        #             arr[i], arr[left] = arr[left], arr[i]
        #     else:
        #         if arr[right] < arr[left]:
        #             arr[right], arr[i] = arr[i], arr[right]
        #             i = self.rightChild(i)
        #         else:
        #             arr[left], arr[i] = arr[i], arr[left]
        #             i = self.leftChild(i)
    
    def insert(self,arr, element):
        
        arr.append(element)
        i = len(arr) - 1
        n = len(arr)
        self.heapUp(arr,i,n)
        
            
    def remove(self, arr, index, n):
        lastIndex = n 
        if n > 0:
            self.swap(arr,index,lastIndex)
        self.heapDown(arr, index, n)
        
        
    def update(self, arr, index, element):
        arr[index] = element
        
        
    def getMin(self,arr):
        return arr[0]
        
    def leftChild(self, index):
        return index * 2 + 1
    def rightChild(self, index):
        return index * 2 + 2
    def parent(self, index):
        return (index - 1) // 2
        
    def swap(self, arr, index1, index2):
        arr[index1],arr[index2] = arr[index2],arr[index1]
