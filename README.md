# Code
A library of some interesting algorithms, data structure implementations or just random stuff learnt in/out of school

# Algorithm 

* Comparison-based sort 
  * Priority-queue sort
    * idea: to push all elements into a priority queue ranked by their keys and pop from the priority queue.
    * pseudo code: 
      
      Given a collection C of n items to be sorted and a priority queue Q,
      
          for i <-- 0 to n do
      
              Q.insert(C[i])
        
          for i <-- 0 to n do
      
              C[i] <-- Q.removeMin()
        
    * implementation determines the time complexity as well as memory usage
 
 
    Insertion sort
    - given a collection of n items A to be sorted
    - implement priority queue as a sorted list 
    - removeMin() takes O(1) time
    - insert() takes O(n) time
    - time complexity:
      worst case: O(n^2)
      best case: O(n) (already sorted)
    - can be implemented as in-place sorting by keeping the sorted region at the start of the collection and
      gradually expands toward the unsorted area until the whole list is sorted
    - Python code: https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py
    
    Selection sort 
    - given a collection of n items A to be sorted
    - implement priority queue as a unsorted list
    - insert() takes O(1)
    
    
      
    
   

# Data structure


# Interesting coding problems

* 2 sum
  - Given an array of integers, return indices of the two numbers such that they add up to a specific target.
  - assume only one matching pair in the array
  - example. l = [2, 1, 5, 4, 9], tartget = 9
             expected output [2, 3]
  
  Solution 1:
  
    1, use a hash table to hash all values in the array
    
    2, looping through the array from 0 to length of the array-1
    
    3, for each loop, find the target-array[i] in hash table
    
    4, if found during the loop, return the pair; otherwise, such pair doesn't exist.
    
    Time complexity: 
    
    O(n) for putting n elements in to hash table
    
    O(n) at most for looping the array, each lookUp operation takes O(1) time.
    
    total = O(n) 
    
    Memory usage: 
    
    O(n) for hash table (depending on implmentation)
    
    Code: https://github.com/yitongw2/Code/blob/master/solutions/twoSum.java
                  
                      
