/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    num1 = num1.split('').reverse().map(Number);
    num2 = num2.split('').reverse().map(Number);
    var res = [];
    for(var i = 0; i < num1.length; i++){
        for(var j = 0 ; j < num2.length; j++){
            if(res[i+j]){ 
                res[i+j] += num1[i] * num2[j];
            }else{
                res[i+j] = num1[i] * num2[j];
            }
           // document.write("<br>" + num1[i] + " " + num2[j] + " "+ res[i+j]);
        }
    }
    for(var i = 0 ; i < res.length; i++){
        if(res[i] > 9){
            if(res[i+1]){
                res[i+1] += Math.floor(res[i]/10);
            }else{
                res[i+1] = Math.floor(res[i]/10);
            }
            res[i] %= 10;
        }
    }
    
    res = res.reverse().join("");
    var start = 0;
    i = 0;
    while(res[i] === "0" && res[i+1] === "0"){
        start = i+1;
        i++;
    } 
    
    return res.substring(start, res.length);
};
