 
$(document).ready(function(){
	var res = "";
	// var items=[
	// {
	// 	no:329,
	// 	type:'Memorization',
	// 	title:'Longest Increasing Path in a Matrix',
	// 	url:'https://leetcode.com/problems/longest-increasing-path-in-a-matrix/',
	// 	difficulty:Hard
	// },
	// {
	// 	no:319,
	// 	type:'Bulb Switcher',
	// 	title:'Longest Increasing Path in a Matrix',
	// 	url:'https://leetcode.com/problems/longest-increasing-path-in-a-matrix/',
	// 	difficulty:Hard
	// },
	// ];
   
	var items = $("tbody tr");
	var prob = new Array(items.length);
	for(var i = items.length-1; i >= 0; i--){
		var str = $(items[i]).find("a");
		var html = $(items[i])[0].outerHTML;

		prob[i] = new Object;
		prob[i].url = /problems\/(.*)\/"/.exec(html)[1];
		prob[i].title =str.html();
		prob[i].no = /<td>(\d+)<\/td>/.exec(html)[1];
		prob[i].acceptance = /<td>(\d+)<\/td>/.exec(html)[1];
		prob[i].hard = /<td value="\d+.\d+%">(\w+)<\/td>/.exec(html)[1];
		prob[i].acceptance = /<td>(\d+.\d+%)<\/td>/.exec(html)[1];
 	    res += '|'+prob[i].no + '|['+prob[i].title;
		if(str.parent().find(".fa").length > 0){
			res+=' ' + '<sup>$<sup> ';
		}
		res += '](https://leetcode.com/problems/'+
			prob[i].url+')|[js](./leetcode_js/'+prob[i].title+
			'.js) [py](./leetcode_py/'+prob[i].title+'.py) [java](./leetcode_java/'+ prob[i].url + '/Solution.java)|'+prob[i].hard+'|[essence](./analysis/'+prob[i].title+
 			'.md)|\n';
	}
 	console.log(res);
});