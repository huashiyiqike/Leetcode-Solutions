# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | awk '{
for(i=1;i<=NF;i++){count[$i]++;}
}
END{
    for(i in count){
        print i, count[i];
    }
}' | sort -k2nr