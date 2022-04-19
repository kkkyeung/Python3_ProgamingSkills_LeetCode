https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/discuss/516999/Python-1-line

Let take a look at an example:
A = [5, 4, 2 , 1]
When we pass it to a lambda function([bin(a).count('1'), a]), I like to think that it converts it to:
A = sorted([2, 5], [1, 4], [1, 2], [1, 1])

It convert 5 to [2, 5]. Why? 5 = 0101 in binary and there are two 1's in it, hence [2, ] and the second value, 5, it's just the value 5 [ , 5]. It applies to the rest of the values.

Lambda function convert list A to a standard form that Python can use to sort. First it compare the first value then the second value.
A -> [[1,1], [1,2], [1, 4], [2,5]]
A = [1, 2, 4, 5]