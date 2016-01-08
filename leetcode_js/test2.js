//for(var i = 0 ; i < 10 ; i++){
//    var obj = document.createElement("div");
//    //obj.innerHTML = i;
//    //obj.onclick = function(){alert(i);}
//    //document.body.appendChild(obj);
//    var  a = [2,3,4];
//    document.writeln(a.slice(0,1));
//}
var re = /&/;
var str = " &amp;fdsaff&fdsa&";
//document.write(str);
document.writeln(str.replace(re, "&a"));
document.write(str.replace("&", "&a"));
//document.write(str);
var move = function(){
    $(".test")
}