/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 

let helper: (nums: number[], res: number[][], path: number[], vis: boolean[])=>any = 
function(nums: number[], res: number[][], path: number[], vis: boolean[]){
	if(path.length == nums.length){
		res.push(path.slice());
		return;
	}
	for(let i:number = 0; i < nums.length; i++){
		if(i > 0 && nums[i] == nums[i-1] && vis[i-1]){
			continue;
		}
		if(!vis[i]){
			vis[i] = true;
			path.push(nums[i]);
			helper(nums, res, path, vis);
			path.pop();
			vis[i] = false;
		}
	}
}

let permuteUnique : (nums:number[]) => number[][] =
 function(nums:number[]){
	nums = nums.sort((a:number, b:number)=>{return a - b;});
	let res: number[][] = [];
	let vis: boolean[] = [];
	for(let i:number = 0; i < nums.length; i++){
		vis[i] = false;
	}
	helper(nums, res, [], vis);
	return res; 
}