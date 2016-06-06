// var $ = require('jquery');   
// //var fs= require('fs');  
//var $ = require('jquery')(require("jsdom").jsdom().parentWindow);
// //var jsdom = require("jsdom").jsdom;

// var jsdom = require("jsdom").jsdom;
var fs = require('fs');

var jsdom = require("jsdom");
var window = jsdom.jsdom().defaultView;



fs.readFile('_test.html', 'utf-8', function(err, data) {
	if (err) {
		console.log(err);
	} else {
		jsdom.jQueryify(window, "http://code.jquery.com/jquery.js", function() {
			var $ = window.$;
			$("body").prepend("<h1>The title</h1>");
			console.log($("h1").html());

			var res = ""; 
			var items = $(data).find("tbody tr");
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
			fs.writeFile('_generated.md',res,'utf-8',function(err){
				if(err){console.log(err);}
			}); 
		});
	}
})