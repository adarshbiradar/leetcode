Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.



Solution
0 1 1 1 
1 1 1 1
0 1 1 1 

0 1 1 1 result = 3
1 1 2 2 result = 6
0 1 2 3 result = 6

3+6+6  = 15
