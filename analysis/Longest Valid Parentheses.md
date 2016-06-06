<backquote><pre>
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
</backquote></pre>

The first thought is to count the number of left parentheses and right parentheses. However, since the longest valid parenthetheses are connected, we only need care if the current pair matches, and expand to left if so. We cannot use dp because it is hard to split the problem into sub ones(each part affects each other). We need a data structure to keep record of the state while traversing. Since we care for the nearest pair and also need history information, stacks come naturally. Since only '(' needs to be stored, we can store the indexes. Special care should be taken to empty stacks: it can mean part or all of the sequences constitute the result, so we need to maintain a leftmost starting index.
