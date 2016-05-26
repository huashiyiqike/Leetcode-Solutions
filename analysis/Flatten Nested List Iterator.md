<backquote><pre>
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
</backquote></pre>

Note that you can only use the provided APIs. The given data is a list, however, in the list there are only elements that can be accessed with these APIs. You should put them in a common inner data structure(stack, queue, etc., whatever keeps the traversal in order) so that you can retrieve them easily later. You should get the next result ready in the boolean function hasNext in case there are empty objects inside the given list.