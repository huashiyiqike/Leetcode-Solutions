<blockquote>
<pre>There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.

</pre>
</blockquote>

If the ith bulb has even factors(including 1), it will be off in the end. Only the perfect square numbers can make the bulb on. There are totally n bulbs and we count the perfect square numbers less than n by sqrt n.
/************/
If f is the ith factors,the ith/f also is the factorys of ith.So the ith (except t*t=ith) has odd factors so will off.Only(t*t=ith)The ith bulb will on,so we can count the number of i to ith has how many the perfect square numbers.