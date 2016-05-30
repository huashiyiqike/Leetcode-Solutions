function TrieNode(){
	this.next = {};
	this.end = false;
}

function Trie(words){
	this.root = new TrieNode;
	for(var i = 0; i < words.length; i++){ 
		var cur = this.root, word = words[i];
		for(var j = 0; j < word.length; j++){
			if(!(word[j] in cur.next)){
				cur.next[word[j]] = new TrieNode;
			}
			cur = cur.next[word[j]];
		}
		cur.end = true;
	}
}
/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
    var res = {}, trie = new Trie(words).root;
    for(var i = 0; i < board.length; i++){
    	for(var j = 0; j < board[0].length; j++){
    		dfs(board, i, j, trie, res, '');
    	}
    }
    var all = [];
    for(var i in res) all.push(i);
    return all;
};

function dfs(board, idx, idy, trie, res, path){
	if(idx < 0 || idx >= board.length || idy < 0 || idy >= board[0].length 
		 ||!(board[idx][idy] in trie.next)){
		return;
	}
	trie = trie.next[board[idx][idy]];
	path += board[idx][idy];
	if(trie.end && !(path in res)){
		res[path] = true;
	} 
	var tmp = board[idx][idy];
	board[idx][idy] = null;
	dfs(board, idx + 1, idy, trie, res, path);
	dfs(board, idx - 1, idy, trie, res, path);
	dfs(board, idx, idy + 1, trie, res, path);
	dfs(board, idx, idy - 1, trie, res, path);
	board[idx][idy] = tmp;
}