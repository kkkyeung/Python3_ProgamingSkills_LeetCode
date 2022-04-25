1. For My solotion:
More like iterative:
Create an empty list then append the whole root into it and set the current depth
check if there is none or not, of none, just return output.
otherwise , keep updating the depth using while loop.

Time: 47ms   > 75.89% 
Memory: 15.3MB  < 82.44%




2. For the recursive solution:
directly find the depth of the root, no matter left or right,
if root is none return 0, if not just return the depth +1 since the head of the tree is count 1.


the runtime will be faster , but the memory usage will be used more.
Time: 40ms  > 94.30% 
Memory: 16.3MB  < 27.10%