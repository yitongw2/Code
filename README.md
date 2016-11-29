# Code
A library of some interesting algorithms, data structure implementations or just random stuff learnt in/out of school

## Index
- [Algorithm](https://github.com/yitongw2/Code/blob/master/README.md#algorithm)
    - [Graham Scan](https://github.com/yitongw2/Code/blob/master/README.md#graham-scan)
    - [Dynamic Programming](https://github.com/yitongw2/Code/blob/master/README.md#dynamic-programming)
    - [Comparison-based Sort](https://github.com/yitongw2/Code/blob/master/README.md#comparison-based-sort)
       * [Insertion sort](https://github.com/yitongw2/Code/blob/master/README.md#insertion-sort)
       * [Selection sort](https://github.com/yitongw2/Code/blob/master/README.md#selection-sort)
       * [Heap sort](https://github.com/yitongw2/Code/blob/master/README.md#heap-sort)
- [Data Structure](https://github.com/yitongw2/Code/blob/master/README.md#data-structure)
    - [Heap](https://github.com/yitongw2/Code/blob/master/README.md#heap-min-heap)
- [Problems](https://github.com/yitongw2/Code/blob/master/README.md#interesting-coding-problems)
    - [0-1 Knapsack problem](https://github.com/yitongw2/Code/blob/master/README.md#0-1-knapsack-problem)
    - [Fractional Knapsack problem](https://github.com/yitongw2/Code/blob/master/README.md#fractional-knapsack-problem)
    - [Longest common sequence](https://github.com/yitongw2/Code/blob/master/README.md#longest-common-sequence)
    - [2 Sum problem](https://github.com/yitongw2/Code/blob/master/README.md#2sum)
    - [Matrix Determinant](https://github.com/yitongw2/Code/blob/master/README.md#matrix-determinant)
      

# Algorithm 

##  Graham Scan
  - Convex Hull
    - given a collection of (x, y) coordinate pairs (points), find the set of points that surround all points within the shape
      that they form so that any line segments between any two interior points stays inside the shape.
    - the following graph contains 16 uniquely located points and the bold line segments form the convex hull for these 16           points.
      
         ![screen shot 2016-11-27 at 1 37 02 pm](https://cloud.githubusercontent.com/assets/13974845/20652034/b0bdf184-b4a6-11e6-896b-658b84524238.png)

    - can be also visualized by taking the union of all triangles formed by any 3 points.
    
         ![screen shot 2016-11-27 at 1 43 57 pm](https://cloud.githubusercontent.com/assets/13974845/20652076/a5318c58-b4a7-11e6-8df2-72e4dd310e8d.png)
      
  - Left turn? Right turn? Straight?
    - given 2 point p(x1, y1), q(x2, y2)
    - assume add another point r(x3, y3)
    - connect point p and q, extend the line segment to a straight line 
    - a left turn happens when the line segment q-r can be obtained by rotating the straight line counter-clockwisely with 180       degree
        
        ![screen shot 2016-11-26 at 10 07 28 pm](https://cloud.githubusercontent.com/assets/13974845/20645980/d1f52cb4-b424-11e6-8812-00b7a3a6e1b4.png)
        
    - a right turn happens when the line segment q-r can be obtained by rotating the straight line clockwisely with 180 degree
        
        ![screen shot 2016-11-26 at 9 57 20 pm](https://cloud.githubusercontent.com/assets/13974845/20645954/76f28b5a-b423-11e6-977c-8092be92ada9.png)

    - more mechanical way to determine left/right turn: Matrix determinant
    - assume a matrix below, p(x1, y1), q(x2, y2), r(x3, y3)
      
      [x1,  y1,  1]
      
      [x2,  y2,  1]
       
      [x3,  y3,  1]

    - it turns out that the determinant of the matrix indicates the turning of p-q-r
       - if det(matrix)=0, then p-q-r straight
       - if det(matrix)<0, then p-q-r turns right
       - if det(matrix)>0, then p-q-r turns left
  - Top half of convex hull
    - easy to locate the upper half of the convex hull by putting the point with larger y coordinate in front when sorting the
      points.
    - can apply the algorithm that finds the upper half of the convex hull to the bottom half of the convex hull by 
      simply reversing the y coordinates of all points.
  - Pesudo code for top half of the convex hull:
      
      Given a collection of n points C, 
      
                sort C by their x coordinate (if tie occurs, choose the point with larger y coordinate before the other one)
                initialize an empty stack
                for i<--0 to n do
                  if stack.size() < 2 then
                    stack.push(C[i])
                  else
                    while (the last two points in stack and C[i] forms a left turn)
                      stack.pop()
                    stack.push(C[i])
                return stack 
  - time complexity: 
    - O(n) for integer sorting/O(nlogn) for comparison-based sorting
    - O(n) times repetition * O(1) for push, pop...
    - (since the nested while loop can at most pop n points at the end of day, it won't change the order of the for loop)
    - in total: O(n)/O(nlogn)
  - [Python Code](https://github.com/yitongw2/Code/blob/master/algorithm/graham_scan.py) 
  
  
## Dynamic Programming 
  - idea: 
    
    1, solve a problem by breaking the problem into simple subproblems (recurrence)
    
    2, solve the subproblem and store it in a memory-based data structure (memoization)
    
  - recurrence 
    * a recurrence forumla that describes how the value for a larger argument can be obtained by computing with values for
      smaller arguments.
    * base case: when the argument is small enough, it calculates the result rather than breaking it down to smaller 
      subproblems
    * e.g. recurrence for Fibonacci numbers
      - F(n)=F(n-1)+F(n-2), for n>=2
      - F(0)=F(1)=1, otherwise
  - memoization
    * optimization technique that stores the result of a particular recursive subproblem in a memory-based data structure           (list or dict in Python, hash table in general)
    * once the result is stored in the data structure, it can be easily fetched.
    * using memoization saves the time from expensive recursive calls
    * e.g. memoization table used in finding Fibonacci number
            ![screen shot 2016-11-27 at 11 54 12 am](https://cloud.githubusercontent.com/assets/13974845/20651351/6eb49512-b498-11e6-8b1e-1756eb8df60e.png)
    * downside: can be complicated to fetch the trace
  - Example of dynamic programming:
    * longest common sequence problem (more details [here](https://github.com/yitongw2/Code/blob/master/README.md#longest-common-sequence))
                  

    
## Comparison-based sort 
  * Priority-queue sort (concept)
    * idea: to push all elements into a priority queue ranked by their keys and pop from the priority queue.
    * pseudo code: 
      
      Given a collection C of n items to be sorted and a priority queue Q,
      
          for i <-- 0 to n do
      
              Q.insert(C[i])
        
          for i <-- 0 to n do
      
              C[i] <-- Q.removeMin()
        
    * implementation determines the time complexity as well as memory usage
 
 
### Insertion sort
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
  - [Python code](https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py)
    
### Selection sort 
  - given a collection of n items A to be sorted
  - essentially, a priority-queue sort
  - implement priority queue as an unsorted list 
  - insert() takes O(1) (simply add the key to the end of list)
  - removeMin() takes O(n) (loop through the while list for the minimum)
  - time complexity: O(n^2) (sorted or not)
  - can can implemented as in-place sorting by swapping the smallest key found so far with the key at the beginning
  - [Python code](https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py)

### Heap sort
  - given a collection of n items A to be sorted
  - essentially, a priority-queue sort
  - implement priority queue as a heap (details about heap is available in data structure section)
  - time complexity: O(nlogn) (using heapify instead of insertion to construct heap boosts the process by a constant factor
    but the o notation remains the same since the high order is nlogn)
  - [Python code](https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py)
    
      
    
   

# Data structure

## Heap (Min Heap)
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
  - [Code](https://github.com/yitongw2/Code/blob/master/data_structure/heap.py)


# Interesting coding problems

## 0-1 Knapsack problem
  - Given a collection C of items each has a numeric size and a numberic value, a number L as the limit of total size, find a     combination of items that maximizes the total value and yet keep the total size under the limit L. 
  - can each take all of the item or none of it into the combination
  - idea: dynamic programming
    * breaking the problem into subproblems
    * if we include the ith item into the combination, then the subproblem is looking for the next item to be included with a 
      a reduced total size.
    * if we do not include the ith item into the combination, then the subproblem is looking for the next item to be included
      with an unchanged size
    * a table K containing solutions(values) to all subproblems, starting at i th item and with a size limit s
    * recurrence formula:
      - K[i][0]=0 or K[0][s]=0  (base case).
      - K[i][s]=value(i) + K[i-1][s-size(i)]  (include ith item).
      - K[i][s]=K[i-1][s]  (not include ith item).
    * how to choose the right item to include?
      - choose the one that maximizes the value of the solution
      - max(value(i)+K[i-1][s-size(i)], K[i-1][s])
    * pesudo code:
    
                          init a 2D list table K
                          for i <-- 0 to n do
                            for s <-- 0 to L do
                              if i = 0 or s = 0 then
                                K[i][s]=0
                              else
                                K[i][s]=max(value(i)+K[i-1][s-size(i)], K[i-1][s])
                           trace back to recover the combination of items
     * [Code]()
  
  
## Fractional Knapsack problem
  - Given a collection C of items each has a numeric size and a numberic value, a number L as the limit of total size, find a     combination of items that maximizes the total value and yet keep the total size under the limit L. 
  - can take part of an item (fractional) into the combination. 
  - e.g. item B has size of 2 and value of 3, the result can include item B with size of 1 and value of 3/2.
  - Solution (greedy approach):
  
      example table of 7 items
      
      ![screen shot 2016-11-28 at 1 25 49 pm](https://cloud.githubusercontent.com/assets/13974845/20686870/1750516c-b56f-11e6-9a1e-67b644d8a98d.png)
    1. sort the items by their value per size (value/size)
    2. loop through sorted items
    3. if there is any remaining space, include all of the item or part of it to the solution depending on which one is
       smaller and decrement the remaining space by the size included in the solution
    4. otherwise, the knapsack is full, return the solution.
  - [Code](https://github.com/yitongw2/Code/blob/master/solutions/knapsack.py)
    
  

## Longest common sequence
  - given 2 string X and Y (in general, can be array of char, int or other. for this problem, assume they are string 
    in Python), find a subsequence that appears in both of them (do not have to be consecutive) and it must be as long as         possible.
  - Solution (dynamic programming):
    * derive a recurrence
      * let table[i][j] denote the number of common chars found between first i chars of X and first j chars of Y
      * when the last char of X, Y match, can be sure that the last char is in the common sequence
      * otherwise, either match first i chars of X with firt j-1 chars of Y or match first i-1 chars of X with first
        j chars of Y. Since the common sequence should as long as possible, choose the case where there are more common
        chars. 
    * pesudo code:
      
                        initialize a 2D list L
                        
                        m <-- the length of X
                        
                        n <-- the length of Y
                        
                        for i <-- 0 to m do
                          
                          for j <-- 0 to n do
                            
                             if i = 0 or j = 0 then   // base case
                                
                                L[i][j]=0
                             
                             else if X[i-1] = Y[j-1] then
                              
                                L[i][j] <-- 1+L[i-1][j-1]
                             
                             else
                                
                                L[i][j] <-- max(L[i-1][j], L[i][j-1])
                         
                         track the trace in the table from bottom right corner and obtain the common sequence
    * time complexity: O(n^2)
    * [Code](https://github.com/yitongw2/Code/blob/master/solutions/lcs.py)
                         
                                

## 2 sum
  - given an array of integers, return indices of the two numbers such that they add up to a specific target.
  - assume only one matching pair in the array
  - example. l = [2, 1, 5, 4, 9], tartget = 9
             expected output [2, 3]
  - Solution 1:
  
    1, use a hash table to hash all values in the array
    
    2, looping through the array from 0 to length of the array-1
    
    3, for each loop, find the target-array[i] in hash table
    
    4, if found during the loop, return the pair; otherwise, such pair does not exist.
    
    * Time complexity: 
    
      * O(n) for putting n elements in to hash table
    
      * O(n) at most for looping the array, each lookUp operation takes O(1) time.
    
      * total = O(n) 
    
    * Memory usage: 
    
      * O(n) for hash table (depending on implmentation)
    
    * [Code](https://github.com/yitongw2/Code/blob/master/solutions/twoSum.java)
              
              


## Matrix determinant
  - given a n x n matrix, calculate its determinant 
  - Solution: 
    - for 2 x 2 matrix, [[a, b], [c, d]]  simply calculate a*d-b*c
    - for n x n matrix, use cofactors and mirrors of the matrix to break it down to the sum of cofactor * det(submatrix)
    - more details on [how to obtain the determinant for n x n matrix](https://people.richland.edu/james/lecture/m116/matrices/determinant.html)
    - assume that each row of the given matrix is a square matrix
    - recursive function {base case : 2x2 matrix}
                         {recurrence : cofactor1*det(submatrix1)+...cofactork*det(submatrixk)}
    - [Code](https://github.com/yitongw2/Code/blob/master/algorithm/matrix_determinant.py)
  
  
  
  
