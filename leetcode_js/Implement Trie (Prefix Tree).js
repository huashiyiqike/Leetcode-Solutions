/**
 * @constructor
 * Initialize your data structure here.
 */
var TrieNode = function() {
    var obj = new Object();
    obj.end = false;
    obj.nexts = {};
    return obj;
};

var Trie = function() {
    this.root = TrieNode();
};

/**
 * @param {string} word
 * @return {void}
 * Inserts a word into the trie.
 */
Trie.prototype.insert = function(word) {
    var cur = this.root;
    for(var i = 0; i < word.length; i++){
        if(!(word[i] in cur.nexts)){
            cur.nexts[word[i]] = TrieNode(); 
        }
        cur = cur.nexts[word[i]];
    }
    cur.end = true;
};

/**
 * @param {string} word
 * @return {boolean}
 * Returns if the word is in the trie.
 */
Trie.prototype.search = function(word) {
    var cur = this.root;
    for(var i = 0 ; i < word.length; i++){
        if(!cur || !cur.nexts || !(word[i] in cur.nexts)){return false;}
        cur = cur.nexts[word[i]];
    }
    return cur.end === true;
};

/**
 * @param {string} prefix
 * @return {boolean}
 * Returns if there is any word in the trie
 * that starts with the given prefix.
 */
Trie.prototype.startsWith = function(prefix) {
    var cur = this.root;
    for(var i = 0 ; i < prefix.length; i++){
        if(!cur || !cur.nexts || !(prefix[i] in cur.nexts)){return false;}
        cur = cur.nexts[prefix[i]];
    }
    return true;
};
/**
 * Your Trie object will be instantiated and called as such:
 * var trie = new Trie();
 * trie.insert("somestring");
 * trie.search("key");
 */