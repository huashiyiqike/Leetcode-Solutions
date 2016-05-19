/**
 * @param {number[][]} buildings
 * @return {number[][]}
 */
var getSkyline = function(buildings) {
    var res = [], liveHR= [];
    var i = 0;
    var rightmost;
    while(i < buildings.length || liveHR.length > 0){
    	if(liveHR.length == 0 || (i < buildings.length && liveHR[0][1] < buildings[i][0])){
	    	 // just start or new buildings that are right to previous rightmost
	    	rightmost = buildings[i][0];
	    	while(i<buildings.length && builds[i][0] == rightmost){
	    		// in case multiple buildings start at rightmost
	    		heappush(liveHR, [buildings[i][1], buildings[i][2]]);
	    	}
   		 }else{
   		 	rightmost = liveHR[0][1];
   		 	while(liveHR.length > 0 && liveHR[0][1] <= rightmost){
   		 		heappop(arr);
   		 	}
   		 	var height = liveHR.length > 0 ? liveHR[0][0] : 0; 
   		 }
   		 if(res.length == 0 || height != res[res.length-1][1]){
   		 	res.push([rightmost, height]);
   		 }
    }
    return res;
};

function heappush(arr, obj){
	arr.push(obj);
	var i = arr.length-1;
	while(i>0){
		var p = Math.floor((i-1)/2);
		if(obj[0] > arr[p][0]){ 
			var tmp = obj;
			obj = arr[p];
			arr[p] = tmp;
			i = p;
		}else{
			break;
		}
	}
}
function swap(a, b){
	var tmp = a;
	a = b;
	b = tmp;
}
function heappop(arr){ 
	arr[0] = arr.pop();
	var i = 0;
	while(2*i+1 < arr.length){
		if(2*i+2 < arr.length && arr[i] < arr[2*i+2]){
			var tmp = arr[i];
			arr[i] = arr[2*i+2];
			arr[2*i+2] = tmp;
			i = 2*i +2;
		}else if(arr[i] < arr[2*i+1]){
			swap(arr[i], arr[2*i+1]);
			i = 2*i + 1;
		}else{break;}
	}
}

