# Code
A library of some interesting algorithms, data structure implementations or just random stuff learnt in/out of school

## Index
- [Algorithm](https://github.com/yitongw2/Code/blob/master/README.md#algorithm)
    - [Next Permutation in lexicographic ordering](https://github.com/yitongw2/Code/blob/master/README.md#next-permutation-in-lexicographic-ordering)
    - [Graham Scan](https://github.com/yitongw2/Code/blob/master/README.md#graham-scan)
    - [Dynamic Programming](https://github.com/yitongw2/Code/blob/master/README.md#dynamic-programming)
    - [Graph Algorithm](https://github.com/yitongw2/Code/blob/master/README.md#graph-algorithm)
      * [DFS vs BFS](https://github.com/yitongw2/Code/blob/master/README.md#depth-first-search)
      * [Connectivity](https://github.com/yitongw2/Code/blob/master/README.md#connectivity)
      * [Minimum Spanning Tree](https://github.com/yitongw2/Code/blob/master/README.md#minimum-spanning-tree)
        - [Prim-Jarnik Algorithm](https://github.com/yitongw2/Code/blob/master/README.md#prim-jarnik-algorithm)
        - [Kruskal Algorithm](https://github.com/yitongw2/Code/blob/master/README.md#kruskal-algorithm)
        - [Boruvka Algorithm](https://github.com/yitongw2/Code/blob/master/README.md#boruvka-algorithm)
      * [Shortest Path](https://github.com/yitongw2/Code/blob/master/README.md#shortest-path)
        - [Dijkstra Algorithm](https://github.com/yitongw2/Code/blob/master/README.md#dijkstra-algorithm)
        - [Bellman-Ford Algorithm](https://github.com/yitongw2/Code/blob/master/README.md#bellman-ford-algorithm)
    - [Comparison-based Sorting](https://github.com/yitongw2/Code/blob/master/README.md#comparison-based-sort)
       * [Insertion sort](https://github.com/yitongw2/Code/blob/master/README.md#insertion-sort)
       * [Selection sort](https://github.com/yitongw2/Code/blob/master/README.md#selection-sort)
       * [Heap sort](https://github.com/yitongw2/Code/blob/master/README.md#heap-sort)
       * [Quick sort](https://github.com/yitongw2/Code/blob/master/README.md#quick-sort)
       * [Merge sort](https://github.com/yitongw2/Code/blob/master/README.md#merge-sort)
    - [Integer Sorting](https://github.com/yitongw2/Code/blob/master/README.md#integer-sort)
       * [Bucket sort](https://github.com/yitongw2/Code/blob/master/README.md#bucket-sort)
       * [Radix sort](https://github.com/yitongw2/Code/blob/master/README.md#radix-sort) 
    - [Huffman Coding](https://github.com/yitongw2/Code/blob/master/README.md#huffman-coding)
    - [CYK algorithm](https://github.com/yitongw2/Code/blob/master/README.md#cyk-algorithm)
    
- [Data Structure](https://github.com/yitongw2/Code/blob/master/README.md#data-structure)
    - [Union-Find](https://github.com/yitongw2/Code/blob/master/README.md#union-find)
    - [Graph](https://github.com/yitongw2/Code/blob/master/README.md#graph)
    - [Binary Search Tree](https://github.com/yitongw2/Code/blob/master/README.md#binary-search-tree)
    - [AVL Tree](https://github.com/yitongw2/Code/blob/master/README.md#avl-tree)
    - [WAVL Tree](https://github.com/yitongw2/Code/blob/master/README.md#wavl-tree)
    - [Heap](https://github.com/yitongw2/Code/blob/master/README.md#heap-min-heap)
    - [Stack](https://github.com/yitongw2/Code/blob/master/README.md#stack)
- [Problems](https://github.com/yitongw2/Code/blob/master/README.md#interesting-coding-problems)
    - [448. Find All Numbers Disappeared in an Array](https://github.com/yitongw2/Code/blob/master/README.md#find-all-numbers-disappeared-in-an-array-leetcode-448)
    - [354. Russian Envelopes](https://github.com/yitongw2/Code/blob/master/README.md#russian-doll-envelopes-leetcode-354)
    - [461. Hamming Distance](https://github.com/yitongw2/Code/blob/master/README.md#hamming-distance-leetcode-461)
    - [345. Reverse Vowels of a String](https://github.com/yitongw2/Code/blob/master/README.md#reverse-vowels-of-a-string-leetcode-345)
    - [Maximum subarray]()
    - [0-1 Knapsack problem](https://github.com/yitongw2/Code/blob/master/README.md#0-1-knapsack-problem)
    - [Fractional Knapsack problem](https://github.com/yitongw2/Code/blob/master/README.md#fractional-knapsack-problem)
    - [Longest common sequence](https://github.com/yitongw2/Code/blob/master/README.md#longest-common-sequence)
    - [2 Sum problem](https://github.com/yitongw2/Code/blob/master/README.md#2-sum)
    - [Matrix Determinant](https://github.com/yitongw2/Code/blob/master/README.md#matrix-determinant)
      

# Algorithm 
##  Next Permutation in lexicographic ordering
  - permutation in lexicographic ordering
    * ABC is in non-decreasing lexicographical ordering
    * CBA is in non-increasing lexicographical ordering
    * the full ordering of set {A,B,C} of 3 elements : ABC --> CBA
  - problem to be solved
    * given a permutation, compute the lexicographically next greater permutation. 
    * the key idea is to imagine that, for every permutation, there is a suffix of non-increasing elements.

        | index  | 0 | 1 | 2 | 3 | 4 | 5 |
        |---|---|---|---|---|---|---|
        | perm  | 1 | 3 | 5 | 4 | 2 | 0 |
  - suffix in the above example is perm[2:], for permutation of {5,4,2,0}, this permutation already has the highest lexicographical ordering.
  - to configure the next lexicographical ordered permutation, we take the next element 3 into the set and reconfigure an initial permutation for set {5,4,2,0,3}.
    * locate the longest non-increasing sequence by looking for the largest index k that Arr[k]\<Arr[k+1]. If the array Arr is already longest non-increasing sequence, the permutation itself is the highest permutation. 
    * locate the largest item in suffix by looking for the largest index l such that Arr[l]\>Arr[k].
    * swap Arr[l] and Arr[k]
    * reverse the suffix in order to restore the permutation ranking of the suffix to the lowest possible. 
  - [Code](https://github.com/yitongw2/Code/blob/master/algorithm/nextperm.py)        
  
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
    * 0-1 knapsack problem (more details [here](https://github.com/yitongw2/Code/blob/master/README.md#0-1-knapsack-problem))
    * CYK algorithm (more details [here](https://github.com/yitongw2/Code/blob/master/README.md#cyk-algorithm))              
    
## Graph Algorithm    
  ### Depth-first Search
  - [code](https://github.com/yitongw2/Code/blob/master/algorithm/dfs.py)
  ### Breadth-first Search 
  - [code](https://github.com/yitongw2/Code/blob/master/algorithm/bfs.py)
  ### Connectivity
  - Connected
    * a graph is connected when any node can be reached from any other nodes
    * graph with 1 node is connected or even empty is connected
  - Biconnected
    * a graph is biconnected if the graph is connected and removing any single node won't disconnect the graph
    * stronger than connected
    * essentially, for any two nodes, there exists at least 2 disjoint path between them (so that removing any single node
    on either path won't disconnect them)
    * <node1 -- node2> is biconnected because removing one will make a single node, which is connected to itself.
  - Strongly Connected Components
    * a subgraph where where any two vertices can be reached from each other
    * articulation point : if an articulation point is removed, a connected componnent will be disconnected
  - to find all strongly connected components
    * Kosaraju's Algorithm
    * Tarjan's Algorithm
        - each node v keeps (index, lowlink, onstack)
            * index : the depth of v in dfs tree
            * lowlink : the node that could reach v with the lowest index
            * onstack : is the node pushed onto stack
        - pesudocode
                
                           s = empty stack
                           index = 0
                           visited = empty dict
                           def recur_tarjan(G, v, index):
                                v.index = index
                                v.lowlink = index
                                s.push(v)
                                ++index
                                v.onstack = true
                                for w that v->w:
                                    if w is not visited:
                                        recur_tarjan(G, w, index)
                                        v.lowlink = min(v.lowlink, w.lowlink)
                                    else if w is on stack s:
                                        v.lowlink = min(v.lowlink, w.index)
                                if v.index = v.lowlink:
                                    reqeat until v is on top of stack:
                                        top = s.top()
                                        remove top from s
                                        add to a collection of connected components                    
                                
                           
    * both run in O(|V|+|E|), but Tarjan's approach works better in practice possibly because Tarjan's approach doesn't need to reverse the graph
    * [code](https://github.com/yitongw2/Code/blob/master/algorithm/scc.py)
    
## Minimum Spanning Tree
  ###  Prim-Jarnik Algorithm
  - pesudocode
    
                            def prim(G,v):
                                    D = empty dictionary for distqances
                                    P = empty dictionary for parents
                                    D[v] = 0
                                    P[v] = v
                                    for vertex w != v:
                                        D[w] = infinity
                                        P[w] = None
                                    PQ = priority queue with all vertices in G order by their distances
                                    while (PQ is not empty):
                                       w = PQ.removeMin()
                                       for u that w->u:
                                            if D[u] > D[w]+weight(w,u):
                                                D[u] = weight(w,u)
                                                P[u] = w
                                                update D[u] in PQ
                                    output D, P 
                                   
  - constructing a binary heap : O(n)
  - n iterations
    * removeMin() : O(logn)
  - m edges
    * update distance in priority queue : O(logn)
  - time complexity : O((m+n)logn)
  - [prim_mst](https://github.com/yitongw2/Code/blob/master/algorithm/mst.py)
  ### Kruskal Algorithm
  - pesudocode
  
                    U = a collection of clusters where each vertex is a cluster
                    while (U has more than 1 cluster):
                        sort edges by weights
                        for each edge (u,w) in edges:
                            if u and w not in the same cluster:
                                join u and w as 1 cluster
                                output (u,w)
                                
  
  - time complexity : O(mlogn)
  - [kruskal_mst](https://github.com/yitongw2/Code/blob/master/algorithm/mst.py)
  ### Boruvka Algorithm  
  - pesudocode
  
                        U = a collection of clusters where each vertex is a cluster
                        while (there is more than 1 cluster in U):
                            for each cluster c in U:
                                find the cheapest edge e going from c to another cluster d
                                join cluster c and d as 1 cluster
                                output this edge e 
  
  - O(logn) iterations : since every iteration join 2 clusters
  - O(m) : find the mim weighted edge
  - time complexity : O(mlogn)
  - [boruvka_mst](https://github.com/yitongw2/Code/blob/master/algorithm/mst.py)  
  ### All-Pairs Shortest Paths
  - Floyd–Warshall algorithm
    * pesudocode
                            
                            T = 2D-matrix table (n x n matrix)
                            for each vertex v in G:
                                T[v][v] = 0
                            for each edge (u,w) in G:
                                T[u][w] = weight(u,w)
                            for k=0->n:
                                for i=0->n:
                                    for j=0->n:
                                        if T[i][j] > T[i][k]+T[k][j]:
                                            T[i][j] = T[i][k]+T[k][j]
         
    * time complexity : O(n^3)            
                            

  
## Shortest Path
  ### Dijkstra Algorithm
  - no negative weights
  - [dijkstra_shortest_path](https://github.com/yitongw2/Code/blob/master/algorithm/shortest_path.py)
  ### Bellman-Ford Algorithm
  - no negative-weight cycle 
  - but can have negative weights
  - [bellman_ford_shortest_path](https://github.com/yitongw2/Code/blob/master/algorithm/shortest_path.py)
  
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
    
### Quick Sort
  - divide-and-conquer algorithm
    * divide the problem into several subproblems with smaller size
    * recursively solve these subproblems
    * when the size of the subproblem shrinks to the point that we can solve it fast enough, actually solve the subproblem
  - idea of quick sort (simple in-place version):
    * choose a pivot (an element in the sequence) randomly or not
    * partition the sequence into two subsequences: (simple partition)
      - the left subsequence contains elements that are smaller or equal to the pivot
      - the right subsequence contains elements that are greater than the pivot
      
      ![screen shot 2016-12-27 at 6 47 26 am](https://cloud.githubusercontent.com/assets/13974845/21501857/65055216-cc00-11e6-9302-9ca57ee2fbc8.png)
      
    * recurse on the two subsequences until the subsequences contains only 1 element (it is already sorted)
          
      ![screen shot 2016-12-27 at 6 34 33 am](https://cloud.githubusercontent.com/assets/13974845/21501661/af62c0f2-cbfe-11e6-84fc-104d62cb0ba1.png)

  - analysis
    * quick sort has two major components: partition and recursive calls 
        - there must be one partition in each recursive call
        - each partition takes O(n) time ([for details]())
    * so the performance of quick sort depends heavily on the number of recursive calls 
        - the number of recursive calls depends on how we choose the pivot
        - if we always choose the pivot to be the max/min element in the sequence, then, each time when we partition the
          sequence, we will always have a subsequence of size n-1 and another subsequence of size 1.
                            
                    recurrence formula: T(n) = T(n-1)+T(1)+O(n) 
                    ...
                    by induction, T(n) = O(n^2)
            
          time complexity of O(n^2) is not ideal.
        - if we wisely choose the pivot to be or close to the median, then we have 2 equally-sized portions
                
           ![screen shot 2017-01-05 at 11 45 58 pm](https://cloud.githubusercontent.com/assets/13974845/21711977/cba3ccca-d3a6-11e6-8fb0-fcd1be64e292.png)
                    
                    we can write recurrence as follow:
                    T(n) = 2*T(n/2)+O(n)
                    ...
                    by master theorem, T(n) = O(nlogn)
                    
          * however, to find the exact median of a sequence of size n requires at least the knowledge about n/2 elements, the 
            process takes O(n) and adds more constant factor to its O-notation
        - instead, choose pivot randomly can guarantee, on average case, that we can at least split the sequence into 1-to-3
          portions every recursive call
          
          ![screen shot 2017-01-06 at 12 37 16 am](https://cloud.githubusercontent.com/assets/13974845/21712237/5a9c9398-d3a8-11e6-94cc-4e31c379770e.png)
          
          * a good pivot: a good pivot should split the array, in the worst case, into a subsequence of size n/4 and another subsequence of size 3n/4.
            - the middle half of the sequence are good pivots
            ![screen shot 2017-01-06 at 12 46 29 am](https://cloud.githubusercontent.com/assets/13974845/21712431/a8b65f04-d3a9-11e6-911b-b743c793c89e.png)
            - if the probability of picking a pivot is 1/n, then the probability of picking a good pivot is 1/2
            - this implies that, on average, if we pick pivot randomly, it takes at most two tries before picking up a good pivot (just like flipping a
              coin).
          * assume we always split the sequence into 1-to-3 portions, we can write the recurrence as T(n) = T(3n/4)+T(n/4)+O(n)
            - by induction (hard to prove), we can prove that T(n) = O(logn)
            - or by drawing a quick-sort tree, we can see that 
              * the longest path of the quick sort tree is the rightmost path
              * on each level, we perform partition and it costs O(n)
              * T(n) = O(nlog(4/3)n) = O(nlogn)
            ![screen shot 2017-01-06 at 1 11 29 am](https://cloud.githubusercontent.com/assets/13974845/21713115/28baa98c-d3ad-11e6-864d-c88786e46271.png)
            - therefore, we can say, if we always pick a good pivot, the lower bound of the running time is O(nlogn)
          * even if we can not always pick a good pivot (most likely in reality), it only adds a constant factor to its O-notation.
            - we know that, for any recursive call that did not pick up a good pivot, the next recursive call on its subproblems is statistically gonna 
              pick a good pivot since the odd of picking a good pivot is 50%.
            - therefore, the total number of recursive calls, in the worst case, is at most twice as many as the number of recursive calls where we can
              at least split the sequence into 1-to-3 portions.
            - multiply the running time by a constant factor of 2 will not change its O-notation
- [Code](https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py)

### Merge Sort
  - divide-and-conquer algorithm
  - 2 components
    * recursive calls: divide the sequence into several subsequences and recurse on them 
    * merge: merge the result of these recursive calls into one sorted sequence 
  - idea of merge sort
    * first divide the sequence into 2 equally-sized subsequences and recurse on them until they are naturally sorted
    * then merge the 2 sorted subsequences into 1 sorted sequence
  - merge
    * given 2 sorted sequence A and B, merge them into 1 sorted sequence

                        i <-- 0
                        j <-- 0
                        outpur <-- empty list 
                        while (A is not empty or B is not empty) do
                            if A[i]<B[j] then 
                                push A[i] into output
                                ++i
                            else
                                push B[j] into output
                                ++j
                        push whaterver is left in A or B into output
                        return output
    * analysis
      - time complexity: O(size of A + size of B)
        * the number of elements pushed into output = size of A + size of B
        * other operations can viewed as constant-time operations
        * therefore, we have: O(size of A + size of B)+O(1) 
  - recurrence  
    * base case: when size of sequence is less than 2, the sequence is already sorted  
    * unlike quick sort, merge sort always divide the sequence into 2 equally-sized subsequences by splitting the sequence from the middle position
    * we can write the recurrence as T(n) = 2T(n/2)+O(n)
  - analysis
    * solving the recurrence

                        T(n) = 2T(n/2)+O(n)
                        ... by master theorem, 
                        T(n) = O(nlogn)

    * time complexity: O(nlogn)
  - [Code](https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py)


## Integer sort
  * sorting that are specialized for sorting integers
  * is able to break through the lower bound of comparison-based sorting O(logn)
  * without relying on comparisons, collect other information about elements in the sequence and sort it based on these information

### Bucket Sort
  - given a sequence of n elements where elements are in the range [0, N-1]
    * first, create an array of N buckets and use elements as indices of bucket array
    * push each element in the sequence into the bucket array according to the key of the element (usually the key is the           element itself)
    * enumerate elements in each bucket in the order from bucket 0 to N-1
    ![screen shot 2017-01-06 at 2 11 19 am](https://cloud.githubusercontent.com/assets/13974845/21714761/87f34b7c-d3b5-11e6-953b-24ccc1bece53.png)
  - bucket
    * each bucket is itself an array 
    * each bucket is indexed by an integer (usually an element in the sequence)
  - pesudocode
    
                        given a sequence S of n elements with range [1, N]
                        initialize a bucket array B of size N
                        initialize an empty list O
                        for i <-- 0 to n do
                            push S[i] into the bucket at index i of B
                        for j <-- 0 to N-1 do
                            find the bucket at index j of B
                            push everything in the bucket into O
                        return O
                          
  - [Code](https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py)

### Radix Sort
 - [Code](https://github.com/yitongw2/Code/blob/master/algorithm/sorting.py)
                    
## CYK algorithm
  - [Code](https://github.com/yitongw2/Code/blob/master/algorithm/cyk.py) 
  
# Data structure
## Union-Find
  - tree-based union-find disjoint set 
  - any sequence of M union and find operations on N objects takes O(N + MlogN) time
  - [code](https://github.com/yitongw2/Code/blob/master/data_structure/union_find.py)
## Graph
  - consists of a finite set of vertices and a finite set of edges
  - example, road map can thought as a directed graph
    * each intersection is a vertex
    * each road is an ordered edge from a vertex to another vertex
  - types
    * undirected graph
      - egdes are unordered (bidrectional)
      - (u,w) is the same edge as (w,u) 
    * directed graph 
      - edges are ordered 
      - (u,w) and (w,u) are two different edges
      - DAG == Directed Acyclical Graph
        * one form of directed graph
        * without cycle
  - representations
    * adjacency list
      - basic idea: 
        * use a collection of unordered lists to represent a graph
        * each list stores the neighbors of a vertex
      - implementation
        * Guido van Rossum approach: use a hash table to hash a vertex to a list of edges
        * Corman et.al approach: use a single list of lists and represent each vertex by its index in the list
        * Goodrich (Chancellor’s Professors at UCI) and Tamassia: have classes of vertex objects and edge objects. 
    * adjacency matrix
      - basic idea:
        * assume there are n vertices, use a n x n matrix to represent graph
        * if (u,w) exists, go to u row and w column and mark the cell as 1 (by default, each cell is marked as 0)
    * incidence matrix
  - operations
    * adjacent(G, u, v): determine if vertices u and v are neighbors
    * neighbors(G, u): get all neighbors of vertex u
    * add_vertex(G, u): add vertex u to graph G
    * remove_vertex(G, u): remove vertex u from graph G (along with all edges involving vertex u)
    * add_edge(G, u, v): add edge (u,v) to graph G 
    * remove_edge(G, u, v): remove edge (u,v) from graph G
    * get_vertex_value(G, u): get the value assoicated with vertex u
    * set_vertex_value(G, u, val): set the value assocaited with vertex u
  - [Code](https://github.com/yitongw2/Code/blob/master/data_structure/graph.py)  



## Binary Search Tree
  - a N-ary tree structure where N <= 2. 
  - a search data structure where searching for a key in the collection should be
    relatively fast (faster than simply linear searching for a key in a list)
  - for each node n in the binary tree
    * the key of n must be unique in the tree
    * can either have 0 (leaf node), 1 or 2 children.  
    * every node in n's left subtree must have keys smaller than n's key
    * every node in n's right subtree must have keys larger than n's key
  - the data structure only stores a pointer to the root node.
  - supported basic functionalties:
    * insertion: insert a node at one of the lead node of the tree
    * removal: remove a node specified by a key from this tree
    * search: look for a particular node with a specfied key 
  - a **perfect binary tree** is a tree that satifies the following 2 properties:
    * external nodes must be a perfect binary tree
    * for each non-external node, its left subtree and right subtree must be both perfect binary tree 
    
        e.g. the following tree is a perfect binary tree where each node either have 0 or 2 children 

![screen shot 2016-12-10 at 5 23 49 pm](https://cloud.githubusercontent.com/assets/13974845/21077348/7a0d826a-befd-11e6-8238-d109785879b3.png)
    
  - the height for a perfect binary subtree = O(logn)
    * at height = 0, there are 2^0 nodes on this level
    * at height = 1, there are 2^1 nodes on this level
    * ...
    * at height = k, there are 2^k nodes on this level
    * with height h, there are, in total, (2^0)+(2^1)+(2^2)+...+(2^h) ==> 2^(h+1)-1
                           
                                Geometric series: a+ar+ar^2+...+ar^(n-1)
                                Geometric sum: a*(1-r^n)/(1-r)
                                    (2^0)+(2^1)+(2^2)+...+(2^h)
                                ==> a=1, r=2
                                ==> (1-2^(h+1))/(1-2)
                                ==> 2^(h+1)-1
                             
    * suppose there are n nodes in a tree of height h, n = 2^(h+1)-1
        
                                n = 2^(h+1)-1
                             ==> n+1 = 2^(h+1)
                             ==> log(n+1) = h+1
                             ==> h = log(n+1)-1
                             ==> h = O(logn)
                             Therefore, height of a perfect binary tree is O(logn)
              
  - however, the basic binary search tree is not self-balancing, so the shape could grow into a linear structure (Professor       Alex Thronton calls it a degenerate tree) 
    * e.g. sequentially insert items of a sorted array {1,2,3,4,5} into a bst)
    
    ![screen shot 2016-12-02 at 2 22 08 pm](https://cloud.githubusercontent.com/assets/13974845/20852486/f5f41b64-b89a-11e6-845d-25e75d04361b.png)
    
    * in the extreme case like this, searching for a particular key as well as other operations could be as slow as O(n) since
      the height of the tree becomes O(n) instead of O(logn).
  - our best hope is that, given n nodes stored in a binary search tree, we can search/insert/delete a node by
    traversing much less than n nodes, namely O(log) nodes down toward one of the leaf nodes.  
  - when the binary search tree is perfectly balanced or near perfectly balanced, the cost of these operations is O(logn)
    * near perfect ==> complete binary tree == a relaxed version of perfect binary tree
        - a complete binary tree is a tree where, at any level except the root level, the preceding level of the tree must
          be full. 
        - that is to say, instead of forbidding the existence of any nodes with only 1 child (in the following example, 
          node 8 has only 1 child node 6), we tolerate this imperfection once but limits the only child of the particular
          node (node 6 in the example) to be the rightmost node on the bottom-most level.
        
             e.g. a complete binary tree
             
            ![screen shot 2016-12-10 at 5 45 47 pm](https://cloud.githubusercontent.com/assets/13974845/21077453/8305a368-bf00-11e6-94c8-0f06c90a0d21.png)
       
       - since the difference between a complete binary tree and a perfect binary tree is merely the bottom-most level, 
         the asymtopic notation of the height of the tree is still O(log). 
  - overhead required: need to maintain the perfect binary tree or complete binary tree.
  - [Code](https://github.com/yitongw2/Code/blob/master/data_structure/bst.py)

## AVL Tree
  - a variant of binary search tree that balances its height so that it won't grow into a degenerate tree.
  - Perfect or Complete?
    * both perfect and complete binary tree has a promised height of O(logn)
    * but the cost of maintaing either of them may possibly take Ω(n) times operations in the worst case. 
    * maintaing a perfect or complete binary tree is way too expensive if we constantly need to modify (insert/delete) the
      content of tree.
  - the idea behind AVL tree is that, if we relax the rules about how we arrange nodes in a tree a little looser,
    we can reduce the cost of rebalancing the binary tree while still maintain the height of the tree to be O(logn).
  - **AVL property = for each node in AVL tree, the height of its left and right subtrees differ by no more than 1.**
    * e.g. AVL tree 
                
      ![screen shot 2016-12-10 at 6 30 22 pm](https://cloud.githubusercontent.com/assets/13974845/21077632/c6eb1f12-bf06-11e6-85b8-49d98297bb33.png)
  
  - height of AVL tree
    * consider the minimum number of nodes n necessary to qualify as an AVL tree with height of h
    * given a node in an AVL tree, the height of its subtrees can either be one less than the parent node or 2 less than the         parent node. ==> they can be divided into 2 subsets of nodes
        
      ![screen shot 2016-12-10 at 7 18 39 pm](https://cloud.githubusercontent.com/assets/13974845/21077833/87d51ede-bf0d-11e6-9194-55300ea9cc75.png)
      
    * therefore, we can describe the relationship between n and h as a recurrence M(h): 
        - when h = 0, n = 1 ==> M[0]=1 (base case)
        - when h = 1, n = 2 ==> M[1]=2 (base case)
        - when h = k (k>=2), n = M[k-1]+M[k-2]+1 ==> M[k]= M[k-1]+M[k-2]+1 (recursive case)
            
            
        Solving the recurrence
            
              intuitively, a tree with height h-1 can contain more nodes than a tree with height h-2. 
              therefore, M[k-1]>M[k-2]  ==> M[k-1]>=M[k-2]+1
              obtain: M[k] >= 2*M[k-2]
                  ==> by induction, M[k] >= 2*(2*M[k-4])
                                    M[k] >= 2*(2*(2*M[k-6]))
                                    ...
                                    M[k] >= 2^j*M[k-2*j]
                  let j = k/2,
                  ==> M[k] >= 2^(k/2) / 2M[k - k]
                  ==> M[k] >= 2^(k/2)
                  let n be the number of nodes in AVL tree with height k, 
                  ==> n >= 2^(k/2)
                  ==> k/2 >= log(n)
                  ==> k >= 2*log(n)
                  ==> k >= log(n)
                  therefore, the height of AVL tree is O(logn)
                        
        
  - rotation
    * AVL tree balances its height to O(logn) by performing rotation operation during insertion or deletion.
    * O(logn) operations (worst case: downward from root to leaf)
    * trinode rotation
        - LL rotation
        - RR rotation
  - [Code](https://github.com/yitongw2/Code/blob/master/data_structure/avl_tree.py)

## WAVL Tree
  - Weak AVL tree, introduced in 2015 by Bernhard Haeupler, Siddhartha Sen and Robert E Tarjan.
  - a self-balancing binary tree that can be perceived as both of AVL tree and Red-Black tree. 
  - WAVL's advantage over AVL tree and Red-Black tree
    * height of WAVL tree is between 1.433logn to 2logn (Red-Black tree has a height of 2log(n))
    * rotation in WAVL tree costs an amortized O(1) (AVL tree costs O(logn))
  - each node of the WAVL tree is assigned to a rank
  - rank difference of a node n is the difference between the rank of n and the rank of n's parent node 
    * a 1-1 node has 2 children with rank difference of 1
    * a 1-2 node has 1 child with rank difference of 1 and 1 child with rank difference of 2
    * a 2-2 node has 2 children with rank difference of 2
  - WAVL tree must satisfy the following WAVL properties  
    * all external nodes have rank of 0
    * every node with 2 external nodes have rank of 1
    * every non-root nodes can have either have rank difference of 1 or 2
  - when only insert elements into WAVL tree (without deletion), it performs exactly like AVL tree with a heigh of 1.433logn.
    * insertion-path: the path from root to the external node where the element is to be inserted
    * for each node along the path, we either 
      - create a 1-1 node by trinode rotation
      - create a 1-2 node by promoting its parent or trinode rotation
    * therefore, the WAVL tree without deletion has only 1-1 node and 1-2 node and it matches the definition of AVL tree
    * essentially, AVL tree is Weak AVL tree wihtout 2-2 nodes
  - when deletion is involved, there might be 2-2 nodes in the WAVL tree 
    * since defintion of WAVL tree is loose (allows the existence of 2-2 node), we only perform trinode rotation when 1-1 node, 1-2 node and 
      2-2 node is not viable through simple demotion.
    * the cost of rotation is amortized to be constant
  - [Code](https://github.com/yitongw2/Code/blob/master/data_structure/wavl_tree.py)


## Heap (Min Heap)
  - a 2-ary tree data structure that satisifies the following properties:
    * heap-order proprty: the key of parent node should be less than (grater than if max heap)the key of any child node
    * complete-binary property: each level of heap must be filled untill any elements can be inserted to next level
  - a specified search structure that is most efficient for retreieving the smallest/largest key in the collection of items.
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

## Stack
  - conceptual data structure that obeys the LIFO (Last In First Out) principle
  - essentially, a collection of items where only one end of the collection can be accessed (added or removed)
  - hence, stack should support: 
    * push(item): add item to the end of the collection
    * pop(): remove the item on the end of the collection (and usually return it)
    * top(): return the item currently on the end of the collection
    * size(): return the number of items in the stack
  - can be implemented as array or linked list (implemented with Python list in the example)
  - time complexity:
    * push(): O(1)
    * pop(): O(1)
    * top(): O(1)
    * size(): O(1)
  - [Code](https://github.com/yitongw2/Code/blob/master/data_structure/stack.py)

# Interesting coding problems
## Hamming Distance (Leetcode 461)
  - [Code](https://github.com/yitongw2/Code/blob/master/solutions/hamming_distance.py)
 
## Reverse Vowels of a String (Leetcode 345)
  - [Code](https://github.com/yitongw2/Code/blob/master/solutions/Reverse_Vowels_String.java)
  
## Find All Numbers Disappeared in an Array (Leetcode 448)
  - [Code](https://github.com/yitongw2/Code/blob/master/solutions/disappeared_nums_array.py)

## Russian Doll Envelopes (Leetcode 354)
  - Given a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
  - the goal is to find the maximum number of envelopes can you Russian doll? (put one inside other).
  - each envelopes can fit itself, so maxEnvelopes([(1,2)]) has an answer of 1.
  - basic solution (time: O(n^2)):
    * first sort the envelopes first by their width and, if width is the same, sort by their height. 
    * make a table of length n (n is the number of )
    * the base case for all envelopes = 1 
    * for each envelope, we look back to the envelopes we saw before:
        - find an envelope in the table that it can fit into the current envelope and it can fit the most envelopes before. 
    * example:  envelopes = [[5,4],[6,4],[6,7],[2,3]]
    
        after sorting: [[2,3],[5,4],[6,4],[6,7]]
        
        table
        
        | envelopes  | [2,3] | [5,4] | [6,4] | [6,7]| 
        |---|---|---|---|---|
        | table  | 1 | 2 | 1 | 1 |
        
        Suppose we are currently at [6,4], 
            we look back at [2,3] and [5,4]:
            
            - [2,3] \< [6,4] and 1+1 \> 1. Therefore, for now, [6,4] can fit at most 2 envelopes including itself.
            
            - [5,4] can not be included by [6,4] since they have the same height. 
            
            - therefore, we put 2 to the cell for [6,4] in the table.
        
        table
        
        | envelopes  | [2,3] | [5,4] | [6,4] | [6,7]| 
        |---|---|---|---|---|
        | table  | 1 | 2 | 2 | 1 |
    
    * [Code](https://github.com/yitongw2/Code/blob/master/solutions/RussianEnvelopes.java) 
  
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
      - K[i][0]=0 or K[0][s]=0,  base case.
      - K[i][s]=value(i) + K[i-1][s-size(i)],  to include ith item.
      - K[i][s]=K[i-1][s],  not to include ith item.
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
     * [Code](https://github.com/yitongw2/Code/blob/master/solutions/knapsack.py)
  
  
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
  
  
  
  
