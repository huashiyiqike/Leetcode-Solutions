/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
	var courses = [];
	for(var i = 0; i < numCourses; i++){courses[i] = new node(i);}

    for(var i = 0; i < prerequisites.length; i++){
    	var start = prerequisites[i][0], pre = prerequisites[i][1]; 
    	courses[pre].into++; 
    	courses[start].next.push(courses[pre]); 
    }
    var stack = [], count = 0, res = [];
    for(var i = 0 ; i < courses.length; i++){
		if(courses[i].into == 0){
			stack.push(courses[i]);
			res.unshift(courses[i].id);
			count++;
		} 	 
    } 
    while(stack.length > 0){
    	var cur = stack.pop();
    	for(var i = 0; i < cur.next.length; i++){
    		if(cur.next[i].into == 1){
    			stack.push(cur.next[i]);
    			res.unshift(cur.next[i].id);
    			count++;
    		}
    		cur.next[i].into--;
    	}
    }
    return count == numCourses?res:[];
}
function node(id){
	this.id = id;
	this.into = 0;
	this.next = [];
}
