# Read from the file file.txt and output the tenth line to stdout.
cat file.txt | awk '{if (NR==10) print $0}' #awk 'NR==10 {print}' file.txt
sed -n 10p <file.txt
awk '{if (NR==10) print $0}' <file.txt


count=0
while read line
   do count=$[$count+1] #let $count=$count+1
   if [ $count -eq 10 ] # [ "$count" -eq 10 ]
        then echo $line  
    fi   
done < file.txt


# Solution 1
cnt=0
while read line && [ $cnt -le 10 ]; do
  let 'cnt = cnt + 1'
  if [ $cnt -eq 10 ]; then
    echo $line
    exit 0
  fi
done < file.txt

# Solution 2
awk 'FNR == 10 {print }'  file.txt
# OR
awk 'NR == 10' file.txt

# Solution 3
sed -n 10p file.txt

# Solution 4
tail -n+10 file.txt|head -1