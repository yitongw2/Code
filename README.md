# Code
A library of some interesting algorithms, data structure implementations or just random stuff learnt in/out of school

# Algorithm 


* Graham Scan
  - Convex Hull
    - given a collection of (x, y) coordinate pairs (points), find the set of points that surround all points within the shape
      that they form so that any line segments between any two interior points stays inside the shape.
    - can be also visualized by taking the union of all triangles formed by any 3 points.
  - Left turn? Right turn? Straight?
    - given 2 point p(x1, y1), q(x2, y2)
    - assume add another point r(x3, y3)
    - connect point p and q, extend the line segment to a straight line 
    - a left turn happens when the line segment q-r can be obtained by rotating the straight line counter-clockwisely
        
        ![screen shot 2016-11-26 at 10 07 28 pm](https://cloud.githubusercontent.com/assets/13974845/20645980/d1f52cb4-b424-11e6-8812-00b7a3a6e1b4.png)
        
    - a right turn happens when the line segment q-r can be obtained by rotating the straight line clockwisely
        
        ![screen shot 2016-11-26 at 9 57 20 pm](https://cloud.githubusercontent.com/assets/13974845/20645954/76f28b5a-b423-11e6-977c-8092be92ada9.png)

    
  

    
    
* Comparison-based sort 
  * Priority-queue sort (concept)
    * idea: to push all elements into a priority queue ranked by their keys and pop from the priority queue.
    * pseudo code: 
      
      Given a collection C of n items to be sorted and a priority queue Q,
      
          for i <-- 0 to n do
      
              Q.insert(C[i])
        
          for i <-- 0 to n do
      
              C[i] <-- Q.removeMin()
        
    * implementation determines the time complexity as well as memory usage
 
 
  * Insertion sort
    - given a collection of n items A to be sorted
    - essentially, a priority-queue sort
    - implement priority queue as a sorted list 
    - removeMin() takes O(1) time
    - insert() takes O(n) time
    - time complexity:
      * worst case: O(n^2)
      * best case: O(n) (already sorted)
    - can be implemented as in-place sorting by keeping the sorted region at the start of the collection and
      gradually expands toward the unsorted area until the whole list is sorted
    - Python code: https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py
    
  * Selection sort 
    - given a collection of n items A to be sorted
    - essentially, a priority-queue sort
    - implement priority queue as an unsorted list 
    - insert() takes O(1) (simply add the key to the end of list)
    - removeMin() takes O(n) (loop through the while list for the minimum)
    - time complexity: O(n^2) (sorted or not)
    - can can implemented as in-place sorting by swapping the smallest key found so far with the key at the beginning
    - Python code: https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py

  * Heap sort
    - given a collection of n items A to be sorted
    - essentially, a priority-queue sort
    - implement priority queue as a heap (details about heap is available in data structure section)
    - time complexity: O(nlogn) (using heapify instead of insertion to construct heap boosts the process by a constant factor
      but the o notation remains the same since the high order is nlogn)
    - Python code: https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py
    
      
    
   

# Data structure

* Heap (Min Heap)
  - a binary tree data structure that satisifies the heap property
  - heap-order proprty: the key of parent node should be less than (grater than if max heap)the key of any child node
  - complete-binary property: each level of heap must be filled untill any elements can be inserted to next level
  - height of heap = ceiling(log2(n+1))
  - level numering(1-based index):
    * parent node: i
    * left node: 2*i
    * right node: 2*i+1
  - time coplexity:
    * heapify(): O(2*n)
    * insert(): O(logn)
    * removeMin(): O(logn)
  - Code: https://github.com/yitongw2/Code/blob/master/data_structure/heap.py


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
              
              
              
              
 

* Matrix determinant
  - given a n x n matrix, calculate its determinant 
  - for 2 x 2 matrix, [[a, b], [c, d]]  simply calculate a*d-b*c
  - for n x n matrix, use cofactors and mirrors of the matrix to break it down to the sum of cofactor * det(submatrix)
  - more details on how to obtain the determinant for n x n matrix (n>2): https://people.richland.edu/james/lecture/m116/matrices/determinant.html
  - assume that each row of the given matrix is in the same size
  - recursive function {base case : 2x2 matrix}
                       {recurrence : cofactor1*det(submatrix1)+...cofactork*det(submatrixk)}
  - Code: https://github.com/yitongw2/Code/blob/master/algorithm/matrix_determinant.py
  
  
  
  
