# Code
A library of some interesting algorithms, data structure implementation or just random stuff learnt in/out of school

# Algorithm 


# Data structure


# Interesting coding problems

* 2 sum
  - Given an array of integers, return indices of the two numbers such that they add up to a specific target.
  - assume only one matching pair in the array
  - example. l = [2, 1, 5, 4, 9], tartget = 9
             expected output [2, 3]
  
  Solution 1 (in Java):
    1, use a hash table to hash all values in the array
    2, looping through the array from 0 to length of the array-1
    3, for each loop, find the target-array[i] in hash table
    4, if found during the loop, return the pair; otherwise, such pair doesn't exist.
