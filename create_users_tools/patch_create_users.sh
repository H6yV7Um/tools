

while read line
do
	echo $line
	sudo bash create_user.sh $line
done < abc
