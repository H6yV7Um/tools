

#dir=$1
#filename=`basename $dir`
#echo $filename
#cat $dir/* > /tmp/$filename

#head /tmp/abc | awk 'BEGIN{array["hi"]=2;} {if($1 in array){array[$1]+=int($3);}else{array[$1]=int($3);}} END{for(item in array){print item,array[item];}'
cat /tmp/v2_map_ipad_imei_one_day_less.20130623.part1 | awk 'BEGIN{array["hi"]=2;} {if(($1,$2,$5) in array){array[$1,$2,$5]+=int($3);}else{array[$1,$2,$5]=int($3);}} END{for(item in array){split(item, array2, SUBSEP);print array2[1],array2[2],array2[3],array[item];}}'  > /tmp/haha
#head /tmp/abc | awk 'BEGIN{array["hi"]=2;} {if($1 in array){array[$1]+=int($3);}else{array[$1]=int($3);}} END{for(item in array){print item,array[item];}}' 

