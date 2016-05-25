var WordDictionary = function() {
    this.root = new Node;
};
function Node(){
    this.next = {}; 
    this.end = false; 
}
/**
 * @param {string} word
 * @return {void}
 * Adds a word into the data structure.
 */
WordDictionary.prototype.addWord = function(word) {
    var cur = this.root;
    for(var i = 0; i < word.length; i++){
        if(!(word[i] in cur.next)){
            cur.next[word[i]] = new Node; 
        }
        cur = cur.next[word[i]];
    }
    cur.end = true;
}
/**
 * @param {string} word
 * @return {boolean}
 * Returns if the word is in the data structure. A word could
 * contain the dot character '.' to represent any one letter.
 */
WordDictionary.prototype.search = function(word) {
    var cur = [this.root];
    for(var i = 0 ; i < word.length; i++){
        var next = [];
        if(word[i] == '.'){
            for(var j = 0; j < cur.length; j++){
                for(var key in cur[j].next){
                    next.push(cur[j].next[key]);
                }
            } 
        }else{
            if(cur.length == 0){return false;}
            for(var j = 0; j < cur.length; j++){
                if(word[i] in cur[j].next){
                    next.push(cur[j].next[word[i]]);
                }
            } 
        }
        cur = next;
    }
    return cur.filter(function(val){return val.end;}).length > 0;
};
