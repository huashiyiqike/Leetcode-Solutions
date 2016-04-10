function quicksort(a){
	if(a.length <= 1) return a;
	var idx = partition(a);
	a = merge(quicksort(a.slice(0,idx)),quicksort(a.slice(idx,a.length)));
    return a;
}
function partition(a){
	var index = 1, i = a.length-1;
	while(i > index){
		if(a[i] < a[0]){
			var tmp = a[index];
			a[index] = a[i];
			a[i] = tmp;
			index++;
		}else{
			i--;
		}
	}
	if(a[0] > a[index]){
		var tmp = a[index];
		a[index] = a[0];
		a[0] = tmp;
	}
	return index;
}
function merge(a, b){
	var c = [];
	var x = 0, y = 0;
 
	while(x < a.length && y < b.length){
		if(a[x] <= b[y]){c.push(a[x]);x++;}
		else{c.push(b[y]); b++;}
	}
	if(x < a.length){
		c = c.concat(a.slice(x, a.length));
	}
	if(y < b.length){
		c = c.concat(b.slice(y, b.length));
	}
	return c;
}
var tmp = quicksort([1,4,43,5,77,0,232,434,3]);
console.log(tmp);