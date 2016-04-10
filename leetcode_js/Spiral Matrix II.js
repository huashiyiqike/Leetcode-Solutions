var generateMatrix = function(n) {
   var l = n;
    n *= n;
    var has = [];
    for(var i = 0; i< l; i++){
        var tmp = new Array(l);
        for(var j=0; j<l;j++){
            tmp[j] = false;
        }
        has.push(tmp);
    }

    var dir=[[0,1],[1,0],[0,-1],[-1,0]];
    var diridx = 0, x = 0, y=0;
    for(i = 0; i < n ;i++){
        has[x][y] = i+1;
        var tmpx = x + dir[diridx][0];
        var tmpy = y + dir[diridx][1];
        if(tmpx < 0 || tmpx > l-1 || tmpy < 0 || tmpy > l-1 || !!has[tmpx][tmpy]){
            diridx += 1;
            diridx %= 4;
        }
        x = x + dir[diridx][0];
        y = y + dir[diridx][1];

    }
    return has;
};
