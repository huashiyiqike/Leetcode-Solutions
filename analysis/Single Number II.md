<backquote><pre>
Given an array of integers, every element appears three times except for one. Find that single one. 
</backquote></pre>

The number in 32 bits , just count how many 1s are there in each bit, and count[i] %= 3 will clear it once it reaches 3. After running for all the numbers for each bit, if we have a 1, then that 1 belongs to the single number, we can simply move it back to its spot by doing ans |= sum << i;