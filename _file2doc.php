<?php 
if(file_exists("README.md")){
	$f2 = fopen("README.md", "w");
}
fwrite($f2, "LeetCode\n========\n\n###LeetCode Solutions\n\n"."
| # |  Title | Solution | Difficulty | Analysis\n".
"|  --- | --- | --- | --- | --- | --- |\n");

if(file_exists("_generated.md")){
	$f = file("_generated.md"); 
	for($i = 0; $i < count($f); $i++){  
		$arr = explode('|', $f[$i]);  
		$tmp = array();
		$res = '';
		preg_match("/\[py\]\(.\/([^\.]*\.py)/", $arr[3], $tmp);
		if(file_exists($tmp[1]) && filesize($tmp[1]) > 20){
			$res .= $tmp[0].')';
		}
		 
		preg_match("/\[js\]\(.\/([^\.]*\.js)/", $arr[3], $tmp);
		if(file_exists($tmp[1]) && filesize($tmp[1]) > 20){
			$res .= " ".$tmp[0].')';
		} 

		preg_match("/\[java\]\(.\/([^\.]*\.java)/", $arr[3], $tmp);
		if(file_exists($tmp[1]) && filesize($tmp[1]) > 20){
			$res .= " ".$tmp[0].')';
		}

		$arr[3] = $res;
		preg_match("/\[essence\]\(.\/([^\.]*\.md)/", $arr[5], $tmp);
		if(!file_exists($tmp[1]) || filesize($tmp[1]) < 20){
			$arr[5]= ' ';
		} 
		fwrite($f2, join('|', $arr));
	}
}