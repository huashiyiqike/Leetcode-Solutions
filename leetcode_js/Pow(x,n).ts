/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */

function myPow(x:number, n:number){
	let res:number = 1, m:number = Math.abs(n);
	while(m > 0){
		if((m&1) != 0){
			res *= x;
		}
		m >>>= 1; // unsigned shift
		x *= x;
	}
	if(n < 0){
		res = 1 / res;
	}
	return res;
}