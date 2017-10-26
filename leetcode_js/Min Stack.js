/**
 * @constructor
 */
var MinStack = function() {
    this.stack = []; 
};

/**
 * @param {number} x
 * @returns {void}
 */
MinStack.prototype.push = function(x) {
    if (this.stack.length == 0) {
        this.stack.push(x,x);
    } else {
        this.stack.push(Math.min(this.stack[this.stack.length-2], x), x);
    }
};

/**
 * @returns {void}
 */
MinStack.prototype.pop = function() {
    this.stack.pop();
    this.stack.pop();
};

/**
 * @returns {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length-1]
};

/**
 * @returns {number}
 */
MinStack.prototype.getMin = function() {
    return this.stack[this.stack.length-2]
};