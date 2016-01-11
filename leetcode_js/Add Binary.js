/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    a = a.split('').reverse().map(Number);
    b = b.split('').reverse().map(Number);
    if(a.length < b.length){
        var tmp = a;
        a = b;
        b = tmp;
    }
    var inc = 0;
    for(var i = 0; i < a.length; i++){
        a[i] += inc;
        if(i < b.length) a[i] += b[i];
        inc = Math.floor(a[i]/2);
        a[i] %= 2;
    }
    if(inc > 0) a = a.concat(1);
    return a.reverse().join("");
};
document.writeln(addBinary("1","1"));
document.writeln(addBinary("11","1"));