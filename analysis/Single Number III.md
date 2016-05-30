<backquote><pre>
 Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5]. 
</backquote></pre>
Use XOR to store the difference among these numbers, if XOR all elements, the result is the difference between two number like result = A^B.Find one digit 1 in the result, which can be used to distinguish A and B. depends on this, XOR elements which the bit equals 1  to find A .And A^result = B 