First we need to create an empty list for containing the output.
then copy a nums2 input list, for edit later.

find the index position of the nums2 list based on the nums1 index,
if the position is the last of the nums2, just append -1 to the output list.
Otherwise, delete the element and before the element inside the list based on the position.
then, we will have a new list which containing the elements after that selected position.
than just get the first element of the new list and append it to the output list.

or , if the new list contain nothings, just append -1.

finally return the output list.