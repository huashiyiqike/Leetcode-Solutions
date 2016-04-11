var true_inplace = {
	qs:function(a){
		function partition(a, left, right){
			if(left < right){
				var pivot = left;
				for(var i = pivot+1; i < right+1; i++){
					if(a[i] < a[left]){
						pivot++;
						var tmp = a[i];
						a[i] = a[pivot];
						a[pivot] = tmp;
					}
				}

				var tmp = a[pivot];
				a[pivot] = a[left];
				a[left] = tmp;
				partition(a, left, pivot-1);
				partition(a, pivot+1, right);
			}
		}
		partition(a, 0, a.length-1);
		return a;
	}
}
console.log(true_inplace.qs([4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]));

var inplace = {
	quicksort: function quicksort(a) {
		inner(0, a.length-1);

		function inner(start, end) {
			if (end - start <= 0) return;
			var idx = partition(start, end);
			inner(start, idx-1);
			inner(idx+1, end);
			merge(start, idx, end);
		}

		function partition(start, end) {
			var pivot = start;
			for(var i = pivot+1; i < end+1; i++){
				if(a[i] < a[start]){
					pivot++;
					var tmp = a[i];
					a[i] = a[pivot];
					a[pivot] = tmp;
				}
			}

			var tmp = a[pivot];
			a[pivot] = a[start];
			a[start] = tmp;

			return pivot;
		}
		

		function merge(start, idx, end) {
			var l1 = a.slice(start, idx),
				l2 = a.slice(idx, end);
			var x = 0,
				y = 0;
			while (x < l1.length && y < l2.length) {
				if (l1[x] < l2[y]) {
					a[start++] = l1[x++];
				} else {
					a[start++] = l2[y++];
				}
			}
			while (x < l1.length) {
				a[start++] = l1[x++];
			}
			while (y < l2.length) {
				a[start++] = l2[y++];
			}
		}
		return a;
	}

}
var tmp = inplace.quicksort([1, 4, 43, 5, 77, 0, 232, 0, 3, 434, 3]);
console.log(tmp);

function slow() {
	function quicksort(a) {
		if (a.length <= 1) return a;
		var idx = partition(a);
		a = merge(quicksort(a.slice(0, idx)), quicksort(a.slice(idx, a.length)));
		return a;
	}

	function partition(a) {// This partition doesn't do the job
		var index = 1,
			i = a.length - 1;
		while (i > index) {
			if (a[i] < a[0]) {
				var tmp = a[index];
				a[index] = a[i];
				a[i] = tmp;
				index++;
			} else {
				i--;
			}
		}
		if (a[0] > a[index]) {
			var tmp = a[index];
			a[index] = a[0];
			a[0] = tmp;
		}
		return index;
	}

	function merge(a, b) {
		var c = [];
		var x = 0,
			y = 0;

		while (x < a.length && y < b.length) {
			if (a[x] <= b[y]) {
				c.push(a[x]);
				x++;
			} else {
				c.push(b[y]);
				b++;
			}
		}
		if (x < a.length) {
			c = c.concat(a.slice(x, a.length));
		}
		if (y < b.length) {
			c = c.concat(b.slice(y, b.length));
		}
		return c;
	}
	var tmp = quicksort([1, 4, 43, 5, 77, 0, 232, 434, 3]);
	console.log(tmp);
}