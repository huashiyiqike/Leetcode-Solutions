>Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

There are two solutions.
1. divide and conquer. It is easy to merge two lists. So we can divide the lists to two parts and conquer each one. If the small part has less or equal to two lists, we conbine them and return the resulted new list; otherwise we recursive divide it.

2. use heapsort. We put the heads of each lists to the heap. Once pop we push the next one in that list into the heap. 