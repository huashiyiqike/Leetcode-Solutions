/**
 * @param {number[][]} buildings
 * @return {number[][]}
 */
  

var getSkyline = function(buildings) {
    var res = [], liveHR= [];
    var i = 0;
    var rightmost;
    while(i < buildings.length || liveHR.length > 0){
        if(liveHR.length == 0 || (i < buildings.length && liveHR[0][1] >= buildings[i][0])){
             // just start or new buildings that are right to previous rightmost
            rightmost = buildings[i][0];
            while(i<buildings.length && buildings[i][0] == rightmost){
                // in case multiple buildings start at rightmost
                heappush(liveHR, [buildings[i][2], buildings[i][1]]);
                i += 1;
            }
         }else{
            rightmost = liveHR[0][1];
            while(liveHR.length > 0 && liveHR[0][1] <= rightmost){
                heappop(liveHR);
            }
         }
        var height = liveHR.length > 0 ? liveHR[0][0] : 0; 
        if(res.length == 0 || height != res[res.length-1][1]){
            res.push([rightmost, height]);
            console.log(rightmost+" "+height);
         }

    }
    return res;
}; 


function heappush(arr, obj){
    arr.push(obj);
    var i = arr.length-1;
    while(i>0){
        var p = Math.floor((i-1)/2);
        if(arr[i][0] > arr[p][0]){ 
            var tmp = arr[i];
            arr[i] = arr[p];
            arr[p] = tmp;
            i = p;
        }else{
            break;
        }
    }
}
 
function heappop(arr){ 
    if(arr.length == 1){
        arr.pop();
        return;
    }
    arr[0] = arr.pop();
    var i = 0;
    while(2*i+1 < arr.length){
        if(2*i+2 >= arr.length){
            if(arr[i][0] < arr[2*i+1][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+1];
                arr[2*i+1] = tmp; 
                i = 2*i + 1;
            }
            return;
        }

        if(arr[2*i+1][0]>arr[2*i+2][0]){
            if(arr[i][0] < arr[2*i+1][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+1];
                arr[2*i+1] = tmp; 
                i = 2*i + 1;
            }
            else if(arr[i][0] < arr[2*i+2][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+2];
                arr[2*i+2] = tmp;
                i = 2*i +2;
            } else{break;}
        }else{
            if(arr[i][0] < arr[2*i+2][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+2];
                arr[2*i+2] = tmp; 
                i = 2*i + 2;
            }
            else if(arr[i][0] < arr[2*i+1][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+1];
                arr[2*i+1] = tmp;
                i = 2*i +1;
            } else{break;}
        }
    }
}

console.log("test")
 
console.log(getSkyline([[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]]));
console.log("[[2,70],[4,30],[6,41],[7,70],[10,102],[30,41],[60,91],[80,72],[90,59],[120,0]]");