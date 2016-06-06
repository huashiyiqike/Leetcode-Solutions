var isValid = function(s) {
    var stack = [];
    for(var i = 0;i < s.length;i++){
        switch(s[i]){
            case '(': stack.push('(');break; 
            case '[': stack.push('[');break; 
            case '{': stack.push('{');break; 
            case ')': if(stack.length <= 0 || (stack.length > 0 &&
             stack[stack.length - 1] !== '(')) {return false;}
             stack.pop();break; 
            case ']': if(stack.length <= 0 || (stack.length > 0 &&
             stack[stack.length - 1] !== '[')) {return false;}
            stack.pop();break; 
            case '}': if(stack.length <= 0 || (stack.length > 0 &&
             stack[stack.length - 1] !== '{')) {return false;}
            stack.pop();break;  
        } 
    }
    return stack.length == 0;
};